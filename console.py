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
    prompt = '(hbnb)'
    __theclasses = {
            "BaseModel",
            "User",
            "Amenity",
            "City",
            "Place",
            "Review",
            "State"
            }

    def do_quit(self, line):
        """Quit command to exit the program"""
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
            print(eval(argus[0])().id)
            storage.save()

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
        argum = ln.split()
        dicti = storage.all()
        if len(argum) == 0:
            print("** class name missing **")
            return
        elif argum[0] not in HBNBCommand.__theclasses:
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

    def do_update(self, line):
        """ method to define the action update and instance"""
        args = line.split()
        class_name = args[0]
        instance_id = args[1]
        attribute_name = args[2]
        attribute_value = args[3]
        key = "{}.{}".format(class_name, instance_id)
        instance = storage.all()[key]

        if len(args) == 0:
            print("** class name missing **")
            return

        if class_name not in HBNBCommand.__theclasses:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        if key not in storage.all().keys():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        setattr(instance, attribute_name, attribute_value)
        instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
