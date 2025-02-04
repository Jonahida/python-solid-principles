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

