class StudentLimitExceededError(Exception):
    def __init__(self, message="Не можна додати більше 10 студентів до групи."):
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

    # Порівняння студентів по їх строковому представлення
    def __eq__(self, other):
        if isinstance(other, Student):
            return str(self) == str(other)
        return False

    # Реалізація методу хешування
    def __hash__(self):
        return hash(str(self))


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


# Створення студентів
st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')

# Створення групи
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)

# Виведення групи
print(gr)

# Тести на пошук студентів
assert gr.find_student('Jobs') == st1  # Повертає студента 'Steve Jobs'
assert gr.find_student('Jobs2') is None  # Студент з таким прізвищем не знайдений

# Видалення студента
gr.delete_student('Taylor')
print(gr)  # Після видалення залишився тільки один студент

# Тест на спробу додавання більше 10 студентів
try:
    # Додаємо ще 9 студентів для тесту
    for i in range(9):
        st = Student('Male', 20, f'First{i}', f'Last{i}', f'AN1{i}')
        gr.add_student(st)
    gr.add_student(Student('Male', 21, 'Extra', 'Student', 'AN200'))  # Повинен викликати помилку
except StudentLimitExceededError as e:
    print(e)  # Достигнуто ліміту студентів