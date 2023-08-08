#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    intro = 'Welcome to the turtle shell.   Type help or ? to list commands.\n'
    prompt = '(hbnb)'

    def do_EOF(self, line):
        return True
    


if __name__ == '__main__':
    HBNBCommand().cmdloop()
