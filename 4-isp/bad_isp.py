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

