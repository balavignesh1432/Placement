## Creational Patterns
### 1. Builder
Lets you construct complex objects step-by-step, separating the construction logic from the object representation (Product).

**Used:**
- Avoid telescoping constructors (constructors with multiple parameters).
- Object requires many optional fields.

**Components:**
- **Builder:** Defines methods to set up the product.
- Typically returns this from each method to support chaining.

- **ConcreteBuilder:** Implements the Builder interface 
- Implements the build() method that returns the final product instance.

- **Product:** The final object being constructed.

```java
class Product{
    private String field1;
    private String field2; // optional
    Product(String field1, String field2){
        this.field1 = field1;
        this.field2 = field2;
    }
}

interface Builder {
    Builder buildField1(String);
    Builder buildField2(String);
    Product build();
}

class ConcreteBuilder implements Builder{
    private String field1; 
    private String field1 = "DefaultRam"; // Optional
    public Builder buildField1(String field1) {
        this.field1 = field1;
        return this;
    }
    public Builder buildField2(String field2) {
        this.field2 = field2;
        return this;
    }
    public Product build(){
        return new Product(field1, field2);
    }
}
// Client
Product Obj = new ConcreteBuilder().buildField1("field1").build();
```

### 2. Factory Method
Defines an interface for creating objects but lets subclasses decide which object to instantiate.
New product types can be introduced without altering client code. (Loose Coupling)

**Use:**
- Object creation logic is complex, and conditional.
- Type of object to be created isn't known until runtime.

**Components:**
- **Product:** Interface for objects created by the factory.
- **Concrete Product:** The actual object that implements the product interface.
- **Creator:** Declares the factory method.
- **Concrete Creator:** Implements the factory method to create specific products.

```java
interface Product{
    public void use();
}

class ConcreteProductA implements Product{
    public void use(){
        System.out.println("Using Product Type A");
    }
}

class ConcreteProductB implements Product{
    public void use(){
        System.out.println("Using Product Type B");
    }
}

abstract class Creator{
    Product create();
}

class ConcreteCreatorA extends Creator{
    public Product create(){
        return new ConcreteProductA();
    }
}

class ConcreteCreatorB extends Creator{
    public Product create(){
        return new ConcreteProductB();
    }
}

//client
Product productA = new ConcreteCreatorA().create();
productA.use();
Product productB = new ConcreteCreatorB().create();
productB.use();
```

### 3. Singleton
Guarantees a class has only one instance and provides a global point of access to it.
Lazy or Eager Initialization: An Instance can be created at class load time (eager) or when first needed (lazy).

**Components:**
- **Private Constructor:** This ensures that the class has control over its instantiation process.
- **Static Instance member**
- **Static Method that returns the instance.**

**Eager Initialization:**
```java
class Singleton{
    private static final Singleton instance = new Singleton(); // Final makes it thread safe
    private Singleon(){}
    public static Singleton getInstance(){
        return instance;
    }
}
```

**Lazy Initialization:** Only use resource when needed.
```java
class Singleton{
    private static Singleton instance;
    private Singleton(){}
    public static Singleton getInstance(){
        if(instance == null){
            instance = new Singleton();
        }
        return instance;
    }
}
```
**Bill Pugh Singleton** (Using nested class with final attribute): Thread Safe Lazy Initialization
```java
class Singleton{
    private static class SingletonHelper{
        private static final Singleton Instance = new Singleton();
    }
    public static Singleton getInstance(){
        return SingletonHelper.Instance;
    }
}
```

## Behavioural Patterns

### 1. Observer: 
Defines a one-to-many dependency between objects so that when one object (the subject) changes its state, all its dependents (observers) are automatically notified and updated. 
Decoupling the subject and its observers, allowing them to interact through a common interface. 
Observers can be added or removed at runtime, and the subject doesn’t need to know who they are.

**Components:**
- **Subject:** Maintains a list of observers, provides methods to add/remove them, notify all of change.
- **ConcreteSubject:** A specific subject that holds actual data. On state change, it notifies registered observers.
- **Observer:** Defines an interface with an update() method to ensure all observers receive updates
- **ConcreteObserver:** Implements the observer interface and reacts to subject updates 

```java
interface Subject{
    public void addObserver();
    public void removeObserver(Observer ob);
    public void notifyObservers(Observer ob);
}

class ConcreteSubject implements Subject{
    private List<Observer> observers = new ArrayList<Observer>();
    private String subject;
    public void addObserver(Observer ob){
        observers.add(ob);
    }
    public void removeObserver(Observer ob){
        observers.remove(ob);
    }
    public void notifyObservers(){
        for(Observer ob: observers){
            ob.update(subject);
        }
    }
    public void setSubject(String s){
        this.subject = s;
        notifyObservers();
    }
}

interface Observer{
    public void update(String subject);
}

class concreteObserver implements Observer{
    public void update(String subject){
        // Perform Operations on subject State Change
    }
}

//client
ConcreteSubject cs = new ConcreteSubject();
ConcreteObserver co1 = new ConcreteObserver();
ConcreteObserver co2 = new ConcreteObserver();
cs.addObserver(co1);
cs.addObserver(co2);
cs.setSubject("State changed!");
```

