# Single Responsibility Principle (SRP)

## Definition

**A class should have only one reason to change.**

This means each class should focus on a single responsibility.

## Bad Example (Violates SRP)
```python
class Employee:
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        return self.salary * 1.2  # Example calculation

    def generate_report(self):
        return f"Employee: {self.name}, Salary: {self.salary}"
```

## What’s Wrong?

The `Employee` class has multiple responsibilities:

1. **Stores employee data**.

2. **Calculates salary**.

3. **Generates reports**.

When any of these responsibilities change, the class must be modified, which violates the SRP. For example:

- If we change the way the salary is calculated, we modify the `Employee` class.

- If we need to change how reports are generated, we again modify the same class.

This leads to tightly coupled code, making it more difficult to maintain and test.


## Good Example (Follows SRP)
```python
class Employee:
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary

class SalaryCalculator:
    def calculate_salary(self, employee: Employee):
        return employee.salary * 1.2  # Example calculation

class ReportGenerator:
    def generate_report(self, employee: Employee):
        return f"Employee: {employee.name}, Salary: {employee.salary}"

```
## Why is this better?

- **Single Responsibility**: Each class now has a single responsibility:

  - `Employee` class only stores employee data.

  - `SalaryCalculator` handles salary calculations.

  - `ReportGenerator` manages report generation.

- **Maintainability**: If the salary calculation rules change, we only need to modify the `SalaryCalculator` class, not the `Employee` class.

- **Scalability**: Adding new responsibilities (like different types of reports or more complex salary calculations) doesn’t affect the existing classes, which keeps the codebase flexible.

- **Testability**: Since the responsibilities are divided across classes, we can test each class independently, ensuring that the system behaves as expected without unwanted side effects.

## Key Takeaways

- **SRP** helps prevent classes from becoming too large and complex.

- It improves **modularity**, making each part of your system easier to understand, test, and modify.

- SRP also leads to a more **flexible and extensible** codebase, as changes to one responsibility won't cause ripple effects in other areas.

### Additional Examples:

1. **Bad Example:**
   A `User` class that handles both user data and sending notification emails:

```python
class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def send_email(self, subject: str, message: str):
        # Code to send email
        pass
```

- **What's wrong?**: This class is responsible for both storing user data and handling email sending, which violates SRP.

- **Good Example**: Separate the concerns into different classes:

```python
class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

class EmailSender:
    def send_email(self, user: User, subject: str, message: str):
        # Code to send email to user
        pass
```

- **Why is this better?**: The `User` class only stores user data, and the `EmailSender` class handles the email functionality. This separation of concerns adheres to SRP, making both classes easier to maintain.

2. **Bad Example**: A `Book` class that handles both book data and printing reports:

```python
class Book:
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages

    def print_report(self):
        print(f"Book: {self.title} by {self.author}")
        print(f"Pages: {self.pages}")
```

- **Good Example**: Separate the printing logic into a different class:

```python
class Book:
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages

class ReportPrinter:
    def print_report(self, book: Book):
        print(f"Book: {book.title} by {book.author}")
        print(f"Pages: {book.pages}")
```

- **Why is this better?**: The `Book` class now only contains book-related data, and the `ReportPrinter` class is responsible for printing the report. This makes each class focused on a single responsibility.
