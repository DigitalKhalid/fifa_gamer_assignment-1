class Student:
    passingMark = 50  # class variable

    def __init__(self, name, mark):
        # Initialize Student object with name and mark
        self.name = name
        self.mark = mark

    def __str__(self):
        # Return a string representation of the Student object
        return f"Name: {self.name}, Mark: {self.mark}"

    def passOrFail(self):
        # Check if the student passes or fails based on the passing mark
        if self.mark >= Student.passingMark:
            return "Pass"
        else:
            return "Fail"


# Part a, b, and c
if __name__ == '__main__':
    # Create a Student object with name 'John' and mark 52
    student1 = Student('John', 52)
    # Check if student1 passes or fails
    status1 = student1.passOrFail()
    print(f"Student 1 status: {status1}")

    # Part a, b, and d
    # Create a Student object with name 'Jenny' and mark 69
    student2 = Student('Jenny', 69)
    # Check if student2 passes or fails
    status2 = student2.passOrFail()
    print(f"Student 2 status: {status2}")

    # Part e
    # Update the passing mark to 60
    Student.passingMark = 60
    # Check if student1 passes or fails after updating the passing mark
    status1 = student1.passOrFail()
    # Check if student2 passes or fails after updating the passing mark
    status2 = student2.passOrFail()
    print(f"After updating passing mark, Student 1 status: {status1}")
    print(f"After updating passing mark, Student 2 status: {status2}")
