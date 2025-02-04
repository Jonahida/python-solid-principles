# Liskov Substitution Principle (LSP)

## Definition

*"Subtypes must be substitutable for their base types without altering the correctness of the program."*

A subclass should extend a superclass **without breaking** expected behavior.

## Bad Example (Violates LSP)
```python
class Bird:
    def fly(self):
        return "I can fly!"

class Sparrow(Bird):
    pass  # Sparrow can fly

class Penguin(Bird):
    def fly(self):
        raise Exception("I cannot fly!")  # ❌ Violates LSP
```

## What's Wrong?

- **Penguin** is a `Bird`, but it cannot fly.

- If a function expects `Bird` and calls `fly()`, it will crash when given a `Penguin`.

- This breaks LSP because `Penguin` is not a proper substitute for `Bird`.

## Good Example (Follows LSP)

```python
from abc import ABC, abstractmethod

class Bird(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class FlyingBird(Bird):
    @abstractmethod
    def fly(self):
        pass

class Sparrow(FlyingBird):
    def make_sound(self):
        return "Chirp!"

    def fly(self):
        return "I can fly!"

class Penguin(Bird):
    def make_sound(self):
        return "Honk!"  # Penguins make sounds but do not fly
```

## Why is this better?

- We separate flying and non-flying birds.

- `FlyingBird` has a fly method, so Sparrow correctly inherits from it.

- `Penguin` does not inherit from `FlyingBird`, so it does not have an incorrect `fly()` method.

- Now, all subclasses correctly extend their parents, following **LSP**.

## Key Takeaways

- The **Liskov Substitution Principle (LSP)** ensures that derived classes can be used interchangeably with their base class without affecting the functionality of the program.

- By following LSP, we ensure that our inheritance hierarchy is logical and doesn't break existing behavior.

- The principle helps us avoid unexpected errors in our code when substituting base class objects with derived class objects.


---

## Additional Examples

1. **Bad Example (Violates LSP)**
```python
class Rectangle:
    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def area(self):
        return self.width * self.height

class Square(Rectangle):
    def set_width(self, width):
        self.width = width
        self.height = width  # ❌ Violates LSP

    def set_height(self, height):
        self.height = height
        self.width = height  # ❌ Violates LSP
   ```

- **What's wrong?**:

    - **Square** is a subclass of `Rectangle`, but it breaks expected behavior.

    - A `Rectangle` should be able to set width and height independently, but for a `Square`, setting one dimension forces the other to be the same.

    - This violates **LSP** because a `Square` cannot be used as a true substitute for a `Rectangle`.

- **Good Example  (Follows LSP)**: 
```python
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side
```

- **Why is this better?**
    - Both `Rectangle` and `Square` now implement the `Shape` interface and calculate area in a way that makes sense for each class.

    - `Square` does not break the expected behavior of `Rectangle` and can now be used interchangeably with other shapes without issues.

2. - **Bad Example**

```python
class Bird:
    def fly(self):
        return "I can fly!"

class Ostrich(Bird):
    def fly(self):
        raise Exception("I cannot fly!")  # ❌ Violates LSP
```

- **What's wrong?**:

    - **Ostrich** is a `Bird`, but it cannot fly.

    - If a function expects a `Bird` and calls `fly()`, it will crash when given an `Ostrich`.

    - This breaks **LSP** because `Ostrich` cannot be used as a proper substitute for `Bird`.

- **Good Example  (Follows LSP)**:
```python
from abc import ABC, abstractmethod

class Bird(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class FlyingBird(Bird):
    @abstractmethod
    def fly(self):
        pass

class Ostrich(Bird):
    def make_sound(self):
        return "Boom!"  # Ostriches make sounds but do not fly
```

- **Why is this better?**
    - `Ostrich` does not need to inherit from `FlyingBird` because it does not fly.

    - By separating flying birds from non-flying birds, we maintain proper behavior and avoid breaking LSP.


