# Interface Segregation Principle (ISP)

## Definition

*"A client should not be forced to depend on interfaces it does not use."*

Interfaces should be **specific** rather than all-encompassing.

## Bad Example (Violates ISP)
```python
from abc import ABC, abstractmethod

class Worker(ABC):
    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat(self):
        pass

class Human(Worker):
    def work(self):
        return "I'm working!"

    def eat(self):
        return "I'm eating!"

class Robot(Worker):
    def work(self):
        return "I'm working!"

    def eat(self):
        raise Exception("I don't eat!")  # ❌ Violates ISP
```

## What's Wrong?

- **Robot** is forced to implement the `eat()` method, even though it doesn't need it.

- By implementing unused methods like `eat()`, the `Robot` class violates the **Interface Segregation Principle**.

- Clients relying on `Robot` will encounter unnecessary code (like exceptions) if they attempt to invoke `eat()`.

## Good Example (Follows ISP)
```python
from abc import ABC, abstractmethod

class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass

class Human(Workable, Eatable):
    def work(self):
        return "I'm working!"

    def eat(self):
        return "I'm eating!"

class Robot(Workable):
    def work(self):
        return "I'm working!"
```

- We separate concerns into distinct interfaces:

    - `Workable` for objects that can work.

    - `Eatable` for objects that can eat.

- **Robot** only implements the `Workable` interface, avoiding the unnecessary `eat()` method.

- By using smaller, more specific interfaces, each class only implements what it actually needs, following **ISP**.

## Key Takeaways

- The **Interface Segregation Principle (ISP)** advocates for interfaces that are specific to client needs, ensuring clients don't depend on methods they don’t use.

- **ISP** prevents the forcing of unnecessary methods upon classes, helping maintain flexibility and cleaner design.

- By separating functionality into smaller interfaces, we achieve better maintainability and scalability in our codebase.


---

### Additional Examples:

1. **Bad Example:**
   A `Device` class that forces subclasses to implement both `play()` and `charge()` methods:

```python
class Device:
    def play(self):
        pass

    def charge(self):
        pass

class Phone(Device):
    def play(self):
        return "Playing music"

    def charge(self):
        return "Charging phone"

class TV(Device):
    def play(self):
        return "Playing channel"

    def charge(self):
        raise Exception("I don't charge!")  # ❌ Violates ISP
```

- **What's wrong?**:  TV doesn't need the `charge()` method but is forced to implement it.

**Good Example**:  Split responsibilities into separate interfaces:

```python
class Playable(ABC):
    @abstractmethod
    def play(self):
        pass

class Chargeable(ABC):
    @abstractmethod
    def charge(self):
        pass

class Phone(Playable, Chargeable):
    def play(self):
        return "Playing music"

    def charge(self):
        return "Charging phone"

class TV(Playable):
    def play(self):
        return "Playing channel"
```

- **Why is this better?**:
    - The `TV` class doesn't need to implement `charge()`, as it implements only the `Playable` interface.

    - The `Phone` implements both `Playable` and `Chargeable`, following **ISP** properly.


2. **Bad Example**: A `Bird` interface that forces subclasses to implement `fly()` and `swim()`:

```python
class Bird(ABC):
    @abstractmethod
    def fly(self):
        pass

    @abstractmethod
    def swim(self):
        pass

class Sparrow(Bird):
    def fly(self):
        return "I can fly"

    def swim(self):
        return "I can swim"

class Penguin(Bird):
    def fly(self):
        raise Exception("I can't fly")  # ❌ Violates ISP
    def swim(self):
        return "I can swim"
```
- **What's wrong?**: `Penguin` doesn't need to implement `fly()`, but is forced to because of the interface.

**Good Example**: Split the interface into more appropriate parts:

```python
class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass

class Swimmable(ABC):
    @abstractmethod
    def swim(self):
        pass

class Sparrow(Flyable, Swimmable):
    def fly(self):
        return "I can fly"

    def swim(self):
        return "I can swim"

class Penguin(Swimmable):
    def swim(self):
        return "I can swim"
```

- **Why is this better?**

    - The `Penguin` class only implements the Swimmable interface, not the unnecessary Flyable interface.

    - Each class only implements the relevant functionality, adhering to ISP.
