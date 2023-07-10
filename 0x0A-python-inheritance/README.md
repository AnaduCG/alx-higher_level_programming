# 0x0A. Python - Inheritance
This project aims to provide a comprehensive understanding of inheritance in Python, covering topics such as superclass, subclass, attributes and methods listing, new attribute creation, class inheritance, multiple base classes, method or attribute overriding, inherited attributes and methods, the purpose of inheritance, and the usage of isinstance, issubclass, type, and super built-in functions.

## Table of Contents
-  Superclass, Baseclass, or Parentclass
-  Subclass
-  Listing Attributes and Methods
-  Adding New Attributes
-  Class Inheritance
-  Defining a Class with Multiple Base Classes
-  Default Class Inheritance
-  Method or Attribute Overriding
-  Inherited Attributes and Methods
-  Purpose of Inheritance
-  Usage of isinstance, issubclass, type, and super
### 1. Superclass, Baseclass, or Parentclass
In object-oriented programming, a superclass, baseclass, or parentclass is a class from which other classes inherit properties and methods. It serves as a template for creating derived classes.

### 2. Subclass 
A subclass is a class that inherits properties and methods from a superclass or baseclass. It can add new attributes and methods or override existing ones inherited from the superclass.

### 3. Listing Attributes and Methods
To list all attributes and methods of a class or an instance, you can use the built-in function dir(). For example:


````Python
class MyClass:
    def __init__(self):
        self.attribute = 42

    def my_method(self):
        pass

my_instance = MyClass()

print(dir(MyClass))
print(dir(my_instance))
````
Output:


```Python
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'attribute', 'my_method']
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'attribute', 'my_method']
```
4. Adding New Attributes
An instance can have new attributes assigned to it dynamically. Simply assign a value to a new attribute using dot notation. For example:


```Python
class MyClass:
    pass

my_instance = MyClass()
my_instance.new_attribute = 10
print(my_instance.new_attribute)  # Output: 10
```
## 5. Class Inheritance `<a name="class-inheritance"></a>`
To inherit a class from another, use parentheses after the class name and specify the superclass. The subclass will inherit all attributes and methods from the superclass. For example:


```Python
class SuperClass:
    def superclass_method(self):
        pass

class SubClass(SuperClass):
    pass

my_instance = SubClass()
my_instance.superclass_method()
```
## 6. Defining a Class with Multiple Base Classes
Python supports multiple inheritance, which allows a class to inherit from multiple base classes. To define a class with multiple base classes, separate them by commas in the parentheses. For example:


```Python
class BaseClass1:
    pass

class BaseClass2:
    pass

class MultiBaseClass(BaseClass1, BaseClass2):
    pass
```
## 7. Default Class Inheritance
Every class in Python inherits from the object class by default. This means that if no explicit superclass is specified, the class automatically becomes a subclass of object.

## 8. Method or Attribute Overriding
Inheritance allows subclasses to override methods or attributes inherited from the base class. To override a method, simply define a method with the same name in the subclass. For example:



```Python
class BaseClass:
    def some_method(self):
        pass

class SubClass(BaseClass):
    def some_method(self):
        # Override the method
        pass
```
## 9. Inherited Attributes and Methods
Subclasses inherit all attributes and methods from their superclass(es). They can access and use these inherited attributes and methods directly. For example:


```Python
class BaseClass:
    def base_method(self):
        pass

class SubClass(BaseClass):
    def sub_method(self):
        self.base_method()  # Accessing inherited method
```
## 10. Purpose of Inheritance
The purpose of inheritance is to enable code reuse and create hierarchical relationships between classes. It allows subclasses to inherit and extend the functionality of their superclasses, reducing code duplication and promoting modularity.

## 11. Usage of isinstance, issubclass, type, and super
 - isinstance(object, classinfo) is used to check if an object is an instance of a specified class or a subclass thereof.
 - issubclass(class, classinfo) is used to check if a class is a subclass of another class or a subclass thereof.
 - type(object) returns the type of an object. It can also be used to check the type of an object against a specific class or type.
 - super() returns a temporary object of the superclass, allowing you to call its methods. It is commonly used to invoke overridden methods in the base class.



Examples:


```Python
class ParentClass:
    def __init__(self):
        self.parent_attribute = "Parent attribute"

    def parent_method(self):
        print("Parent method")

class ChildClass(ParentClass):
    def __init__(self):
        super().__init__()
        self.child_attribute = "Child attribute"

    def child_method(self):
        print("Child method")

parent_instance = ParentClass()
child_instance = ChildClass()

print(parent_instance.parent_attribute)  # Output: Parent attribute
parent_instance.parent_method()  # Output: Parent method

print(child_instance.parent_attribute)  # Output: Parent attribute (inherited)
print(child_instance.child_attribute)  # Output: Child attribute
child_instance.parent_method()  # Output: Parent method (inherited)
child_instance.child_method()  # Output: Child method
```
### Usage of isinstance, issubclass, type, and super:


```Python
class BaseClass:
    pass

class SubClass(BaseClass):
    pass

my_instance = SubClass()

print(isinstance(my_instance, BaseClass))  # Output: True
print(issubclass(SubClass, BaseClass))  # Output: True
print(type(my_instance) == SubClass)  # Output: True

class SuperClass:
    def method(self):
        print("SuperClass method")

class OverridingClass(SuperClass):
    def method(self):
        super().method()  # Call the method in the superclass
        print("OverridingClass method")

my_instance = OverridingClass()
my_instance.method()

# Output:
# SuperClass method
# OverridingClass method
```
These examples illustrate the concepts and demonstrate the usage of inheritance and related built-in functions.