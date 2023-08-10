#!/usr/bin/python3
""" this module contains the entry point of the command interpreter:
"""
import cmd
from models.base_model import BaseModel
import re
from models import storage


class HBNBCommand(cmd.Cmd):
    """ this is the cmd class
    """
    intro = 'Welcome to the command interpreter.   Type help or ? to list commands.\n'
    prompt = '(hbnb)'
    __theclasses = {
            "BaseModel",
            }

    def do_quit(self, line):
        """ this will exit the program """
        return True

    def do_EOF(self, line):
        """ this will exit the program on EOF """
        print()
        return True

    def emptyline(self):
        """ does nothing on empty line """
        pass

    def do_create(self, ln):
        """ craetes a new instance of BaseModel """
        argus = ln.split()
        if len(argus) == 0:
            print("** class name missing **")
        elif argus[0] not in HBNBCommand.__theclasses:
            print("** class doesn't exist **")
        else:
            obj = storage.classes[argus[0]]()
            obj.save()
            print(obj.id)

    def do_show(self, ln):
        """ prints the string representation of an instance
        """
        argum = ln.split()
        dictObj = storage.all()
        if len(argum) == 0:
            print("** class name missing **")
        elif argum[0] not in HBNBCommand.__theclasses:
            print("** class doesn't exist **")
        elif len(argum) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(argum[0], argum[1]) not in dictObj:
            print("** no instance found **")
        else:
            insts = dictObj["{}.{}".format(argum[0], argum[1])]
            print(insts)
    def do_destroy(self, ln):
        """
        this module destroys a class instance
        """
        argum = parse(ln)
        dicti = storage.all()
        if len(argum) == 0:
            print("** class name missing **")
            return
        elif argum[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        elif len(argum) == 1:
            print("** instance id missing **")
            return
        elif "{}.{}".format(argum[0], argum[1]) not in dicti.keys():
            print("** no instance found **")
            return
        else:
            del dicti["{}.{}".format(argum[0], argum[1])]
            storage.save()

    def do_all(self, ln):
        """ this method displays al the instances of a class """
        argum = ln.split()
        if len(argum) > 0 and argum[0] not in HBNBCommand.__theclasses:
            print("** class doesn't exist **")
        else:
            object_ = []
            for o in storage.all().values():
                sl = o.__class__.__name__
                if len(argum) > 0 and argum[0] == sl:
                    object_.append(o.__str__())
                elif len(argum) == 0:
                    object_.append(o.__str__())
            print(object_)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
