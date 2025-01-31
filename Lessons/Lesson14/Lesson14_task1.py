class StudentLimitExceededError(Exception):
    def __init__(self, message="Можна додати не більше 10 студентів в групу"):
        self.message = message
        super().__init__(self.message)

class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, Age: {self.age}, Gender: {self.gender}"

class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()}, Record Book: {self.record_book}"

class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise StudentLimitExceededError("Не можна додати більше 10 студентів до групи.")
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = "\n".join([str(student) for student in self.group])
        return f'Group Number: {self.number}\nStudents:\n{all_students}'

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')

gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)

print(gr)

assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод пошуку повинен повертати екземпляр Student'

gr.delete_student('Taylor')
print(gr)

for i in range(3, 12):
    st = Student('Male' if i % 2 == 0 else 'Female', 20 + i, f"FirstName{i}", f"LastName{i}", f"AN1{i}")
    try:
        gr.add_student(st)
        print(f"Студент {st.first_name} {st.last_name} доданий до групи.")
    except StudentLimitExceededError as e:
        print(e)
try:
    st_extra = Student('Male', 28, 'Extra', 'Student', 'AN999')
    gr.add_student(st_extra)
except StudentLimitExceededError as e:
    print(f"Error: {e}")