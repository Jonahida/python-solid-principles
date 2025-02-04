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

