#!/usr/bin/python3
"""Module contains the entry point of the command interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """class to handle commands to the console"""

    prompt = '(hbnb) '

    def do_quit(self, *args):
        '''Quit command to exit the program'''
        return True

    do_EOF = do_quit

    def emptyline(self, *args):
        '''empty line + <enter> only returns the prompt'''
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
