## Characteristics of Software
- **Functionality:** The things that software is intended to do or its core purpose.
- **Usability:** The extent to which the software can be used with ease.
- **Reliability:** Ability to perform what it was designed to do accurately and consistently over time.
- **Flexibility:** How simple it is to improve and modify the software.
- **Portability:** Ease with which the software can be transferred from one environment or platform to another.
- **Integrity:** How well the software maintains the accuracy and consistency of data.
- **Efficiency:** Ability of the software to use system resources efficiently.

## Categories of Software
- **System Software:** Helps manage the hardware of your computer. Example: Operating System.
- **Application Software:** Programs we use on a computer to perform specific tasks. Example: Word.
- **Web Applications Software:** Programs accessed via a web browser. Example: Gmail.
- **Embedded Software:** Software built into devices to help them function properly. Example: Factory machinery.

## Software Development Life Cycle (SDLC)
Six phases:
1) **Planning and Requirement Analysis:** Set objectives/goals and define the scope of the project or software.  
2) **Defining Requirements:** Identify what the software needs to do (functional) and how well it should do it (non-functional).  
3) **Design:** Decide on the overall structure/architecture, including HLD and LLD.  
4) **Development:** Turn the design into a working product by writing the actual code.  
5) **Testing and Integration:** Test the software for bugs and ensure everything works together smoothly.  
6) **Deployment and Maintenance:** Deploy for production use and maintain to fix issues.

**Baseline:** After all activities associated with a particular phase are accomplished, the phase output acts as a baseline for the next phase.

## Software Requirement Specification (SRS) Format
Complete specification and description of requirements of the software that need to be fulfilled for successful development of the software system.

- **Functional requirements:** Mandatory, specified by the user.
- **Non-functional requirements:** Not mandatory, specified by technical individuals.

#### Computer-Aided Software Engineering (CASE): 
- Set of automated software application programs, which are used to support SDLC activities. It is a software package that helps with the design and deployment.

## Coupling
- Degree of interdependence between software modules; shows relative independence between modules.
- High coupling means modules are closely connected, and changes in one module affect other modules.
- Low coupling means modules are independent, and changes in one module have little impact on other modules (ideal).

## Cohesion
- Degree to which elements in a module work together to fulfill a single, well-defined purpose; shows the relative functional strength of the module.
- High cohesion: elements are closely related and focused on a single purpose (ideal).
- Low cohesion: elements are loosely related and serve multiple purposes.


## SOLID Principles
Enhance software design, making code more maintainable and scalable.

1) **Single Responsibility Principle:** A class should have only one reason to change. Classes should have a single responsibility (not a single function or method). Achieved by breaking fat classes into smaller classes.
2) **Open/Closed Principle:** Software entities (classes, modules, functions, etc.) should be open for extension but closed for modification. Behavior can be extended as new requirements come in, but the working code of the entity should not be changed. Achieved using abstraction; for extension, create new implementations.
3) **Liskov Substitution Principle:** Derived or child classes must be substitutable for their base or parent classes. Any child should be usable in place of its parent without unexpected behavior. Client code should not need to care which specific subtype it is dealing with. Subclasses should not arbitrarily tighten or loosen the behavior defined by the base class.
4) **Interface Segregation Principle:** Do not force any client to implement an interface that is irrelevant to them. Clients should not be forced to implement methods they do not use. Achieved by breaking (segregating) fat interfaces into smaller interfaces.
5) **Dependency Inversion Principle:** High-level modules should not depend on low-level modules; both should depend on abstractions (interfaces). Abstractions should not depend on details. Details (concrete implementations) should depend on abstractions. High-level modules define what they need (the contract/interface), and low-level modules provide the how (implementation). Achieved using abstraction for class implementations.


## Modularization
Breaking down a program's functionality into separate, independent modules, each of which includes just the information needed to carry out one part of the intended capability.

