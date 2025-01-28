class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def describe(self):
        print(f"Imię: {self.name},\nWiek: {self.age},\nWypłata: {self.salary}\n")