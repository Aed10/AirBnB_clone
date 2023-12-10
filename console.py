#!/usr/bin/python3
"""This module defines a command interpreter for AirBnB clone"""
import cmd
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
    classes = {"BaseModel", "User", "State", "City",
                            "Amenity", "Place", "Review"}

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

    def default(self, arg):
        """Called on an input line when the command prefix is not recognized"""
        args = arg.split(".")
        if args[0] in HBNBCommand.classes:
            if args[1] == "all()":
                self.do_all(args[0])
            elif args[1] == "count()":
                self.do_count(args[0])
            elif args[1].startswith("show("):
                self.do_show(args[0] + " " + args[1][6:-2])
            elif args[1].startswith("destroy("):
                self.do_destroy(args[0] + " " + args[1][9:-2])
            elif args[1].startswith("update("):
                args[1] = args[1][7:-1]
                args[1] = args[1].replace('"', "")
                args[1] = args[1].replace("'", "")
                args[1] = args[1].replace(",", "")
                args[1] = args[1].replace("{", "")
                args[1] = args[1].replace("}", "")
                args[1] = args[1].split()
                self.do_update(
                    args[0] + " " + args[1][0] + " " + args[1][1] + " " +
                    args[1][2])
        else:
            print("*** Unknown syntax: {}".format(arg))
    def do_count(self, arg):
        """Retrieve the number of instances of a class"""
        count = 0
        for key in models.storage.all():
            if key.startswith(arg + "."):
                count += 1
        print(count)

    def do_BaseModel(self, arg):
        """Retrieve the number of instances of a class"""
        self.do_count("BaseModel")

    def do_User(self, arg):
        """Retrieve the number of instances of a class"""
        self.do_count("User")

    def do_State(self, arg):
        """Retrieve the number of instances of a class"""
        self.do_count("State")

    def do_City(self, arg):
        """Retrieve the number of instances of a class"""
        self.do_count("City")

    def do_Amenity(self, arg):
        """Retrieve the number of instances of a class"""
        self.do_count("Amenity")

    def do_Place(self, arg):
        """Retrieve the number of instances of a class"""
        self.do_count("Place")

    def do_Review(self, arg):
        """Retrieve the number of instances of a class"""
        self.do_count("Review")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
