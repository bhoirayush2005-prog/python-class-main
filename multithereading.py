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