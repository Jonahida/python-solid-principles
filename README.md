# SOLID Principles in Python

This repository provides Python implementations of the **SOLID** principles, a set of five object-oriented design principles intended to make software systems easier to maintain, extend, and understand.

The principles are as follows:

1. **Single Responsibility Principle (SRP)**
2. **Open/Closed Principle (OCP)**
3. **Liskov Substitution Principle (LSP)**
4. **Interface Segregation Principle (ISP)**
5. **Dependency Inversion Principle (DIP)**

Each principle is demonstrated with both **bad** and **good** code examples, showing how adhering to SOLID can lead to more maintainable and flexible code.

---

## Running the Project

### 1. Clone the repository:

```bash
git clone https://github.com/Jonahida/python-solid-principles
cd solid-principles-python
```

### 2. Run the interactive example viewer:
```bash
python main.py
```

This will allow you to explore and compare bad and good implementations for each SOLID principle.

## The SOLID Principles Explained

### 1. Single Responsibility Principle (SRP)

*"A class should have one, and only one, reason to change."*

The SRP suggests that a class should only have one job or responsibility. If a class has more than one responsibility, those responsibilities become coupled, which can lead to challenges when trying to change or extend the functionality.

**Example**:

- **Bad**: A `User` class handling both user data and file handling operations.

- **Good**: Separate classes for managing user data and handling file I/O operations.

---

### 2. Open/Closed Principle (OCP)

*"Software entities (classes, modules, functions, etc.) should be open for extension but closed for modification."*

This principle promotes the idea of extending an existing class or module’s behavior without modifying its code. Instead of changing existing code, we add new functionality by extending or composing new components.

**Example**:

- **Bad**: Modifying a class each time new functionality is needed.

- **Good**: Using inheritance, interfaces, or composition to add new behaviors without altering existing code.

---

### 3. Liskov Substitution Principle (LSP)

*"Objects of a superclass should be replaceable with objects of a subclass without affecting the correctness of the program."*

The LSP ensures that subclasses are extensions of the parent class that behave as expected. Subtypes should be able to replace their base types without causing issues.


**Example**:

- **Bad**: A `Rectangle` class being subclassed into a `Square` class that violates the expected behavior.

- **Good**: `Square` class should not extend `Rectangle`; instead, both should implement a shared interface.

---

### 4. Interface Segregation Principle (ISP)

*"Clients should not be forced to depend on interfaces they do not use."*

The ISP advises breaking down large, general-purpose interfaces into smaller, more specific ones. Clients should only implement interfaces that are relevant to them.


**Example**:

- **Bad**: A `Worker` interface requiring `work()` and `eat()` methods, where `Robot` doesn't need `eat()`.

- **Good**: Separate interfaces for `Workable` and `Eatable`, so clients only implement what they need.

---

### 5. Dependency Inversion Principle (DIP)

*"High-level modules should not depend on low-level modules. Both should depend on abstractions."*

This principle suggests that both high-level and low-level modules should rely on abstractions (e.g., interfaces), not concrete implementations, promoting flexibility and decoupling in the system.


**Example**:

- **Bad**: A `Project` class directly depending on `BackendDeveloper` and `FrontendDeveloper`.

- **Good**: Using an abstraction like `Developer` so that `Project` can work with any type of developer.

---

## The `main.py` Script

The `main.py` script allows you to interactively explore and compare bad and good examples of each SOLID principle. It includes the following features:

1. **Interactive Menu**: The script presents a menu with the following options:

- 1. Single Responsibility Principle (SRP)

- 2. Open/Closed Principle (OCP)

- 3. Liskov Substitution Principle (LSP)

- 4. Interface Segregation Principle (ISP)

- 5. Dependency Inversion Principle (DIP)

- 6. Exit

2. **Code Examples**: When a principle is selected, the script will display:

- **Bad Example**: Code that violates the SOLID principle.

- **Good Example**: Code that follows the SOLID principle.

3. **Simple Navigation**: Choose a principle from the menu to see its examples, and exit the program when you're done.

## Contributing

If you would like to contribute to the project, feel free to submit a pull request with improvements or bug fixes. Please ensure that your code adheres to the SOLID principles and includes clear explanations in the `README.md`.

## License

This project is licensed under the MIT License.