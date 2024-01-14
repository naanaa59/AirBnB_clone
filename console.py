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
    if not args or not args[0]:
        print("** class name missing **")
        return False
    class_name = args[0]
    if class_name not in validated_classes and class_name not in globals():
        print("** class doesn't exist **")
        return False
    if (len(args) < 2 or not args[1]) and check_id:
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
        """Creates new instance"""
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
        """Show command Prints the string representation"""
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
        """all command Prints all string representation"""

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
        """Destroy command Deletes an instance"""
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
        """Update command reloads an instance"""

        prased_arg = re.match(
            r'^(\S*)\s?(\S*)\s?("[^"]+"|\S*)?\s?("[^"]+"|\S*)', arg)
        args = list(prased_arg.groups())
        obj = storage.all()
        if not validated_args(args, check_id=True):
            return
        args[0] = args[0].strip('"')
        args[1] = args[1].strip('"')
        args[2] = args[2].strip('"')

        if not args[2]:
            print("** attribute name missing **")
            return
        if not args[3]:
            print("** value missing **")
            return
        attr_name = args[2]
        attr_value = args[3]
        try:
            attr_value = eval(attr_value)
        except Exception:
            pass
        key = f"{args[0]}.{args[1]}"
        req_instance = obj.get(key, None)
        if req_instance is None:
            print("** no instance found **")
            return
        setattr(obj[key], attr_name, attr_value)
        storage.save()

    def do_count(self, arg):
        """Count command counts all instances"""
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
        validated_methods = {
            'all': self.do_all, 'create': self.do_create,
            'count': self.do_count,
            'show': self.do_show, 'destroy': self.do_destroy,
            'update': self.do_update
            }
        command, args = self.extract(arg)
        if not args:
            print("** Unknown syntax: {}".format(arg))
            return False
        for arg in args:
            validated_methods[command](arg)
        return

    def extract(self, arg):
        command = None
        name = None
        args = None
        all_args = []
        args_list = []
        res = re.match(
            r'^\s*(\w+)\.(\w+)\((?:([{"\']?.*["\'}]?))?\)\s*$', arg)
        if res:
            name = res.group(1)
            command = res.group(2)
            args = res.group(3)
        if args:
            content = re.match(
                r'"?([^"]\S+)"?, {(.+)}', args)
        else:
            content = None
        if command == "update" and content:
            id = content.group(1)
            patt = re.compile(
                r'("[^"]+"|\S+):\s("[^"]+"|[^,]+)')
            matches = patt.findall(content.group(2))
            for match in matches:
                key = match[0]
                value = match[1]
                all_args.append(f"{id} {key} {value}")
        elif args:
            args = args.replace(',', '')
            all_args.append(
                re.sub(r'(["\'])([^"\s]*)\1', r'\2', args))
        if all_args:
            for arg in all_args:
                args_list.append(
                    f"{name} {arg}" if arg else f"{name}")
        elif name:
            args_list.append(f"{name}")
        return command, args_list

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
