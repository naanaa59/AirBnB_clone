#!/usr/bin/python3
"""
This class (program) contains the entry point of
the command interpreter:
"""


import cmd
import re
import shlex
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models import storage


validated_classes = {
            'BaseModel': BaseModel, 'User': User,
            'State': State, 'Place': Place, 'City': City,
            'Amenity': Amenity, 'Review': Review}


def validated_args(args, check_id=False):
    """Checks on args to validated classname entry"""
    if len(args) < 1:
        print("** class name missing **")
        return False
    class_name = args[0]
    if class_name not in validated_classes and class_name not in globals():
        print("** class doesn't exist **")
        return False
    if len(args) < 2 and check_id:
        print("** instance id missing **")
        return False
    return True


class HBNBCommand(cmd.Cmd):
    """
        contains: EOF, quit commands to exit the program
        + prompt

    """
    prompt = "(hbnb) "

    def do_create(self, arg):
        """Create command creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if not validated_args(args):
            return
        new_instance = validated_classes[args[0]]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Show command Prints the string representation
of an instance based on the class name and id."""
        args = arg.split()

        if not validated_args(args, check_id=True):
            return
        obj = storage.all()
        key = f"{args[0]}.{args[1]}"
        req_instance = obj.get(key, None)
        if req_instance is None:
            print("** no instance found **")
            return
        print(req_instance)

    def do_all(self, arg):
        """all command Prints all string representation
of all instances based or not on the class name."""

        args = arg.split()
        objects = storage.all()
        if len(args) < 1:
            print(["{}".format(str(obj)) for key, obj in objects.items()])
            return
        if args[0] not in validated_classes:
            print("** class doesn't exist **")
        else:
            print(["{}".format(
                str(
                    obj)) for key, obj in objects.items(

                    ) if type(obj).__name__ == args[0]])
            return

    def do_destroy(self, arg):
        """Destroy command Deletes an instance based
on the class name and id (save the change into the JSON file)."""
        args = arg.split()

        if not validated_args(args, check_id=True):
            return
        obj = storage.all()
        key = f"{args[0]}.{args[1]}"
        req_instance = obj.get(key, None)
        if req_instance is None:
            print("** no instance found **")
            return
        obj.pop(key)
        storage.save()

    def do_update(self, arg):
        """Reload command Updates an instance based on
the class name and id by adding or updating attribute
(save the change into the JSON file)."""
        args = shlex.split(arg)
        obj = storage.all()
        if not validated_args(args, check_id=True):
            return
        key = f"{args[0]}.{args[1]}"
        req_instance = obj.get(key, None)
        if req_instance is None:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
        if len(args) < 4:
            print("** value missing **")
        else:
            attr_name = args[2]
            attr_value = args[3]

            setattr(obj[key], attr_name, eval(attr_value))
            storage.save()

    def do_count(self, arg):
        """Count command counts all instances based
on their class name"""
        args = arg.split()
        objects = storage.all()
        if len(args) < 1:
            print("** class name missing **")
            return
        if args[0] not in validated_classes:
            print("** class doesn't exist **")
        else:
            count = 0
            for obj in objects.values():
                if type(obj).__name__ == args[0]:
                    count += 1
            print(count)
        return

    def default(self, arg):
        """Default behavior of an invalid syntax"""

        args = arg.split(".")
        'output [User, all()]'
        obj_id = None
        class_name = args[0]
        command = args[1].split("(")
        'output [all, id)]'
        method = command[0]
        obj = command[1].split(")")
        obj_id = obj[0]

        validated_methods = {
            'all': self.do_all,
            'count': self.do_count,
            'show': self.do_show, 'destroy': self.do_destroy,
            'update': self.do_update
            }
        if obj_id is None:
            if method in validated_methods.keys():
                return validated_methods[method](f"{class_name}")
        elif obj_id is not None:    
            return validated_methods[
                method](f"{class_name} {obj_id}")
        print("** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()