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

