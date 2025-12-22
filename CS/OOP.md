# Object-Oriented Programming (OOP)

## Overview

OOP is a programming paradigm — a way of organizing code that uses **objects** and **classes** to represent real-world entities and their behavior.

### Key Characteristics
- **Object**: Has attributes (specific data) and can perform certain actions using methods
- **Organizes code** into classes and objects
- **Improves** modularity, scalability, and maintainability
- **Bottom-up approach** (unlike Procedural programming which uses top-down)

---

## Procedural Programming vs OOP

### Procedural Programming Paradigm
- Logic broken down into smaller, independent, reusable blocks called **functions**
- Data can be shared via arguments; results returned to calling function

**Problems:**
- Top-down approach makes programs difficult to maintain
- Uses many global data items (undesired)

### OOP Approach
- Defines attributes and functionality as a single unit called a **class** (blueprint)
- Organizes code bottom-up for better maintainability

---

## Core Concepts: Classes and Objects

### Class
- A **blueprint** for objects with similar attributes and behavior
- Defines a set of attributes and methods that created objects (instances) can have
- **No memory allocated** when defined

### Object
- An **instance of a class** — a specific implementation
- **Memory allocated** when instantiated
- Represents real-world entities

### Object Structure

An object consists of three components:

| Component | Definition |
|-----------|-----------|
| **State** | Represented by attributes; reflects properties of the object |
| **Behavior** | Represented by methods; reflects response to other objects |
| **Identity** | Unique name; enables interaction with other objects |

### Constructors
- Special methods that initialize objects upon creation
- Have No return type

### Destructors
- A special member function that is automatically called when an object is destroyed. 
- Its primary purpose is to clean up resources the object was using, such as deallocating memory, closing files, or terminating network connections.
---

## The Four OOP Principles

### 1. Encapsulation (Data Hiding)

**Definition:** Wrapping data (variables) and code (methods) together into a single unit (class).

**Key Points:**
- Restricts direct access to object components
- Protects data integrity and prevents unintended modifications
- Data members only accessible to functions defined within the class
- Also known as **data-hiding**

**Example:** Private variables with public getter/setter methods

- Private members − They can be accessed from within the class only.

- Protected members − They are accessible from within the class as well as by classes derived from that class.

- Public members − A class member is said to be public if it can be accessed from anywhere in the program.

---

### 2. Inheritance (IS A Relationship)

**Definition:** A mechanism where a child class derives properties and behaviors from a parent class.

### Child Class Capabilities
- Uses attributes and methods of the parent class
- Overrides parent class methods for specific implementation
- Adds its own additional attributes and methods

### Benefits
- **Code Reusability:** Avoids duplication by reusing parent class components
- **Improves Maintainability:** Reduces redundancy, easier to manage
- **Enhances Extensibility:** Add new functionality without modifying existing code

### Types of Inheritance

| Type | Definition |
|------|-----------|
| **Single** | Subclass inherits from one superclass |
| **Multilevel** | Subclass inherits from another class, which inherits from another (chain) |
| **Hierarchical** | Single parent class has multiple child classes |
| **Multiple** | Subclass inherits from multiple parent classes *(Not supported by Java)* |

---

### 3. Abstraction (Hiding Complexity)

**Definition:** Showing only essential details and hiding the implementation.

**Benefits:**
- Allows programmers to focus on **what** an object does, not **how** it does it
- Reduces complexity by hiding unnecessary implementation details
- Implemented using **Abstract Classes** and **Interfaces**

**Example:** Driver only knows pressing the accelerator increases speed; doesn't know the internal mechanism

#### Abstract Class
- Used to define common behavior subclasses should implement
- Abstract methods are **declared but not implemented**
- Enables **partial abstraction** (can have both abstract and concrete methods)
- Subclasses must provide concrete implementations (unless subclass is also abstract)
- Cannot be instantiated. **Cannot have constructors**

#### Concrete Class
- Has implementation for **all** of its methods

#### Interface (Realization)
- Promotes **full abstraction** (hides all implementation details)
- Contains **only abstract methods**
- Implementation must define all methods and provide implementation
- **Cannot have constructors**

---

### 4. Polymorphism (Many Forms)

**Definition:** Allows a method, function, or object to behave differently based on context.

**Key Features:**
- Enables dynamic method resolution and method flexibility
- Makes applications easier to extend and maintain
- Each subclass provides its own implementation of an abstract method in base class
- **Code Reusability:** Write a single interface that works for multiple types

**Example:** A person at the same time is a father, husband, and employee — possessing different behavior in different situations

#### Types of Polymorphism

#### Static / Compile-Time Polymorphism: Early Binding (Code execution decided at **compile time**)
- Object linked with function/operator **during compile time** based on values
- **Method/Function Overloading:** Use single method name for similar operations (reduces redundancy). Differing by signatures (type and number of parameters)
- **Operator Overloading**

#### Dynamic / Run-Time Polymorphism: Late Binding (Code execution decided at **runtime** in response to function call)
- **Method Overriding:** Subclass method overrides base class method. Achieved by dynamic binding.


## Object Relationships

- **HAS-A (Unidirectional):** One class contains/references another as a field; represents composition or aggregation.
- **Aggregation:** HAS-A where the contained object can exist independently.
- **Composition:** HAS-A where the contained object cannot exist without the container; child objects depend on the parent’s lifetime.
- **KNOWS-A (Bidirectional):** Two classes reference each other to collaborate. It represents **Association**. 
- **Dependency (One-time interaction):** Method takes object of another as method parameters, as local variables, or return type as another Object.

