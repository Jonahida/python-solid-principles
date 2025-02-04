class Employee:
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        return self.salary * 1.2  # Example calculation

    def generate_report(self):
        return f"Employee: {self.name}, Salary: {self.salary}"

