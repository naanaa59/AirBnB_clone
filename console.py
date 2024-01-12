#!/usr/bin/python3
"""
This class (program) contains the entry point of
the command interpreter:
"""
import cmd
from models.base_model import BaseModel
from models import storage

validated_classes = {'BaseModel': BaseModel}

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
            print(["{}".format(str(obj)) for key, obj in objects.items()])
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
        args = arg.split()
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

