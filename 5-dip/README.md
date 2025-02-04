# Dependency Inversion Principle (DIP)

## Definition

*"High-level modules should not depend on low-level modules. Both should depend on abstractions."*

*"Abstractions should not depend on details. Details should depend on abstractions."*

## Bad Example (Violates DIP)
```python
class BackendDeveloper:
    def develop(self):
        return "Writing backend code..."

class FrontendDeveloper:
    def develop(self):
        return "Writing frontend code..."

class Project:
    def __init__(self):
        self.backend = BackendDeveloper()
        self.frontend = FrontendDeveloper()

    def develop(self):
        return f"{self.backend.develop()} {self.frontend.develop()}"
```
## What's Wrong?


- **Tight coupling**: The `Project` class directly depends on concrete implementations of `BackendDeveloper` and `FrontendDeveloper`. This makes it difficult to extend the `Project` class when adding new types of developers, such as `MobileDeveloper`.

- If we want to add a new developer type, we would need to **modify** the `Project` class, violating the **Open/Closed Principle (OCP)** as well.

- This code is difficult to maintain, extend, and test because each change to a developer type requires changes to the `Project` class.


## Good Example (Follows DIP)
```python
from abc import ABC, abstractmethod
from typing import List

class Developer(ABC):
    @abstractmethod
    def develop(self):
        pass

class BackendDeveloper(Developer):
    def develop(self):
        return "Writing backend code..."

class FrontendDeveloper(Developer):
    def develop(self):
        return "Writing frontend code..."

class Project:
    def __init__(self, developers: List[Developer]):
        self.developers = developers

    def develop(self):
        return " ".join([dev.develop() for dev in self.developers])

# Example usage
team = [BackendDeveloper(), FrontendDeveloper()]
project = Project(team)
print(project.develop())  # Output: Writing backend code... Writing frontend code...
```

## Why is this better(Follows ISP)

- **Abstractions over concrete implementations**: The `Project` class now depends on the `Developer` abstraction (an interface or base class), not on the concrete `BackendDeveloper` or `FrontendDeveloper`.

- **Easier to extend**: To add a new developer type (e.g., `MobileDeveloper`), we don't need to modify the `Project` class. We simply create a new class that implements the `Developer` interface. The `Project` class will work seamlessly with any new type of `Developer` that adheres to the `Developer` interface.

- **Flexibility and maintainability**: The `Project` class is now more flexible and easier to maintain because it is decoupled from the low-level details (specific developer types) and depends only on the higher-level abstraction (the `Developer` interface).

- **Testing**: It's easier to mock or stub dependencies during testing because the `Project` class depends on an abstraction rather than a concrete implementation.

## Key Takeaways

- The **Dependency Inversion Principle (DIP)** promotes the use of abstractions to decouple high-level modules from low-level modules.

- By depending on abstractions (interfaces or abstract classes) instead of concrete implementations, we make our code more flexible, extensible, and maintainable.

- **High-level modules** should not depend on **low-level modules**. Both should depend on **abstractions**.

- Adhering to DIP helps reduce the impact of changes to low-level modules on high-level modules, making it easier to extend functionality without modifying existing code.

---

### Additional Examples:

1. **Bad Example (Violates DIP):**
```python
class FileManager:
    def read_file(self):
        pass

    def write_file(self):
        pass

class XMLParser:
    def parse(self):
        pass

class DataProcessor:
    def __init__(self):
        self.file_manager = FileManager()
        self.parser = XMLParser()

    def process_data(self):
        self.file_manager.read_file()
        self.parser.parse()
```

- **What's wrong?**: `DataProcessor` depends directly on both `FileManager` and `XMLParser`. If we want to add support for JSON parsing, we would have to modify the `DataProcessor` class, violating **Open/Closed Principle (OCP)** and **Dependency Inversion Principle (DIP)**.

**Good Example**:
```python
from abc import ABC, abstractmethod

class FileManager(ABC):
    @abstractmethod
    def read_file(self):
        pass

    @abstractmethod
    def write_file(self):
        pass

class Parser(ABC):
    @abstractmethod
    def parse(self):
        pass

class JSONParser(Parser):
    def parse(self):
        pass

class DataProcessor:
    def __init__(self, file_manager: FileManager, parser: Parser):
        self.file_manager = file_manager
        self.parser = parser

    def process_data(self):
        self.file_manager.read_file()
        self.parser.parse()
```

- **Why is this better?**:

    - `DataProcessor` now depends on abstractions (`FileManager` and `Parser`), not on concrete implementations like `FileManager` or `XMLParser`. This allows easy extension without modifying `DataProcessor` (e.g., adding a new `JSONParser`).

2. **Bad Example (Violates DIP)**:
```python
class EmailSender:
    def send_email(self, recipient, subject, message):
        pass  # Code to send an email

class NotificationService:
    def __init__(self):
        self.email_sender = EmailSender()

    def send_notification(self, recipient, message):
        subject = "New Notification"
        self.email_sender.send_email(recipient, subject, message)
```
- **What's wrong?**:
    - The `NotificationService` class directly depends on the `EmailSender` class, which is a concrete implementation.

    - If we need to add other ways to send notifications (e.g., via SMS), we would have to modify the `NotificationService` class, violating the **Open/Closed Principle (OCP)**.

    - This tight coupling makes the `NotificationService` less flexible and harder to extend with new notification methods.

**Good Example (Follows DIP)**:
```python
from abc import ABC, abstractmethod

class Notifier(ABC):
    @abstractmethod
    def send(self, recipient, message):
        pass

class EmailSender(Notifier):
    def send(self, recipient, message):
        subject = "New Notification"
        pass  # Code to send an email

class SmsSender(Notifier):
    def send(self, recipient, message):
        pass  # Code to send an SMS

class NotificationService:
    def __init__(self, notifier: Notifier):
        self.notifier = notifier

    def send_notification(self, recipient, message):
        self.notifier.send(recipient, message)
```

- **Why is this better?**

    - **Abstractions**: The `NotificationService` class no longer depends on concrete classes like `EmailSender` or `SmsSender`. It depends on the `Notifier` abstraction.

    - **Extensibility**: New types of notification senders (e.g., `PushNotificationSender`) can be added easily by implementing the `Notifier` interface without modifying the `NotificationService` class.

    - **Flexibility**: We can inject different notification methods (email, SMS, push notification) into the `NotificationService` at runtime, making the system more flexible and adaptable to change.

    - **Decoupling**: This design decouples the notification logic from the sending method, promoting cleaner and more maintainable code.