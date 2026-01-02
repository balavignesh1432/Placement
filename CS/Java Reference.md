# Java Reference Guide

## Table of Contents
- [Basic Syntax](#basic-syntax)
- [Data Types](#data-types)
- [Variables](#variables)
- [Operators](#operators)
- [Strings](#strings)
- [Math Functions](#math-functions)
- [Control Flow](#control-flow)
- [Loops](#loops)
- [Arrays](#arrays)
- [Methods](#methods)
- [Collections Framework](#collections-framework)

---

## Basic Syntax

### Class Structure
- Every line of code that runs in Java must be inside a class
- The class name should always start with an uppercase first letter
- Java is case-sensitive
- The name of the Java file must match the class name
- When saving the file, save it using the class name and add `.java` to the end of the filename

### Main Method
- The `main()` method is required in every Java program
- It is where the program starts running

### Code Structure
- Curly braces `{}` mark the beginning and the end of a block of code
- Each Java statement must end with a semicolon (`;`)

### Comments
```java
// Single-line comments start with two forward slashes

/* Multi-line comments 
   start with /* and end with */ */
```

### Output
- `System.out.println()` - Method to print a line of text/number to the screen
- `System.out.print()` - Similar to `println()`, but does not insert a new line at the end
- Text must be wrapped inside double quotation marks `""`
- Numbers should not be put inside double quotes

**Explanation:**
- `System` is a built-in Java class
- `out` is a member of System, short for "output"
- `println()` is a method, short for "print line"

---

## Data Types

### Primitive Data Types

#### Integer Types
| Type  | Size      | Range/Description                    | Example           |
|-------|-----------|--------------------------------------|-------------------|
| `byte`  | 1 byte (8 bits) | -128 to 127                          | `byte b = 100;`   |
| `short` | 2 bytes (16 bits) | Integer                              | `short s = 1000;` |
| `int`   | 4 bytes (32 bits) | Integer                              | `int i = -120;`   |
| `long`  | 8 bytes (64 bits) | Integer (ends with `L`)               | `long l = 15000000000L;` |

#### Floating-Point Types
| Type    | Size      | Precision        | Example              |
|---------|-----------|------------------|----------------------|
| `float`  | 4 bytes   | Up to 7 decimals | `float f = 12.23f;`  |
| `double` | 8 bytes   | Up to 15 decimals | `double d = 10.031;` |

#### Other Primitives
- `boolean` - `true` or `false`
- `char` - Single character enclosed in single quotes `'c'` or ASCII value

### Non-Primitive Data Types
- `String` - Text enclosed in double quotes `"String"`
- `Array` - Collection of elements `[]`

---

## Variables

### Declaration
```java
type variableName = value;
```

### Multiple Variables
```java
// Declare multiple variables of the same type
int x = 5, y = 7;

// Assign the same value to multiple variables
x = y = z = 50;
```

### Rules
- Cannot declare the same variable twice
- **Static Typing:** Once a variable is declared with a type, it cannot change to another type later in the program

### Float and Double
```java
// For float, add 'f' at the end of decimal number
float myFloatNum = 5.99f;

// 'd' is optional for double type
double salary = 1000.50;
// or
double salary = 1000.50d;
```

### Final Keyword (Constants)
- Declares the variable as "final" or "constant" (read-only)
- Final variables in Java are usually written in UPPER_CASE
```java
final int HEIGHT = 6;
final String BIRTHYEAR = "1990";
```

### Var Keyword
- Compiler automatically detects the type of a variable based on the value
- You cannot declare `var` without assigning a value
- Once the type is chosen, it stays the same
- Used for complex types as it is shorter
```java
var x = 5;        // Integer
var name = "John"; // String
var cars = new ArrayList<String>(); // ArrayList
```

### Type Casting

#### Widening Casting (Automatic)
Converting a smaller type to a larger type size
```java
int myInt = 9;
double myDouble = myInt; // Automatic casting: int to double
```

#### Narrowing Casting (Manual)
Converting a larger type to a smaller type size
```java
double myDouble = 9.78;
int myInt = (int) myDouble; // Manual casting: double to int
```

### String Concatenation
- The `+` operator concatenates strings
- String and int are converted to String, then appended
```java
String name = "John";
int age = 25;
System.out.println("Name: " + name);           // Name: John
System.out.println("Age: " + age);             // Age: 25
```

---

## Operators

### Arithmetic Operators
```java
+  // Addition
-  // Subtraction
*  // Multiplication
/  // Division (performs integer division or float division based on operands)
%  // Modulus (remainder)
++ // Increment
-- // Decrement
```

**Note:** For integer division, the quotient is returned (not the decimal part).

### Assignment Operators
```java
=   // Assignment
+=  // Addition assignment
-=  // Subtraction assignment
*=  // Multiplication assignment
/=  // Division assignment
%=  // Modulus assignment
&=  // Bitwise AND assignment
|=  // Bitwise OR assignment
^=  // Bitwise XOR assignment
<<= // Left shift assignment
>>= // Right shift assignment
```

### Comparison Operators
```java
==  // Equal to
!=  // Not equal to
<   // Less than
>   // Greater than
<=  // Less than or equal to
>=  // Greater than or equal to
```

### Logical Operators
```java
&&  // Logical AND
||  // Logical OR
!   // Logical NOT
```

### Operator Precedence
1. `()` - Parentheses
2. `*`, `/`, `%` - Multiplication, Division, Modulus
3. `+`, `-` - Addition, Subtraction (left to right)
4. Comparison operators (`<`, `>`, `<=`, `>=`)
5. Equality operators (`==`, `!=`)
6. `&&` - Logical AND
7. `||` - Logical OR
8. `=` - Assignment

---

## Strings

### String Methods
```java
String str = "Hello World";

str.length()        // Returns the length of the string
str.charAt(index)   // Returns char at that index
str.trim()          // Removes leading and trailing spaces
str.indexOf(str)    // Returns first index that matches string
str.toLowerCase()   // Converts to lowercase
str.toUpperCase()   // Converts to uppercase
```

### Escape Characters
```java
\\  // Backslash
\'  // Single quote
\"  // Double quote
\n  // New line
\t  // Tab
```

---

## Math Functions

All methods are part of the `Math` class`:

```java
Math.max(x, y)      // Returns the maximum value
Math.min(x, y)      // Returns the minimum value
Math.abs(x)         // Returns the absolute value
Math.sqrt(x)        // Returns the square root
Math.pow(x, y)      // Returns x raised to the power of y (returns double)
Math.round(x)       // Returns the nearest integer
Math.ceil(x)        // Returns the smallest integer >= x
Math.floor(x)       // Returns the largest integer <= x
Math.random()       // Returns random number between 0.0 and 1.0 (double)
```

---

## Control Flow

### If-Else Statements
```java
if (condition) {
    // code block
}

if (condition) {
    // code block
} else {
    // code block
}

if (condition1) {
    // code block
} else if (condition2) {
    // code block
} else {
    // code block
}
```

### Ternary Operator
```java
(condition) ? expression1 : expression2;
```

**Example:**
```java
int result = (x > y) ? x : y;
```

### Switch Statement
```java
switch(expression) {
    case value1:
        // code block
        break;
    case value2:
        // code block
        break;
    default:
        // code block
}
```

---

## Loops

### While Loop
```java
while (condition) {
    // code block
}
```

### Do-While Loop
```java
do {
    // code block
} while (condition);
```

### For Loop
```java
for (expression1; condition2; expression3) {
    // code block
    // expression1: Only executed at the start
    // condition2: Checked from the start of each iteration
    // expression3: Executed after the end of every iteration
}
```

### Enhanced For Loop (For-Each)
- Can be used directly on arrays as iterator
- Cannot be used on String (only on arrays)
```java
for (type variableName : arrayName) {
    // code block to be executed
}
```

### Loop Control Statements
- `break` - Stops and jumps out of the loop completely
- `continue` - Skips this iteration, but keeps looping

---

## Arrays

### One-Dimensional Arrays

### Declaration and Initialization
```java
// Declare an array: type followed by square brackets []
// Place values in a comma-separated list inside curly braces {}
String[] vehicles = {"car", "bike"};
int[] nums = {1, 2, 3, 4};

// Access elements
nums[0];  // First element

// Length property
nums.length;  // Returns the length of the array
```

### Creating Arrays with `new`
```java
// Create array of size n, fill later
int[] nums = new int[5];
```

### Looping Through Arrays
```java
// Traditional for loop
for (int i = 0; i < nums.length; i++) {
    System.out.println(nums[i]);
}

// Enhanced for loop
for (int num : nums) {
    System.out.println(num);
}
```

### Two-Dimensional Arrays

#### Initialization
```java
// Each row can have different length
int[][] mat = {{1, 3}, {2, 4, 5}};

// Accessing elements
mat[0][1];  // Returns 3

// Create with known dimensions (at least row count)
String[][] cars = new String[4][3];
```

#### Looping Through 2D Arrays
```java
// Traditional nested for loop
for (int i = 0; i < mat.length; i++) {
    for (int j = 0; j < mat[i].length; j++) {
        System.out.println(mat[i][j]);
    }
}

// Enhanced for loop
for (int[] row : mat) {
    for (int num : row) {
        System.out.println(num);
    }
}
```

---

## Methods

### Method Declaration
- A method must be declared within a class
- `static` keyword indicates the method belongs to the class and not to an object
- Defined with the return type followed by the method name, followed by parentheses `()`
- `void` keyword indicates that the method should not return a value

### Method Syntax
```java
// Method with no return value
static void methodName(String name, int age) {
    // code block
}

// Method with return value
static int methodName() {
    return 6;
}
```

### Method Call
- Call method: Name followed by parentheses `()` and a semicolon `;`
- Parameters: Parameter type followed by name inside parentheses `()`
- Calling values for parameters are called **arguments**

### Rules
- The method call must have the same number of arguments as there are parameters
- The arguments must be passed in the same order

### Return Statement
- Use the `return` keyword for returning values
```java
static int add(int a, int b) {
    return a + b;
}
```

---

## Collections Framework

All collections are part of the `java.util` package. Use the `import` keyword followed by a semicolon.

The Java Collections Framework provides:
- **Interfaces:** List, Set, Map
- **Classes:** ArrayList, HashSet, HashMap, etc.

### When to Use
- **List:** When you care about order, may have duplicates, and want to access elements by index
- **Set:** When you need to store unique values only
- **Map:** When you need to store pairs of keys and values

### Important Notes
- When instantiating objects, use the `new` keyword followed by the class name and parentheses
- Wrapper classes provide a way to use primitive data types as objects.
- You must specify equivalent wrapper classes: `Integer` for `int`, `Boolean` for `boolean`, `Character` for `char`, `Double` for `double`

---

### ArrayList

#### Declaration
```java
import java.util.ArrayList;

ArrayList<String> cars = new ArrayList<String>();
// or
var cars = new ArrayList<String>();
```

#### Common Methods
```java
cars.add("Volvo");           // Add element
cars.get(index);             // Access element
cars.set(index, "BMW");      // Update element
cars.remove(index);          // Remove element
cars.size();                 // Get size
```

#### Sorting
```java
import java.util.Collections;

Collections.sort(cars);                              // Ascending (based on value, ASCII)
Collections.sort(cars, Collections.reverseOrder());  // Descending
Collections.reverse(cars);                           // Reverse order
```

#### Iteration
- Can be looped through using enhanced for loop or traditional for loop with index

---

### LinkedList

#### Declaration
```java
var ll = new LinkedList<String>();
```

#### Common Methods
```java
ll.addFirst(element);    // Adds an element to the beginning of the list
ll.addLast(element);     // Adds an element to the end of the list
ll.removeFirst();        // Removes an element from the beginning of the list
ll.removeLast();         // Removes an element from the end of the list
ll.getFirst();          // Gets the element at the beginning of the list
ll.getLast();            // Gets the element at the end of the list
```

---

### HashSet

#### Declaration
```java
var hashSet = new HashSet<String>();
```

#### Common Methods
```java
hashSet.add(element);        // Add element
hashSet.remove(element);     // Remove element
hashSet.contains(element);   // Check if element exists
hashSet.size();              // Get size
hashSet.clear();             // Clear all elements
```

#### Iteration
```java
for (String item : hashSet) {
    System.out.println(item);
}
```

**Note:** For maintaining insertion order, use `LinkedHashSet` instead of `HashSet`.

---

### HashMap

#### Declaration
```java
var map = new HashMap<String, Integer>();
```

#### Common Methods
```java
map.put(key, value);         // Add key-value pair
map.get(key);                // Get value by key
map.size();                  // Get size
map.containsKey(key);        // Check if key exists
map.remove(key);             // Remove key-value pair
map.keySet();                // Returns set of keys (for iterating)
map.values();                // Returns collection of values (for iterating)
```

---

### Iterator

**Important:** Trying to remove items using a for loop or for-each loop would not work correctly because the collection is changing size. Use `Iterator` instead.

#### Usage
```java
import java.util.Iterator;

Iterator<Integer> it = collection.iterator();
while (it.hasNext()) {
    Integer i = it.next();
    // Now points to first element
    // Safe to remove: it.remove();
}
```
## Annotations
- Special notes that start with the @ symbol.
- Just gives extra information to the compiler.
- Built in annotations: @Override, Indicates that a method overrides a method in a superclass. Helps the compiler check that a method really overrides a method from a superclass.
```java
@Override
  void func() {
    //
  }
```
---

## Quick Reference Summary

### File Naming
- Class name must match filename
- File extension: `.java`
- Class name starts with uppercase

### Common Patterns
```java
// Class structure
public class MyClass {
    public static void main(String[] args) {
        // Your code here
    }
}

// Variable declaration
int x = 5;
String name = "Java";

// Method declaration
static void myMethod() {
    // code
}

// Array declaration
int[] arr = {1, 2, 3};

// ArrayList declaration
ArrayList<String> list = new ArrayList<>();
```

---

array literals {} can only be used at declaration time, not directly as arguments.
new Dog("1", 1, new int[]{1, 2});

## Packages and Imports
- Packages group related classes and avoid name conflicts (think folders).
- Java API is organized into packages/classes.
- Import usage:
  - `import package.name.Class;` (single class)
  - `import package.name.*;` (entire package)
- Create a package with `package mypack;` (package names in lowercase to avoid class-name conflicts).

## Input with Scanner
- Use `Scanner` Class from `java.util` package:
  - `import java.util.Scanner;`
  - `Scanner input = new Scanner(System.in);`
  - `String name = input.nextLine();`
- Common methods:
  - `nextLine()` reads `String`
  - `nextInt()` reads `int`
  - `nextBoolean()` reads `boolean`
  - `nextDouble()` reads `double`
  - `nextLong()` reads `long`
- Invalid input causes `InputMismatchException`.


## Variable Scope
- Block scope: variables inside `if`, `for`, `while` are accessible only in that block.
- Method scope: variables declared directly in a method are usable anywhere in that method.
- Class scope (fields): variables declared in a class but outside methods are accessible to all methods in that class.

