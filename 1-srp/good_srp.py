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

