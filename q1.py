# Define Person Class
class Person:
    def __init__(self, fname, lname, age):
        # Initialize Person object with first name, last name, and age
        self.fname = fname
        self.lname = lname
        self.age = age

    def get_info(self):
        # Print full name and age of the Person
        print("Full Name:", self.fname, self.lname)
        print("Age:", self.age)


# Defining Student class inherited Person class
class Student(Person):
    def __init__(self, fname, lname, age, student_id):
        # Initialize Student object with first name, last name, age, and student ID
        super().__init__(fname, lname, age)
        self.student_id = student_id

    def get_stuinfo(self):
        # Print student's information by calling the parent class method and adding student ID
        super().get_info()
        print("Student ID:", self.student_id)


# Defining Employee class inherited Person class
class Employee(Person):
    def __init__(self, fname, lname, age, employee_num, salary):
        # Initialize Employee object with first name, last name, age, employee number, and salary
        super().__init__(fname, lname, age)
        self.employee_num = employee_num
        self.salary = salary

    def get_empinfo(self):
        # Print employee's information by calling the parent class method and adding employee number and salary
        super().get_info()
        print("Employee Number:", self.employee_num)
        print("Salary:", self.salary)


# Example usage:
if __name__ == '__main__':
    # Create a new Student object and print its information
    new_student = Student("Anthony", "Smith", 35, "s346571")
    new_student.get_stuinfo()
    print("==========================")
    # Create a new Employee object and print its information
    new_employee = Employee("Sarah", "Taylor", 34, 2919736, 5000)
    new_employee.get_empinfo()

