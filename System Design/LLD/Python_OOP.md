
Constructor:
def __init__(self)

The Python constructor which does not accept any parameter other than self is called as default constructor.

If a constructor is defined with multiple parameters along with self is called as parameterized constructor.

You can also assign default values to the formal arguments in the constructor.

Python does not allow multiple constructors. Will only consider the last __init__() method in your class.

can overload constructors based on the type or number of arguments passed.
Using *args, args is list of parameters accesed using indexing

Destructor:
__del__(), called a destructor, that is invoked when the instance is about to be destroyed.

Python deletes unwanted objects (built-in types or class instances) automatically to free the memory space. The process by which Python periodically reclaims blocks of memory that no longer are in use is termed Garbage Collection.

Python's garbage collector runs during program execution and is triggered when an object's reference count reaches zero. An object's reference count changes as the number of aliases that point to it changes.



Access Specifiers:
By default, all the variables and methods in a Python class are public.

name: Public
_name : protected
__name: private


In Python, The underscore is only a convention meaning, not strict access controls.

For Protected:
“This is for internal use. Please don't access it unless you're sure.” Still fully accessible from outside.

For Private:
Because names starting with double underscores are name-mangled.

Python automatically rewrites:

__privgeta  →  _Trial__privgeta
__a         →  _Trial__a

But you can still access it using the mangled name:
Name mangling is the process of changing name of a member with double underscore to the form object._class__variable.

Obj._Trial__privgeta()  


Inheritance:
class Super:
    pass
class Sub(Super):
    pass (Access to attributes and methods of Super)

When instantiated Sub, Constructor of Super is called first and then Subclass.
Destructor order is reverse.

If methods with same name are defined in multiple parent classes, Python follows a specific order to decide which method to execute. This order is known as the Method Resolution Order (MRO). This order is determined by the C3 linearization algorithm, also called MRO.

First, Python looks for the method in the child class itself.
If not found, it searches the parent classes in the order they are listed.

Diamond Problem in Multiple Inheritance:
The diamond problem creates a confusion that which method to call from the base class when it is inherited by the child class. 
Python resolves this by following a the MRO.
When both B and C have same method, but D(B, C) then B's will be called.


Class method is a method that is bound to the class and not to the instance of the class. It can be called on the class itself, rather than on an instance of the class.

Static methods do not have access to the "cls" parameter or "self and therefore it cannot modify the class state. Static methods are used to access static fields of a given class. They cannot modify the state of a class since they are bound to the class, not instance.

Instance method can access the instance variables of the an object. It can also access the class variable as it is common to all the objects. A method with self as one of the formal arguments is called instance method, as it is called by a specific object.

@classmethod
def showcount(cls):
    print (cls.empCount)


The getattr(obj, name[, default]) − to access the attribute of object.

The hasattr(obj,name) − to check if an attribute exists or not.

The setattr(obj,name,value) − to set an attribute. If attribute does not exist, then it would be created.

The delattr(obj, name) − to delete an attribute.



There are four ways to implement polymorphism in Python −

Duck Typing
Operator Overloading
Method Overriding
Method Overloading


Duck Typing:
you can call any method on an object without checking its type, as long as the method exists.



To create an abstract class in Python, it must inherit the ABC class that is defined in the ABC module. 
An abstract method is the one which cannot be called but can be overridden. You need to decorate it with @abstractmethod decorator.


Interface
An abstract class and interface appear similar in Python. The only difference in two is that the abstract class may have some non-abstract methods, while all methods in interface must be abstract, and the implementing class must override all the abstract methods.

from abc import ABC, abstractmethod

# creating interface
class demoInterface(ABC):
    @abstractmethod
    def method1(self):