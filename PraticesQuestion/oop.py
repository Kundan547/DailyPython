class Employee:
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, int(pay))

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    def __str__(self):
        return f'{self.fullname()} - {self.email}'

    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', {self.pay})"

    def annual_salary(self):
        return self.pay * 12

    def compare_salary(self, other):
        if self.pay > other.pay:
            return f'{self.fullname()} has a higher salary than {other.fullname()}'
        elif self.pay < other.pay:
            return f'{other.fullname()} has a higher salary than {self.fullname()}'
        else:
            return f'{self.fullname()} and {other.fullname()} have the same salary'

    @classmethod
    def display_total_employees(cls):
        return f'Total number of employees: {cls.num_of_emps}'


emp_1 = Employee('Kundan', 'Vyas', 50000)
emp_2 = Employee('Karthik', 'Vyas', 60000)
emp_3 = Employee('Vinayak', 'Vyas', 1000000)

Employee.set_raise_amt(1.05)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

emp_str_1 = 'Maan-Singh-70000'
emp_str_2 = 'Suresh-Meena-30000'
emp_str_3 = 'Abhishek-Jeenger-90000'
emp_str_4 = 'Vinayak-Ojha-1000000'

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)

import datetime
my_date = datetime.date(2025, 3, 1)

print(Employee.is_workday(my_date))

print(emp_1)
print(repr(emp_1))

print(emp_1.annual_salary())
print(emp_1.compare_salary(emp_2))

print(Employee.display_total_employees())