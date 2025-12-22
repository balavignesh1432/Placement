## Classes and Objects
- A class is a template; an object is an instance.
- Declare a class with `class` (start class names with uppercase, e.g., `class Main {}`).
- Create objects with `new`: `Main obj = new Main();`.
- Attributes/fields are declared outside methods and accessed with the dot operator: `obj.x;`.
- Methods are invoked the same way: `obj.func();`.
- Static members belong to the class and can be accessed via class name without an instance.
- Attributes are mutable; use `final` to prevent changes: `final int x = 10;`.
- Each object has its own field values—changing one object’s fields does not affect others.

## Method Overloading
- Method overloading allows the same name with different parameter lists (number and/or types) - Signature.
  - `float myMethod(float x)`
  - `int myMethod(int x)`
  - `double myMethod(double x, double y)`

## Constructors
- Special methods to initialize objects; name matches class and has no return type.
- Called on object creation; can set initial attribute values.
- A default constructor is provided if none is written (but cannot set custom initial values).
- `this` refers to the current object; clarifies attributes vs. parameters (`this.x = x;`). Only valid in non-static methods/constructors.
- Constructors can be overloaded.
- Use `this()` to call another constructor in the same class; it must be the first statement.
  - Example:
    - `public Main(String name) { this(2020, name); }`
- Private constructor prevents external instantiation.

## Copy Constructor
- Simple assignment copies references only (shallow Copy): `Complex c3 = c2;`.
- Java does not provide a default copy constructor; you must write one.
  - Example:
    - `public Person(Person another) { this(another.name, another.age); }`
    - Usage: `Person b = new Person(a);` (deep copy when implemented accordingly).

## Access Modifiers
- Classes: `public` (accessible everywhere) or default/package-private (accessible within the same package).
- Members (fields, methods, constructors):
  - `public`: accessible everywhere
  - default/package-private: accessible within the same package
  - `protected`: accessible in the same package and in subclasses
  - `private`: accessible only within the declaring class
- Default is used when none is specified.

## Non-Access Modifiers
- Classes:
  - `final`: cannot be inherited.
  - `abstract`: cannot be instantiated.
- Fields/Methods:
  - `final`: value or implementation cannot be overridden.
  - `static`: belongs to the class; accessible without an instance (or via class name).
  - `abstract`: declared in abstract classes; no body, subclass provides implementation.
- Static methods cannot be overridden.

## Encapsulation
- Hide sensitive data by making attributes `private`.
- Expose `public` getters/setters to read/update private fields.
  - Naming convention: `getName()`, `setName(...)`.
  - Read-only with only getter; write-only with only setter.

## Inheritance
- `extends` enables inheriting attributes and methods.
  - `class Super {}` → `class Sub extends Super {}`
  - `Super base = new Sub();`
- `super` refers to the parent:
  - Access parent attributes/methods.
  - Call parent constructor.
- Methods can be overridden; fields are not overridden (use `super` to access shadowed fields).
- Visibility when overriding can widen or stay the same:
  - Public → Public
  - Protected → Protected/Public
  - Default → Default/Protected/Public
- `super()` must be the first statement in a subclass constructor.
  - Example:
    - `Sub() { super(); }`

## Abstraction and Interfaces
- Abstraction hides details while exposing essentials; use abstract classes or interfaces.
- Abstract classes:
  - Cannot be instantiated.
  - May contain abstract and concrete methods.
  - Declared with `abstract class Name {}`; abstract methods `abstract void method();`.
- Interfaces:
  - Purely abstract types; no constructors.
  - Methods are implicitly abstract and public; attributes are public, static, and final.
  - Implement with `implements`; cannot be instantiated.
  - Multiple interfaces allowed: `class Demo implements FirstInterface, SecondInterface {}`.
  - Only abstract methods → no implementation ambiguity → no diamond problem.

## Marker Interfaces
- Marker interfaces: empty interfaces (e.g., `Serializable`, `Cloneable`, `Remote`).
- Marker interfaces give information to the JVM or compiler about:
- How to treat the object, What operation is allowed/disallowed, What special behavior should be applied

## Cloning
  - Implement `Cloneable` and override `clone()`.
  - `clone()` creates a new object copy; reduces manual copying.
  - Default `Object.clone()` performs Shallow Cloning; Deep Cloning requires custom logic.
  - Shallow Cloning copies first level structures but shares nested objects; deep Cloning clones all.
  - Example:
    - `public Object clone() throws CloneNotSupportedException { return super.clone(); }`
    - Invoke like method of class and type cast with class name: `Classname b = (Classname) a.clone();`