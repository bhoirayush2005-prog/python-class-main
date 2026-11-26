#setter merthod
class student:
    def __init__(self):
        self.marks = 0
    def set_marks(self, marks):
        self.marks = marks
student1 = student()
student1.set_marks(85)


#getter + setter method
class student:
    def __init__(self):
        self.marks = 0
    def set_marks(self, marks):
        self.marks = marks
    def get_marks(self):
        return self.marks
student1 = student()
print(student1.get_marks())
print(student1.set_marks(85))
print(student1.get_marks())


#multiple variables
class student:
    def __init__(self):
        self.marks = 0
        self.name = ""
        self.roll_number = 0
    def set_data(self, marks, name, roll_number):
        self.marks = marks
        self.name = name
        self.roll_number = roll_number

        if 0 <= marks <= 100:
            self.marks = marks
        else:
            print("Invalid marks. Please enter a value between 0 and 100.")
            self.marks = 0  # Set to default value if invalid
    #getter method
    def get_data(self):
        print(f"Name: {self.name}, Roll Number: {self.roll_number}, Marks: {self.marks}")

    #object creation
student1 = student()

#accepting multiple values from user
marks = int(input("Enter marks: "))
name = input("Enter name: ")
roll_number = int(input("Enter roll number: "))

s1.set_data(marks, name, roll_number)

print("Student Details:")
s1.get_data()