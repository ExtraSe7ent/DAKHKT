class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Tên sinh viên: {self.name}, {self.age} tuổi.")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self):
        print(f"Sinh viên {self.name} (MSSV: {self.student_id}) hiện đang vắng mặt.")

student_1 = Student(name="Quang Anh", age=21, student_id="23110149")

student_1.introduce()
student_1.study()