### 2. Strategy
Define a family of algorithms or behaviors, put each of them in a separate class, and make them interchangeable at runtime. Dynamically change the behavior of a class without modifying its code.

**Components:**
- **Strategy:** Interface specifies a set of methods that all concrete strategies must implement.
- **Concrete Strategy:** Implementations of the Strategy Interface. Each concrete strategy provides a specific behavior for performing the task.
- **Context:** Maintains a reference to a strategy object and calls its methods to perform the task.
- The context doesn’t know or care which specific strategy is being used.

```java
interface Strategy{
    public void perform();
}

class ConcreteStrategyA implements Strategy{
    public void perform(){
        System.out.println("Strategy A");
    }
}

class ConcreteStrategyB implements Strategy{
    public void perform(){
        System.out.println("Strategy B");
    }
}

class Context{
    private Strategy context;
    public void setContext(Strategy s){
        this.context = s;
    }
    public void performTask(){
        context.perform();
    }
}

//client
Context c = new Context();
c.setContext(new ConcreteStrategyA());
c.performTask();
c.setContext(new ConcreteStrategyB());
c.performTask();
```

### 3. State Method
Enables an object to change its behavior when its internal state changes. 
Encapsulates each state into its own class, and letting the context object delegate behavior to the current state object.

**Use:**
- The object’s behavior depends on current context, and that context changes over time.
- Avoid large if-else or switch statements that check for every possible state.

**Components:**
- **Context:** Maintains a reference to the current state Object. Delegates calls to the current state.
- **State:** Defines common methods for all states, allowing Context to work with them without knowing concrete types.
- **Concrete States:** Implement the State interface. Define state-specific behavior for each action.

```java
interface State{
    public void handle();  
}

class ConcreteStateA implements State{
    public void handle(){
        // Perform Operation for State A
    }
}

class ConcreteStateB implements State{
    public void handle(){
        // Perform Operation for State B
    }
}

class Context{
    private State state;
    public Context(){
        this.state = new ConcreteStateA();  // Initial State
    }
    public void setState(State state){
        this.state = state;
    }
    public void handle(){
        state.handle();
    }
}

// Client
Context c = new Context();
c.handle();
c.setState(new ConcreteStateB());
c.handle();
```

## Structural Patterns

### 1. Decorator
Extend object behavior without altering existing code. Dynamically add behavior to individual objects without changing other objects.

**Use:**
- Extend the functionality of a class without subclassing it.
- You need to compose behaviors at runtime, in various combinations.

**Components:**
- **Component :** Declares the common interface for concrete components and decorators.
- **ConcreteComponent:** The base object that can be dynamically decorated.
- **Decorator:** Implements the component interface and stores a reference to the component to be decorated.
- **ConcreteDecorators:** Extend the decorator to add new functionality.

```java
interface Component{
    void execute();
}

class ConcreteComponent implements Component{
    public void execute(){
        // Perform Execution
    }
}

abstract class Decorator implements Component{
    protected Component component;  // Make it protected to access from ConcreteDecorator
    public Decorator(Component component){
        this.component = component;
    }
    public void execute(){
        component.execute();
    }
}

class ConcreteDecoratorA extends Decorator{
    public ConcreteDecoratorA(Component component){
        super(component);       // Call constructor Decorator and initialise reference
    }
    public void execute(){
        // Add behaviour
        component.execute();
        // Add behaviour
    }
}
class ConcreteDecoratorB extends Decorator{
    public ConcreteDecoratorB(Component component){
        super(component);       // Call constructor Decorator and initialise reference
    }
    public void execute(){
        // Add behaviour
        component.execute();
        // Add behaviour
    }
}

//client
Component cc = new ConcreteComponent();
Component cd1 = new ConcreteDecoratorA(cc);     //Wrapping with ConcreteDecorator
cd1.execute();
Component cd2 = new ConcreteDecoratorB(cd1);    //Chaining with anotherDecorator
cd2.execute();
```

### 2. Facade
Provides a unified, simplified interface to a complex subsystem making it easier for clients to interact with multiple components without getting overwhelmed by their intricacies.

**Use:**
- The client doesn’t need to know how those parts (API and Database) work internally.
- Reduce the coupling between clients and complex systems.

**Components:**
- **Facade:** Knows which subsystem classes to use and in what order. Delegates requests to appropriate subsystem methods without exposing internal details to the client.
- **Subsystem Classes:** Provides the actual business logic. Do not know about the facade. Can still be used independently if needed.
- Usually facade contains the references of the objects of subSystem classes, initialised in the constructor by instantiating them.

```java
class Facade{
    private SubsystemA sA;
    private SubsystemB sB;
    public Facade() {
        this.sA = new SubsystemA();
        this.sB = new SubsystemB();
    }
    void operation(){
        sA.operationA();
        sB.operationB();
    }
}

class SubsystemA {
    void operationA() {
        System.out.println("SubsystemA operation");
    }   
}

class SubsystemB {
    void operationB() {
        System.out.println("SubsystemB operation");
    }
}

//client
Facade fac = new Facade();
fac.operation();
```