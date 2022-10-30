#!/usr/bin/python3
"""Contains the entry point of a command interpreter"""
import cmd
from models.base_model import BaseModel
from models import storage
import shlex


class HBNBCommand(cmd.Cmd):
    """This is the class definition for the command interpreter"""
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """ This is a method to exit the program"""
        return True

    def help_EOF(self):
        """ This helps to quit the program """
        print("This also quits program\n")

    def do_quit(self, line):
        """This is a method to quit the program"""
        return True

    def help_quit(self):
        """Gives more information on the method quit"""
        print("Quit command to exit the program\n")

    def do_create(self, line):
        """
        Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id
        """
        if line:
            if line == "BaseModel":
                new_instance = BaseModel()
                new_instance.save()
                print(new_instance.id)

            else:
                print("** class doesn't exist **")

        else:
            print("** class name missing **")

    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        all_objs = storage.all()
        if line:
            line = line.split()
            if len(line) == 1:
                if line[0] == "BaseModel":
                    print("** instance id missing **")
                else:
                    print("** class doesn't exist **")
            elif len(line) == 2:
                name = line[0]
                name_id = line[1]
                obj_key = line[0] + "." + line[1]
                print(obj_key)
                if obj_key in all_objs.keys():
                    str_instance = all_objs[obj_key]
                    print(str_instance)
                else:
                    print("** no instance found **")
        else:
            print("** class name missing **")

    def do_destroy(self, line):
        """
        Deletes an instance based on the class nameand
        id (save the change into the JSON file)
        """
        all_objs = storage.all()
        if line:
            line = line.split()
            if len(line) == 1:
                if line[0] == "BaseModel":
                    print("** instance id missing **")
                else:
                    print("** class doesn't exist **")

            elif len(line) == 2:
                name = line[0]
                name_id = line[1]
                obj_key = f"{line[0]}.{line[1]}"

                if obj_key in all_objs.keys():
                    del all_objs[obj_key]
                    storage.save()
                else:
                    print("** no instance found **")
        else:
            print("** class name missing **")

    def do_all(self, line):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        if line:
            all_objs = storage.all()
            line = line.split()
            if len(line) == 1:
                if line[0] == "BaseModel":
                    if all_objs:
                        for value in all_objs.values():
                            print(value)
                    else:
                        pass
                else:
                    print("** class doesn't exist **")
            else:
                pass
        else:
            pass

    def emptyline(self):
        """when line is empty print nothing"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
