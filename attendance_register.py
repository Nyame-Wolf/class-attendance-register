from datetime import datetime


def make_gen():
    counter = 0

    def gen():
        nonlocal counter
        counter += 1
        return counter
    return gen


class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.check_in = None

    def __repr__(self):
        return f'Student(id={self.id}, name={self.name})'


class Class:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.students = {}
        self.sessions = []
        self.start_time = None

    def check_in(self, student):
        if student.checked_in:
            raise ValueError(f'This student is already in another class.')

        self.students[student.id] = student
        student.check_in = self.id

        return f'Student successfully checked into class {self.name}'

    def check_out(self, student):
        if student.checked_in:
             in_put = input('Please give a reason for this student to leave class')
             student.checked_in = False
             if in_put is None:
                raise ValueError('You must provide reason for this student to leave class')
        else:
            return 'This student is not cheked into any class'



    def log_start(self):
        if self.start_time:
            raise ValueError('This class is already in session')

        self.start_time = datetime.now()

        return f'Class started at {self.start_time}'

    def log_end(self):
        if not self.start_time:
            raise ValueError('Cannot end a class that is not in session')

        end_time = datetime.now()
        self.sessions.append({'start': self.start_time, 'end': end_time})
        self.start_time = None

        return f'Class session terminated at {end_time}'

    def __repr__(self):
        return f'Class(id={self.id}, name={self.name})'


class AttendanceRegister:
    def __init__(self):
        self.id_gen = make_gen()
        self.students = {}
        self.classes = {}

    def __str__(self):
        return 'Register with {} students and {} classes'.format(
            len(self.students), len(self.classes)
        )

    def student_add(self, student_name):
        id = self.id_gen()
        student = Student(id, student_name)
        self.students[id] = student

        return f'Added student with id {id}'

    def student_remove(self, class_id):
        b =  self.students.pop(id)

        return f'You deleted student with id {b}'

    def class_add(self, class_name):
        id = self.id_gen()
        klass = Class(id, class_name)
        self.classes[id] = klass

        return f'Added class with id {id}'

    def class_remove(self, class_id):
        k = self.classes.pop(id)

        return f'You deleted class with id {k} '

    def check_in(self, student_id, class_id):
        student = self.students[student_id]
        if not student:
            raise ValueError('That student does not exist')

        klass = self.classes[class_id]
        if not klass:
            raise ValueError('That class does not exist')

        return klass.check_in(student)

    def log_start(self, class_id):
        klass = self.classes[class_id]
        if not klass:
            raise ValueError('That class does not exist')

        return klass.log_start()

    def student_list(self,student):
        if student.checked_in:
            return f'{self.id} : {self.name} in session'
        else:
            return f'{self.id}{self.name}'


    def class_list(self):
        pass




if __name__ == "__main__":
    register = AttendanceRegister()
    # TODO: Create a CLI. Look into using either docopt or click
    print(register)
