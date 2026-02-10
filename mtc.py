# Metaclases = Class OF A CLASS

class Student:
    pass

print(type(Student))

# How to create metaclass

class Dog:
    pass
Dog = type("Dog",(),{})

class MyMeta(type):
    def __new__(cls,name,bases,attrs):
        print(f"MyMeta Class: Creating classes:{name}")
        return super().__new__(cls,name,bases,attrs)
class Dog(metaclass=MyMeta):
    pass

class EnforceHelloMeta(type):
    def __new__(cls,name,bases,attrs):
        if "say_hello" not in attrs:
            raise TypeError(f"{name}must define say_hello!")
        
        if not name.startswith("A"):
            raise ValueError("Class Name Must Start With A")
         
        return super().__new__(cls,name,bases,attrs) 

class Animal(metaclass=EnforceHelloMeta):
    def say_hello(self):
        print("Jungle")

class Anaconda(metaclass=EnforceHelloMeta):
    def say_hello(self):
        print("Hissss!")
anaconda: Anaconda = Anaconda()
anaconda.say_hello()
animal: Animal = Animal()
animal.say_hello()        
    
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args,**kwargs)
        return cls._instances[cls]
    
class Database(metaclass=Singleton):
    pass

db1: Database = Database()
db2: Database = Database()
print(db1 is db2)
 
# Before dataclass, a typical Python class for holding
#  data might look like this:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        return False

person: Person = Person("Alice", 30)
print(person)

# With dataclass, the code becomes much simpler
from dataclasses import dataclass
@dataclass(unsafe_hash=True)
class Person:
    name : str
    age : int

person1 = Person("Alice", 30)
person2 = Person("Bob", 25)
person3 = Person("Alice", 30)
per_set = {person1,person2}
print(per_set)
person1.age = 40
print(person1)
person2.age = 30 # (Unsafe Hash) We can use for change the value of the
print(person2)   # field even if we have hashable dataclass
person3.age = 27
print(person3)    

@dataclass
class Point:
    A: float
    Y: float

point1: Point = Point(1.0, 2.0)
point2: Point = Point(1.0, 2.0)

print(point1 == point2)  

@dataclass(frozen=True)
class Config:
    api_key: str
config = Config(api_key="secret")    

@dataclass
class Person:
    name:  str
    age : int

    def _post_init__(self):
        self.adult = self.age >= 18
        print("post init called")
        
Person = Person("Haris", 20)

from dataclasses import dataclass
from typing import Optional
@dataclass
class Person:
    name: str
    age: int
    occupation: Optional[str] = None

    def greet(self) -> None:
        """Print Is A Greeting Message"""
        print(f"Hello, my name is {self.name} and I am {self.age} years old.And My Occupation Is {self.occupation}")
person = Person("Mustafa",18,"Agentic AI Develepor")
print(person)
person.greet()
    
from dataclasses import dataclass, field
from typing import ClassVar, Final
@dataclass
class Person:
    name : str
    age :int
    occupation: str = "Unkown"
    species: ClassVar[str]= "Homo sapiens"

    @classmethod
    def get_species(cls):
        return cls.species
Mustafa = Person("Mustafa",18,"Agentic AI Developer")
Ali = Person("Ali",25,"Charterd Accountant")
print(Mustafa.get_species())
print(Ali.get_species())

Person.species = "New Species"

print(Mustafa.get_species())
print(Ali.get_species())

from dataclasses import dataclass
from typing import Final, Optional

@dataclass
class Person:
    name: str
    age: int
    occupation: Optional[str] = None

    VERSION: Final[str] = '1.0.0'

    @staticmethod
    def get_version() -> str:
        return Person.VERSION

person = Person("Mustafa", 30, "Software Engineer")
print(person.get_version())  

person1 = Person("Mustafa", 30, "Software Engineer")
person2 = Person("Ali", 25, "Doctor")

print(Person.get_version())

from typing import Any
import random
def print_value(value: Any) -> None:
    print("print_value",type(value),":",value)
print_value(332)
print_value("Hello Mustafa !")
def get_value() -> Any:
    data_list : list = [42,"Agentic AI Developer",3.14,{"key":"value"},False]
    random_index = random.randint(0, len(data_list) - 1)
    return data_list[random_index]
value = get_value()
print("get_value:",type(value),":",value)