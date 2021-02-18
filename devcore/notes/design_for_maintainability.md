# Notes for Design for Maintainability

## Functional and Nonfuntional Requirements

When designing software start with collecting functional and nonfunctional requirements.

- ### Functional requirements:

    - Measured in `yes` or `no` terms and normally include words like `can` and `shall`
    
    - Describes the functionalities of a system, such as a business process, data manipulation, user interation, media processing, calcualtion, or any other action that the system can perform.

    - Normally read by a general audience. Not so technical.

    - Project stakeholder help define these requirements.

    - Derived from `user stories` which is the user's interaction with the software.

    - They also focus on `use cases` are cause and effect.
        
        - Which is what happens after a user performs an action on a software.
        
        - Does te software save to a text file or interact with a database.

    - When writing functional requirements:

        - Be concise

        - Avoid using vague terms

        - Clearly define who can perform actions and access data
        
        - Each function should have single functionality

- #### Examples:

    > User can access, create, edit, delete, save, and restore documents in aweb GUI.<br>
    Administrator can create and delete users. <br>
    Documents can be sent via GUI to other users.

- ### Nonfunctional requirements:

    - These are quality attributes also known as `technical requirements`

    - How a system `should` or `must` perform in an interval or range

    - When writing nonfunctional be sure to use specific times and requirements

    - Often defines constraints on a system

    - Written very technical

    - Requirements are implicit and assumed. Like a fast load webpage.

    - Defined by software developers, the team, designers, and architects.

    - In the software development process these are not all taken into consideration.

    - Too many nonfuctional requirements can drag the development process out forever and make your application complicated.

    - Too few can make your application slow, not available, and insecure. 

- #### Examples

    > The system must support at least 10,000 concurrent users. <br>
      Availability - The system should be available at least 99 percent of the time.<br>
      Web GUI should take less than two seconds to load.<br>
      Users are required to register before they can use the system.<br>
      Passwords must not show anywhere in the logs or the GUI.<br>
      The GUI system can be translated into all other languages.


## Nonfunctional Requirements and Application Quality

As a software developer you are responsible for the quality of your appplication. Clearly defining the nonfuctional requirements is a must. 

It is your job as a software developer to know:

- What the application does

- Who will be using your application?

- What is it's lifecycle?

- How many user's use your application?

- Will the number remain the same or will it grow? 

- How many connections can your application support?


Having clearly defined nonfunctional requirements will help:

- Increase code quality

- Better app speed and performance

- Fewer bugs and errors

- Higher uptime

- Improved security

- Reduced maintenance cost

- Better user experience

Ignoring these can be costly and lead to a huge amount of `technical debt`. 

Here are some examples of technical debt:

- `Lack of testing` - Higher number of bugs in your code.

- `Weak security` - During development security can be a constraint and is often not added or upgrade until it's time for production deployment.

- `Improper environment` - These assumptions can lead to improper functionality of code once in production.

- `Lack of modularity` - Making even the smallest of changes to the code can break the application

 
 ## Maintainability Through Design

At some poit you will have to change something in your code. Designing your application to be maintainable in the beginning is the most important thing you can do for your future self. 

Here are some best practices to make your code more maintainable:

- `Modular design` - Your code should be resusable and each component should function independently

- `Naming conventions` - Adhering to naming conventions throughout your project will help you and your team. Python uses [PEP 8](https://www.python.org/dev/peps/pep-0008/#naming-conventions)

- `Software configuration management` - Use some sort of version control to track your changes and to maintain your code.

- `Coding standards` - Follow well defined coding standards throughout your project and team. Python uses [PEP 8](https://www.python.org/dev/peps/pep-0008/#naming-conventions)

- `Common toolset` - Structure your team so that everyone uses the same IDE, OS and tools. 

- `Object-oriented design` - Goes with modular design. Resuable and extensible classes makes your code easier to make changes and to maintain. 


### SOLID Principle

An acronym that defines five software design principles:

1. `Single responsibility principle` - Each class, function, module, method, and service should have only a single resposibility or one job.

2. `Open-closed principle` - Components (classes, methods, etc.) should be open for extension but closed for modification.

3. `Liskov's substitution principle` - Derived types must be completely substitutable for their base types. The child class should never change the characteristics of the parent class.

4. `Interface segregation principle` - Clients should not be forced to depend upon the interfaces they do not use. 

5. `Dependency inversion principle` - Program to an interface, not to a implementation.

These principles helps developers by:

- Making it easier for developers to maintain and extend software.

- Reducing the amount of technical debt

- Making the code flexible

### 12 Factory App methodology

Find more infor here: [12 Factor App](https://12factor.net/)

#### This example breaks the single responsibility principle

This class gets the interface and command args then updates a device. This breaks the single responsibility principle of the class. 

```python
class NetworkInterface:
    def __init__(self, interface, command):
        self.interface = interface
        self.command = command

    def get_interface(self, interface):
        self.interface = interface

    def get_command(self, command):
        self.command = command

    def update_interface(self):
        Device.update(self.interface, self.command)

```

A better design would be:

```python
class NetworkInterface:
    def __init__(self, interface, command):
        self.interface = interface
        self.command = command

class Device:
    def update_interface(self, network):
        NetworkDevice.update(network.interface, network.command)
```

An even better deign that would conform to the open-closed principle:

```python
class NetworkInterface:
    def __init__(self, interface, command):
        self.interface = interface
        self.command = command

class Device(NetworkInterface):
    def __init__(self):
        super().__init__(self)
    def update_interface(self):
        NetworkDevice.update(self.interface, self.command)
```

## Maintainability Through Implementation

The implementation phase is the phase where the application gets built. In this phase most of the major decisions should have been made. But its not uncommon to have to need to revisit any requirements that may need to be modified. 