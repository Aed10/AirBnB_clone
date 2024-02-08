#!/usr/bin/python3
"""This module defines a command interpreter for AirBnB clone"""
import cmd
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.place import Place
import models


class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""

    prompt = "(hbnb) "
    classes = {"BaseModel", "User", "State", "City", "Amenity", "Place", "Review"}

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing when empty line is entered"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id"""
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class
        name and id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key in models.storage.all():
                print(models.storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id (save the change
        into the JSON file)"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key in models.storage.all():
                del models.storage.all()[key]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of
            all instances based or not on the
        class name"""
        args = arg.split()
        if not arg:
            print([str(value) for value in models.storage.all().values()])
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            print(
                [
                    str(value)
                    for key, value in models.storage.all().items()
                    if key.startswith(args[0] + ".")
                ]
            )

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file)"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = args[0] + "." + args[1]
            if key in models.storage.all():
                setattr(models.storage.all()[key], args[2], args[3])
                models.storage.save()
            else:
                print("** no instance found **")

    def do_count(self, arg):
        """
        Retrieve the number of instances of a class

        Args:
            arg (str): The class name

        Returns:
            int: The number of instances of the class

        """

        count = 0
        for key in models.storage.all():
            if key.startswith(arg + "."):
                count += 1
        print(count)

    def default(self, line: str) -> None:
        """
        This function is the default method of the HBNBCommand class.
        It is called when the user enters a command that does not match any of the other methods.

        Args:
            line (str): The command entered by the user.

        Returns:
            None: This function does not return any values.

        Raises:
            None: This function does not raise any exceptions.

        """
        if "." in line:
            parts = line.split(".", 1)

            if len(parts) == 2:
                funct = {"all": self.do_all, "count": self.do_count}
                if parts[1] in funct and parts[0] in self.classes:
                    funct[parts[1]](parts[0])
                else:
                    print(f"** {parts[1]} or {parts[0]} not defined **")
        else:
            return cmd.Cmd.default(self, line)

    def do_clear(self, arg):
        """Clears the screen"""
        os.system("cls" if os.name == "nt" else "clear")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
