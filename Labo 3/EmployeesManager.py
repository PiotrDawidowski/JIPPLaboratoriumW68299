from Employees import Employee

class EmployeeManager(Employee):
    def __init__(self, name, age, salary, employeesList):
        super().__init__(name, age, salary)
        self.employeesList = employeesList

    def describe(self):
        print(f"Imię: {self.name},\nWiek: {self.age},\nWypłata: {self.salary},\n")
        self.currentEmployees()

    def currentEmployees(self):
        print(f"Lista pracowników menedżera {self.name}:")
        for employee in self.employeesList:
            print(f" - {employee.name}")

    def addEmployee(self, employee):
        if isinstance(employee, Employee):
            self.employeesList.append(employee)
            print(f"Dodano pracownika {employee.name} do losty pracowników menedżera {self.name}.\n")

    def removeEmployeesByAge(self, ageOFEmployee):
        for employee in self.employeesList[:]:  # iterujemy po kopii żeby nie usuwać poprawnych elementó
            if employee.age < int(ageOFEmployee):
                self.employeesList.remove(employee)

    def searchForEmployeeByName(self, nameOfEmployee):
        found = False
        for employee in self.employeesList[:]:
            if employee.name == nameOfEmployee:
                print("Znaleziono pracownika! Jego dane:")
                employee.describe()
                found = True
                break # jezeli nie znajdzie i nie zamkniemy funkcji to wypisze info o braku pracownika tyle razy ile pracownikow jest w liscie
            if not found:
                print("Nie znaleziono pracownika o tym imieniu i nazwisku.")

    def updateEmployeesSalary(self):
        while True:
            name = input(
                "Podaj pełne imię i nazwisko pracownika, którego pensję chcesz zaktualizować (lub wpisz 'anuluj', aby zakończyć): ")

            # Allow the user to exit the loop
            if name.lower() == "anuluj":
                print("Operacja została anulowana.\n")
                break

            # Search for the employee by name
            for employee in self.employeesList:
                if employee.name == name:
                    try:
                        new_salary = float(input(f"Podaj nową pensję dla {employee.name}: "))
                        employee.salary = new_salary
                        print(f"Pensja pracownika {employee.name} została zaktualizowana na {new_salary}.\n")
                    except ValueError:
                        print("Niepoprawna wartość dla pensji. Operacja anulowana.\n")
                    return  # Exit the function once the employee is found and updated

            # If the loop completes without finding the employee
            print("Nie znaleziono pracownika o podanym imieniu i nazwisku. Spróbuj ponownie.\n")


# ------------------------------------------------------------------------

pracownik1 = Employee("Mariusz Pudzianowski", 30, 5000)
pracownik2 = Employee("Milosz Wojcik", 22, 3500)
pracownik3 = Employee("Sandra Parawan", 20, 9700)
pracownik4 = Employee("Lebron James", 39, 123000)

employees = [pracownik1, pracownik2, pracownik3]
manager1 = EmployeeManager("Adrian Puchacki", 30, 13000, employees)

# manager1.describe()
# manager1.addEmployee(pracownik4)
# manager1.currentEmployees()
# manager1.removeEmployeesByAge(32)
# manager1.currentEmployees()
# manager1.searchForEmployeeByName("Mariusz Pudzianowski")
# manager1.updateEmployeesSalary()
# pracownik1.describe() # jezeli zmienimy place pracownikowi1 to program pokaze ze funkcja dziala
