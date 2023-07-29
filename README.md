# AirBnB Clone - The Console

The AirBnB Clone project at Holberton School aims to build a simple copy of the AirBnB website (HBnB) with a command-line interface for managing objects.

## Functionalities of this command interpreter:

* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database, etc.
* Perform operations on objects (count, compute stats, etc.)
* Update attributes of an object
* Destroy an object

## Table of Contents

* [Environment](#environment)
* [Installation](#installation)
* [File Descriptions](#file-descriptions)
* [Usage](#usage)
* [Examples of Use](#examples-of-use)
* [Bugs](#bugs)

## Environment

This project is interpreted and tested on Ubuntu 14.04 LTS using Python 3 (version 3.4.3).

## Installation

1. Clone this repository:
```bash
git clone https://github.com/gebretwodros73/AirBnB_clone_v3.git
```
2. Access AirBnb directory:
```bash
cd AirBnB_clone_v3
```
3. Run the command-line interface (interactively):
```bash
./console
```
and enter commands.
4. Run the command-line interface (non-interactively):
```bash
echo "<command>" | ./console.py
```

## File Descriptions

* `console.py` - The console contains the entry point of the command interpreter.
List of commands this console currently supports:
* `EOF` - exits console
* `quit` - exits console
* `<emptyline>` - overwrites default emptyline method and does nothing
* `create` - Creates a new instance of `BaseModel`, saves it (to the JSON file), and prints the id
* `destroy` - Deletes an instance based on the class name and id (save the change into the JSON file).
* `show` - Prints the string representation of an instance based on the class name and id.
* `all` - Prints all string representations of all instances based or not on the class name.
* `update` - Updates an instance based on the class name and id by adding or updating an attribute (save the change into the JSON file).

* `/models/` directory contains classes used for this project:

* `base_model.py` - The BaseModel class from which future classes will be derived.
   * `def __init__(self, *args, **kwargs)` - Initialization of the base model
   * `def __str__(self)` - String representation of the BaseModel class
   * `def save(self)` - Updates the attribute `updated_at` with the current datetime
   * `def to_dict(self)` - Returns a dictionary containing all keys/values of the instance

Classes inherited from Base Model:
* [amenity.py](/models/amenity.py)
* [city.py](/models/city.py)
* [place.py](/models/place.py)
* [review.py](/models/review.py)
* [state.py](/models/state.py)
* [user.py](/models/user.py)

* `/models/engine` directory contains File Storage class that handles JSON serialization and deserialization:
* `file_storage.py` - Serializes instances to a JSON file & deserializes back to instances.
   * `def all(self)` - Returns the dictionary __objects
   * `def new(self, obj)` - Sets in __objects the obj with key <obj class name>.id
   * `def save(self)` - Serializes __objects to the JSON file (path: __file_path)
   * `def reload(self)` - Deserializes the JSON file to __objects

* `/tests` directory contains all unit test cases for this project:

Test files for each class:
* [/test_models/test_base_model.py](/tests/test_models/test_base_model.py)
* [/test_models/test_amenity.py](/tests/test_models/test_amenity.py)
* [/test_models/test_city.py](/tests/test_models/test_city.py)
* [/test_models/test_file_storage.py](/tests/test_models/test_file_storage.py)
* [/test_models/test_place.py](/tests/test_models/test_place.py)
* [/test_models/test_review.py](/tests/test_models/test_review.py)
* [/test_models/test_state.py](/tests/test_models/test_state.py)
* [/test_models/test_user.py](/tests/test_models/test_user.py)

## Usage

To run the command interpreter, execute `./console` in the project directory. You will then be able to use the supported commands to manage objects in the AirBnB website.

## Examples of use
```
vagrantAirBnB_clone$./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) all MyModel
** class doesn't exist **
(hbnb) create BaseModel
7da56403-cc45-4f1c-ad32-bfafeb2bb050
(hbnb) all BaseModel
[[BaseModel] (7da56403-cc45-4f1c-ad32-bfafeb2bb050) {'updated_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772167), 'id': '7da56403-cc45-4f1c-ad32-bfafeb2bb050', 'created_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772123)}]
(hbnb) show BaseModel 7da56403-cc45-4f1c-ad32-bfafeb2bb050
[BaseModel] (7da56403-cc45-4f1c-ad32-bfafeb2bb050) {'updated_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772167), 'id': '7da56403-cc45-4f1c-ad32-bfafeb2bb050', 'created_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772123)}
(hbnb) destroy BaseModel 7da56403-cc45-4f1c-ad32-bfafeb2bb050
(hbnb) show BaseModel 7da56403-cc45-4f1c-ad32-bfafeb2bb050
** no instance found **
(hbnb) quit
```

## Bugs
No known bugs at this time. 

## Author
Tewodros Gebre- [Github](https://github.com/gebretwodros73)

Zerihun Mohammed - [Github](https://github.com/)

## License
Public Domain. No copy write protection. 
