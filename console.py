#!/usr/bin/python3
"""Contains the entry point of a command interpreter"""


import cmd
from datetime import datetime
import uuid


class HBNBCommand(cmd.Cmd):
    """This is the class definition for the command interpreter"""
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """ This is a method to exit the program"""
        return True

    def do_quit(self, line):
        """This is a method to quit the program"""
        return True

    def help_quit(self):
        """Gives more information on the method quit"""
        print("Quit command to exit the program")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
