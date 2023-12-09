# AirBnB_clone

## Description
This repository contains the first step towards building our first full web application: the AirBnB clone. This first step consists of a command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging).

## Usage
To use the console, run the executable ./console.py. The console will display a prompt (hbnb) where you can type commands. To exit the console, type quit, EOF (Ctrl + D), or exit.

## Commands
The console supports the following commands:

* create: Creates a new instance of a class and saves it to a JSON file.
* show: Prints the string representation of an instance based on the class name and id.
* destroy: Deletes an instance based on the class name and id.
* all: Prints all string representation of all instances based or not on the class name.

## Examples
```
$ ./console.py
(hbnb) create BaseModel
d0fbae1e-7f1e-4f0b-83d0-0b1b5b4fbded
(hbnb) show BaseModel d0fbae1e-7f1e-4f0b-83d0-0b1b5b4fbded
[BaseModel] (d0fbae1e-7f1e-4f0b-83d0-0b1b5b4fbded) {'id': 'd0fbae1e-7f1e-4f0b-83d0-0b1b5b4fbded', 'created_at': datetime.datetime(2020, 7, 1, 21, 50, 5, 698000), 'updated_at': datetime.datetime(2020, 7, 1, 21, 50, 5, 698000)}
(hbnb) destroy BaseModel d0fbae1e-7f1e-4f0b-83d0-0b1b5b4fbded
(hbnb) show BaseModel d0fbae1e-7f1e-4f0b-83d0-0b1b5b4fbded
** no instance found **
(hbnb) all
["[BaseModel] (d0fbae1e-7f1e-4f0b-83d0-0b1b5b4fbded) {'id': 'd0fbae1e-7f1e-4f0b-83d0-0b1b5b4fbded', 'created_at': datetime.datetime(2020, 7, 1, 21, 50, 5, 698000), 'updated_at': datetime.datetime(2020, 7, 1, 21, 50, 5, 698000)}"]

```

## Authors
* **Ayoub Ed dyyany** - [Aed10](https://github.com/Aed10)


