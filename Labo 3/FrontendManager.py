# from Employees import Employee
# from EmployeesManager import EmployeeManager
#
# class FrontendManager:
#     def __init__(self, fManager):
#         self.manager = fManager
#
#     def menu(self):
#         while True:
#             print("\n--- Menu ---")
#             print("1. Dodaj nowego pracownika")
#             print("2. Wyświetl listę pracowników")
#             print("3. Usuń pracowników na podstawie wieku")
#             print("4. Zaktualizuj wynagrodzenie pracownika")
#             print("5. Wyjdź z programu")
#
#             choice = input("Wybierz opcję (1-5): ")
#
#             if choice == "1":
#                 self.add_employee()
#             elif choice == "2":
#                 self.view_employees()
#             elif choice == "3":
#                 self.remove_employees_by_age()
#             elif choice == "4":
#                 self.update_employee_salary()
#             elif choice == "5":
#                 print("Zamykanie programu. Do widzenia!")
#                 break
#             else:
#                 print("Niepoprawna opcja. Spróbuj ponownie.")
#
#     def add_employee(self):
#         name = input("Podaj imię i nazwisko nowego pracownika: ")
#         try:
#             age = int(input("Podaj wiek pracownika: "))
#             salary = float(input("Podaj wynagrodzenie pracownika: "))
#             new_employee = Employee(name, age, salary)
#             self.manager.addEmployee(new_employee)
#         except ValueError:
#             print("Niepoprawna wartość dla wieku lub wynagrodzenia. Spróbuj ponownie.")
#
#     def view_employees(self):
#         self.manager.currentEmployees()
#
#     def remove_employees_by_age(self):
#         try:
#             age = int(input("Podaj maksymalny wiek pracowników do usunięcia: "))
#             self.manager.removeEmployeesByAge(age)
#             print(f"Usunięto pracowników młodszych niż {age} lat.")
#         except ValueError:
#             print("Niepoprawna wartość dla wieku. Spróbuj ponownie.")
#
#     def update_employee_salary(self):
#         self.manager.updateEmployeesSalary()
#
#
# pracownik1 = Employee("Mariusz Pudzianowski", 30, 5000)
# pracownik2 = Employee("Milosz Wojcik", 22, 3500)
# pracownik3 = Employee("Sandra Parawan", 20, 9700)
#
# employees = [pracownik1, pracownik2, pracownik3]
# manager = EmployeeManager("Adrian Puchacki", 30, 13000, employees)
#
# frontend = FrontendManager(manager)
# frontend.menu()

import json
from Employees import Employee
from EmployeesManager import EmployeeManager

import json
from Employees import Employee
from EmployeesManager import EmployeeManager

class FrontendManager:
    def __init__(self, manager, data_file):
        self.manager = manager
        self.data_file = data_file
        self.load_data()

    def menu(self):
        if not self.login():
            print("Niepoprawne dane logowania. Program zakończony.")
            return

        while True:
            print("\n--- Menu ---")
            print("1. Dodaj nowego pracownika")
            print("2. Wyświetl listę pracowników")
            print("3. Usuń pracowników na podstawie wieku")
            print("4. Zaktualizuj wynagrodzenie pracownika")
            print("5. Wyjdź z programu")

            choice = input("Wybierz opcję (1-5): ")

            if choice == "1":
                self.add_employee()
            elif choice == "2":
                self.view_employees()
            elif choice == "3":
                self.remove_employees_by_age()
            elif choice == "4":
                self.update_employee_salary()
            elif choice == "5":
                print("Zamykanie programu. Do widzenia!")
                self.save_data()
                break
            else:
                print("Niepoprawna opcja. Spróbuj ponownie.")

    def login(self):
        print("\n--- Logowanie ---")
        username = input("Podaj login: ")
        password = input("Podaj hasło: ")
        return username == "admin" and password == "admin"

    def load_data(self):
        try:
            with open(self.data_file, "r") as file:
                data = json.load(file)
                self.manager.employeesList = [
                    Employee(emp["name"], emp["age"], emp["salary"])
                    for emp in data
                ]
        except (FileNotFoundError, json.JSONDecodeError):
            print("Plik danych nie istnieje lub jest uszkodzony. Utworzono nowy.")

    def save_data(self):
        with open(self.data_file, "w") as file:
            data = [
                {"name": emp.name, "age": emp.age, "salary": emp.salary}
                for emp in self.manager.employeesList
            ]
            json.dump(data, file, indent=4)

    def add_employee(self):
        name = input("Podaj imię i nazwisko nowego pracownika: ")
        try:
            age = int(input("Podaj wiek pracownika: "))
            salary = float(input("Podaj wynagrodzenie pracownika: "))
            if age <= 0 or salary < 0:
                raise ValueError("Wiek i wynagrodzenie muszą być dodatnie.")
            new_employee = Employee(name, age, salary)
            self.manager.addEmployee(new_employee)
            self.save_data()
        except ValueError as e:
            print(f"Błąd: {e}. Spróbuj ponownie.")

    def view_employees(self):
        self.manager.currentEmployees()

    def remove_employees_by_age(self):
        try:
            age = int(input("Podaj maksymalny wiek pracowników do usunięcia: "))
            if age <= 0:
                raise ValueError("Wiek musi być dodatni.")
            self.manager.removeEmployeesByAge(age)
            self.save_data()
            print(f"Usunięto pracowników młodszych niż {age} lat.")
        except ValueError as e:
            print(f"Błąd: {e}. Spróbuj ponownie.")

    def update_employee_salary(self):
        self.manager.updateEmployeesSalary()
        self.save_data()


pracownik1 = Employee("Mariusz Pudzianowski", 30, 5000)
pracownik2 = Employee("Milosz Wojcik", 22, 3500)
pracownik3 = Employee("Sandra Parawan", 20, 9700)
employees = [pracownik1, pracownik2, pracownik3]
manager = EmployeeManager("Adrian Puchacki", 30, 13000, employees)


frontend = FrontendManager(manager, "employees_data.json")
frontend.menu()
