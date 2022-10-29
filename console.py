#!/usr/bin/python3
"""Contains the entry point of a command interpreter"""
<<<<<<< HEAD
import cmd
=======


import cmd
from datetime import datetime
import uuid
>>>>>>> console


class HBNBCommand(cmd.Cmd):
    """This is the class definition for the command interpreter"""
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """ This is a method to exit the program"""
        return True

<<<<<<< HEAD
    def help_EOF(self):
        """ This helps to quit the program """
        print("This also quits program\n")

=======
>>>>>>> console
    def do_quit(self, line):
        """This is a method to quit the program"""
        return True

    def help_quit(self):
        """Gives more information on the method quit"""
<<<<<<< HEAD
        print("Quit command to exit the program\n")

    def emptyline(self):
        """when line is empty print nothing"""
        pass
=======
        print("Quit command to exit the program")
>>>>>>> console


if __name__ == "__main__":
    HBNBCommand().cmdloop()
