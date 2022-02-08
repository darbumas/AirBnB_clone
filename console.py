#!/usr/bin/python3
"""Module contains the entry point of the command interpreter"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import models


class HBNBCommand(cmd.Cmd):
    """class to handle commands to the console"""
    instance_dict = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
                     'State': State, 'City': City, 'Amenity': Amenity,
                     'Review': Review}
    prompt = '(hbnb)'

    def do_quit(self, *args):
        '''Quit command to exit the program'''
        return True

    do_EOF = do_quit

    def emptyline(self, *args):
        '''empty line + <enter> only returns the prompt'''
        pass

    def do_create(self, arg):
        '''Creates a new instance of BaseModel, saves it (to the JSON file) and
        prints the id'''
        if not arg or len(arg) == 0:
            print("** class name missing **")
        elif arg not in self.instance_dict.keys():
            print("** class doesn't exist **")
        else:
            obj = self.instance_dict[arg]()
            print(obj.id)

    def do_show(self, arg):
        '''Prints the string representation of an instance based on the class
        name and id'''
        if not arg or len(arg) == 0:
            print("** class name missing **")
        cmds = arg.split(" ")
        if cmds[0] not in self.instance_dict.keys():
            print("** class doesn't exist **")
        elif len(cmds) < 2:
            print("** instance id missing **")
        else:
            my_dict = models.storage.all()
            my_string = str(cmds[0] + '.' + cmds[1])
            for key, val in my_dict.items():
                if key == my_string:
                    print(val)
                    return
            print("** no instance found **")

    def do_destroy(self, arg):
        '''Deletes an instance based on the class name and id'''
        cmds = arg.split(" ")
        if not arg or len(arg) == 0:
            print("** class name missing **")
        elif cmds[0] not in self.instance_dict.keys():
            print("** class doesn't exist **")
        elif len(cmds) < 2:
            print("** instance id missing **")
        else:
            my_dict = models.storage.all()
            my_string = str(cmds[0] + '.' + cmds[1])
            for key in my_dict.keys():
                if key == my_string:
                    my_dict.pop(key)
                    models.storage.save()
                    return
            print("** no instance found **")

    def do_all(self, arg):
        '''Prints all string representation of all instances based or not on the
        class name'''
        cmds = arg.split(" ")
        my_dict = models.storage.all()
        if len(arg) == 0:
            for v in my_dict.values():
                print(v)
        elif cmds[0] not in self.instance_dict.keys():
            print("** class doesn't exist **")
        else:
            for key, val in my_dict.items():
                cls_name = key.split('.')
                if cls_name[0] == cmds[0]:
                    print(val)

    def do_update(self, arg):
        '''Updates an instance based on the class name and id by adding or
        updating attribute'''
        cmds = arg.split(" ")
        my_dict = models.storage.all()
        flag = 0
        if not arg or len(arg) == 0:
            print("** class name missing **")
        elif cmds[0] not in self.instance_dict.keys():
            print("** class doesn't exist **")
        elif len(cmds) < 2:
            print("** instance id missing **")
        else:
            my_string = str(cmds[0] + '.' + cmds[1])
            for key in my_dict.keys():
                if my_string == key:
                    flag = 1
                    break
            if flag == 0:
                print("** no instance found **")

        if len(cmds) < 3:
            print("** attribute name missing **")
        elif len(cmds) < 4:
            print("** value missing **")
        else:
            alt_dict = my_dict[my_string]
            try:
                attr = getattr(alt_dict, cmds[2])
                if isinstance(attr, int):
                    setattr(alt_dict, cmds[2], int(cmds[3]))
                elif isinstance(attr, float):
                    setattr(alt_dict, cmds[2], float(cmds[3]))
                else:
                    setattr(alt_dict, cmds[2], cmds[3][1:-1])
            except:
                setattr(alt_dict, cmds[2], cmds[3][1:-1])
        models.storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
