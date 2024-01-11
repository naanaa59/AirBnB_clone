#!/usr/bin/python3
"""
This class (program) contains the entry point of
the command interpreter:
"""
import cmd
from models.base_model import BaseModel
from models import storage

valdated_classes = {'BaseModel': BaseModel}
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
        class_name = arg

        try:
            class_obj = valdated_classes[class_name]
            new_instance = class_obj()
            new_instance.save()
            print(new_instance.id)

        except KeyError:
            print("** class doesn't exist **")
            
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

