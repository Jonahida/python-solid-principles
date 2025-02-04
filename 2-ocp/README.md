# Open/Closed Principle (OCP)

## Definition
*"Software entities should be open for extension but closed for modification."*
This means that adding new functionality **should not** require modifying existing code.

---

## Bad Example (Violates OCP)
```python
class DiscountCalculator:
    def calculate(self, customer_type, price):
        if customer_type == "regular":
            return price * 0.9  # 10% discount
        elif customer_type == "vip":
            return price * 0.8  # 20% discount
        else:
            return price  # No discount
```

## What’s Wrong?

The `DiscountCalculator` class directly handles all discount logic based on the customer type. As a result:
- Adding a new discount type requires modifying the existing `DiscountCalculator` class.
- If more conditions (like different customer types or new discount rules) are added, the `calculate` method will become longer and harder to maintain.

This violates the **Open/Closed Principle** because we are modifying the class instead of extending its functionality.

## Good Example (Follows OCP)
```python
from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, price):
        pass

class RegularDiscount(DiscountStrategy):
    def apply_discount(self, price):
        return price * 0.9  # 10% discount

class VIPDiscount(DiscountStrategy):
    def apply_discount(self, price):
        return price * 0.8  # 20% discount

class GoldDiscount(DiscountStrategy):
    def apply_discount(self, price):
        return price * 0.7  # 30% discount

class DiscountCalculator:
    def __init__(self, strategy: DiscountStrategy):
        self.strategy = strategy

    def calculate(self, price):
        return self.strategy.apply_discount(price)

# Example usage
discount = DiscountCalculator(VIPDiscount())
print(discount.calculate(100))  # Output: 80.0
```
## Why is this better?

- **Extensibility**: New discount types can be added (e.g., `GoldDiscount`) without modifying the existing `DiscountCalculator` class. We simply create a new class implementing the `DiscountStrategy` interface.
  
- **Closed for Modification**: The existing code remains unchanged. We add functionality (new discount strategies) by creating new classes, rather than altering the existing ones.
  
- **Flexible and Scalable**: The design allows for easy addition of new discount types, making the codebase more flexible and scalable.

- **Easier to Test**: Each discount strategy is encapsulated in its own class, making unit tests for each strategy simpler and isolated from others.

## Key Takeaways

- The **Open/Closed Principle (OCP)** encourages designing classes in a way that allows for extending their behavior without altering their existing code.
- By using **polymorphism** (like the strategy pattern in the good example), we can introduce new features while keeping the existing system stable and unmodified.
- This principle reduces the risk of **regression bugs** when new features are added and makes the system more maintainable in the long run.

---

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

**Good Example**: Separate the concerns into different classes:

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

**Good Example**: Separate the printing logic into a different class:

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

## Additional Examples

1. **Bad Example:**
   A `PaymentProcessor` class that handles different payment methods using conditionals

```python
class PaymentProcessor:
    def process_payment(self, payment_method, amount):
        if payment_method == "credit_card":
            # Process credit card payment
            print(f"Processing credit card payment of ${amount}")
        elif payment_method == "paypal":
            # Process PayPal payment
            print(f"Processing PayPal payment of ${amount}")
        elif payment_method == "bitcoin":
            # Process Bitcoin payment
            print(f"Processing Bitcoin payment of ${amount}")
        else:
            raise ValueError("Invalid payment method")
   ```

- **What's wrong?**:  The `PaymentProcessor` class uses conditionals to handle different payment methods. Every time a new payment method is introduced (e.g., `apple_pay`, `stripe`), the process_payment method has to be modified. This violates the **Open/Closed Principle**.

- **Good Example**: Use polymorphism to define separate classes for each payment method:

```python
from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardPayment(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")

class PayPalPayment(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")

class BitcoinPayment(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing Bitcoin payment of ${amount}")

class PaymentProcessor:
    def __init__(self, payment_method: PaymentMethod):
        self.payment_method = payment_method

    def process(self, amount):
        self.payment_method.process_payment(amount)

# Example usage
payment = PaymentProcessor(CreditCardPayment())
payment.process(100)  # Output: Processing credit card payment of $100
```

- **Why is this better?**: The `PaymentProcessor` class now adheres to the **Open/Closed Principle**. New payment methods can be added by creating new classes that implement the `PaymentMethod` interface, without needing to modify the existing code in `PaymentProcessor`.


2. - **Bad Example**
   A `TaxCalculator`class that calculates tax based on different countries

```python
class TaxCalculator:
    def calculate_tax(self, country, income):
        if country == "USA":
            return income * 0.1  # 10% tax for USA
        elif country == "UK":
            return income * 0.2  # 20% tax for UK
        elif country == "Germany":
            return income * 0.25  # 25% tax for Germany
        else:
            raise ValueError("Invalid country")
```
- **What's wrong?**:  The `TaxCalculator` class contains conditionals for different countries. Whenever a new country’s tax rate needs to be added, the class must be modified, violating the **Open/Closed Principle**.

- **Good Example**: Use polymorphism to define separate classes for each country’s tax calculation:

```python
from abc import ABC, abstractmethod

class TaxCalculator(ABC):
    @abstractmethod
    def calculate_tax(self, income):
        pass

class USATaxCalculator(TaxCalculator):
    def calculate_tax(self, income):
        return income * 0.1  # 10% tax for USA

class UKTaxCalculator(TaxCalculator):
    def calculate_tax(self, income):
        return income * 0.2  # 20% tax for UK

class GermanyTaxCalculator(TaxCalculator):
    def calculate_tax(self, income):
        return income * 0.25  # 25% tax for Germany

class TaxProcessor:
    def __init__(self, calculator: TaxCalculator):
        self.calculator = calculator

    def process_tax(self, income):
        return self.calculator.calculate_tax(income)

# Example usage
tax_calculator = TaxProcessor(USATaxCalculator())
print(tax_calculator.process_tax(1000))  # Output: 100.0
```

- **Why is this better?**: The `TaxProcessor` class remains closed for modification, and new tax calculation strategies (such as for new countries) can be added by creating new subclasses of `TaxCalculator`. This allows the system to be easily extended without modifying existing code.

3. - **Bad Example**
   A `ReportGenerator`class that handles different report formats with conditionals

```python
class ReportGenerator:
    def generate_report(self, report_type):
        if report_type == "pdf":
            # Generate PDF report
            print("Generating PDF report...")
        elif report_type == "csv":
            # Generate CSV report
            print("Generating CSV report...")
        elif report_type == "excel":
            # Generate Excel report
            print("Generating Excel report...")
        else:
            raise ValueError("Invalid report type")
```
- **What's wrong?**:  The `ReportGenerator` class requires modification whenever a new report type is added. This violates the **Open/Closed Principle** because the class is not closed for modification.

- **Good Example**: Use polymorphism to create separate classes for each report format:

```python
from abc import ABC, abstractmethod

class Report(ABC):
    @abstractmethod
    def generate(self):
        pass

class PDFReport(Report):
    def generate(self):
        print("Generating PDF report...")

class CSVReport(Report):
    def generate(self):
        print("Generating CSV report...")

class ExcelReport(Report):
    def generate(self):
        print("Generating Excel report...")

class ReportGenerator:
    def __init__(self, report: Report):
        self.report = report

    def generate(self):
        self.report.generate()

# Example usage
report_generator = ReportGenerator(PDFReport())
report_generator.generate()  # Output: Generating PDF report...
```

- **Why is this better?**: The `ReportGenerator` class no longer requires modification when a new report type is added. We can easily extend the functionality by adding new subclasses of `Report` without altering existing code, keeping the system open for extension but closed for modification.
