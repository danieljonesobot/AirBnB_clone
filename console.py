#!/usr/bin/python3
""" this module contains the entry point of the command interpreter:
"""
import cmd
from models.base_model import BaseModel
import re
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


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

    def do_all(self, line):
        """ this command retrieves all instances of a class """
        args = line.split()
        if len(args) > 0 and args[0] not in HBNBCommand.__theclasses:
            print("** class doesn't exist **")
        else:
            object_list = []
            for instance in storage.all().values():
                if len(args) > 0 and args[0] == instance.__class__.__name__:
                    object_list.append(instance.__str__())
                elif len(args) == 0:
                    object_list.append(instance.__str__())
            print(object_list)

    def default(self, line):
        """ this function handles when a command isn't recognized """
        command_mapping = {
            "all": self.do_all,
            "destroy": self.do_destroy,
            "update": self.do_update,
            "show": self.do_show,
            "count": self.do_count
        }

        parts = line.split('.')
        if len(parts) == 2:
            class_name, method_and_args = parts
            method_match = re.match(r'^(\w+)\((.*)\)$', method_and_args)

            if method_match:
                method_name = method_match.group(1)
                method_args = method_match.group(2)

                if method_name in command_mapping:
                    full_command = f"{class_name} {method_args}"
                    return command_mapping[method_name](full_command)

        print("*** Unknown syntax: {}".format(line))
        return False

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

    def do_count(self, line):
        """ this action retrives the number of instances of a class """
        args = line.split()
        a = storage.all().values()
        if len(args) > 0 and args[0] in HBNBCommand.__theclasses:
            ce = args[0]
            c = sum(1 for i in a if i.__class__.__name__ == ce)
            print(c)
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