## SDLC Models
- **Waterfall:** Development process is linear, and each step is finished one by one. Requirements are well-defined and unchangeable. Suitable for small to medium projects (example: safety-critical systems).
- **Rapid Application Development (RAD):** Incremental process focusing on delivering working software in shorter timelines. Used when the requirements are fully understood and component-based construction is adopted. Components go through phases in parallel in a short time frame.
- **Spiral:** Combination of Waterfall and iterative process. Development begins with a limited set of requirements and progresses through each development phase. Functionality is added for increasing requirements in ever-increasing spirals. Main principle is risk evaluation and handling at each phase. Used for projects prone to risks that are difficult to anticipate at the beginning.
- **Agile:** Combination of iterative and incremental processes. Development happens in short bursts/sprints with constant feedback from the customer. Allows for changes at any stage, making it responsive to evolving needs.
- **Prototype:** Working model with limited functionality. Users can review developer proposals and try them out before they are implemented.
- **POC (Proof of Concept):** Used by organizations to validate an idea or concept's practicality. This stage exists prior to the start of the software development process.

## Framework
A set of tools that allows developing software by providing information on how to build it at an abstract level, rather than giving exact details.



## Rayleigh Model
Used to check software reliability.

## Risk vs. Uncertainty
- Risk can be measured; uncertainty cannot be measured.
- After making efforts, risk can be converted into certainty.
- Uncertainty cannot be converted into certainty.

## Software Deterioration
Over time, multiple changes can cause different parts of the software to interact in unexpected ways, making it harder to maintain.

## QA vs. QC
- **Quality Assurance (QA):** Are we following the right process to build quality software? Process-oriented and applied throughout the SDLC. Technique of managing quality. Aims to prevent defects by ensuring proper standards, methods, and procedures are followed. Preventive measure. Example: verification.
- **Quality Control (QC):** Is the product free from defects? Product-oriented and performed after development activities. Identifies defects in the actual software. Mainly the responsibility of the testing team. Corrective measure. Technique to verify quality. Example: validation.

## Verification vs. Validation
- **Verification:** Are we building the product right? Checks whether the software conforms to specifications and design documents. Deals with functionality. Happens during development. Mostly done without executing the code. Prevents defects early. Examples: requirement reviews, design reviews, code reviews.
- **Validation:** Are we building the right product? Checks whether the final product meets user needs and expectations. Deals with quality. Happens after or near completion. Requires executing the software. Examples: unit testing, integration testing, UAT testing.

## Testing Types
- **Unit Testing:** Checks individual units to ensure each piece works properly on its own.
- **Integration Testing:** Checks how well different parts of the software work together.
- **Black Box/Closed Box Testing:** Focuses on validating functionality based on specifications or requirements (high level). Internal workings/implementations are hidden from the tester's view.
- **White Box/Glass Box Testing:** Analyzes the internal structure/implementation (low level).
- **Gray Box Testing:** Combines Black Box and White Box approaches, incorporating input from both developers and testers.
- **Regression Testing:** Ensures that new code changes do not have side effects on existing functions. Selected existing test cases are rerun to ensure that existing functions work correctly.
- **Alpha Testing:** Performed by testers; involves both Black Box and White Box testing.
- **Beta Testing:** Performed by clients; usually involves Black Box testing.


## Clean Room Software Engineering
QA is performed in each and every phase of software development, delivering an efficient and good-quality software product.

## Feasibility Study
Analyzes whether a proposed software project is practical (operational, technical, and financial viability). Decreases the chance of project failure, saving time and money.

## Software Reverse Engineering
Recovering the design, requirement specifications, and functions of a product from an analysis of its code. Facilitates maintenance work by improving system understandability and producing necessary documents for a legacy system.

## Constructive Cost Model (COCOMO)
Software cost estimation model that helps predict the effort, cost, and schedule required for a software development project.


## Data Flow Diagram (DFD)
- Graphical tool used to represent how data moves through a system. Shows data inputs, outputs, data stores, and the processes that transform the data.
- **Level 0 DFD (Context Diagram):** Represents the entire system as one single process, showing its interaction with external entities.
- **Level 1 DFD:** Breaks the Level 0 process into major subprocesses; shows internal data flows and data stores.
- **Level 2 and beyond:** Further decomposes Level 1 subprocesses for a detailed view of specific functional areas.
- **Logical DFD:** Focuses on the processes and illustrates how data flows in the system.
- **Physical DFD:** Shows how the data flow is implemented in the system (data storage and transmission).
- **Black Hole:** A processing step may have input flows but no output flows.
---
