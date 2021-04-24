import datetime


class Groups:
    numbers_of_students = 0
    stipend_percent = 1.07
    default_stipend = 1040

    def __init__(self, first, last, group, stipend):
        self.first = first
        self.last = last
        self.group = group
        self.stipend = stipend
        self.person = first + ' ' + last + ', Group:' + \
            group
        Groups.numbers_of_students += 1

    def student(self):
        print("Info: " + self.person)
        return self.person

    def apply_raise(self):
        self.stipend = int(self.stipend * self.stipend_percent)
        return self.stipend

    @classmethod
    def raise_stipend_by(cls, new_value):
        cls.default_stipend = cls.default_stipend + new_value

    @classmethod
    def from_string(cls, stud):
        first, last, group, stipend = stud.split(':')
        stipend = int(stipend)
        return cls(first, last, group, stipend)

    @staticmethod
    def is_study_day(day):
        if day.weekday() == 5 or day.weekday() == 6:
            print("Weekends!")
            return False
        else:
            print("Study day!")
            return True

    def __repr__(self):
        return "Students('{}','{}','{}')".format(self.first, self.last, self.group)

    def __str__(self):
        return '{}, stipend:{}'.format(self.person, self.stipend)


class Stud(Groups):
    pass


class Workers:
    salary_percent = 2.03

    def __init__(self, first, last, position, salary):
        self.first = first
        self.last = last
        self.position = position
        self.salary = salary

    def apply_salary_raise(self):
        self.salary = int(self.salary * self.salary_percent)
        return self.salary

    def __add__(self, other):
        return self.salary + other.salary


class Curators(Workers):
    def __init__(self, first, last, position, salary, subject, main_student=None):
        super(Curators, self).__init__(first, last, position, salary)
        self.subject = subject
        if main_student is None:
            self.main_student = []
        else:
            self.main_student = main_student

    def print_main_stud(self):
        print("Main student is:", self.main_student.person)


class Teachers(Curators):
    salary_percent = 3.03

    def __init__(self, first, last, position, salary, subject, main_student=None):
        super(Teachers, self).__init__(first, last, position, salary, subject)
        if main_student is None:
            self.main_student = []
        else:
            self.main_student = main_student


class Doctors(Workers):
    salary_percent = 4.03

    def __init__(self, first, last, position, salary, certificate_pass):
        super(Doctors, self).__init__(first, last, position, salary)
        self.certificate_pass = certificate_pass


student1 = Groups("Maksym", "Severyn", "It-12sp", 1040)
student2 = Groups("Bohdan", "Martyniv", "It-12sp", 1040)
student3 = Groups("Vasyl", "Horobec", "M-12", 1040)

worker1 = Workers("John", "Wick", "Teacher", 6000)
worker2 = Teachers("Olena", "Sidorko", "Teacher", 6000, "Math", student1)
worker3 = Doctors("Viktoria", "Set", "Nurse", 7000, True)
worker4 = Curators("Evgenia", "Oscar", "Curator", 6500, "IT", student1)
worker2.print_main_stud()
worker4.print_main_stud()

print("Is worker4 inheriting from 'Teachers' class?",
      isinstance(worker4, Teachers))
print("Is 'Doctors' Subclass of 'Workers'?",
      issubclass(Doctors, Workers))

worker2.apply_salary_raise()
print(worker2.salary)
temp1 = vars(worker1)
for item1 in temp1:
    print(item1, ':', temp1[item1])

temp2 = vars(worker2)
for item2 in temp2:
    print(item2, ':', temp2[item2])

temp3 = vars(worker3)
for item3 in temp3:
    print(item3, ':', temp3[item3])


student4 = Stud("Oleh", "Ivanov", "F-21", 1040)
print("------------------------------")
# print(help(student4))
print("------------------------------")
student1.apply_raise()

Groups.raise_stipend_by(500)
print("New Stipend Amount:", Groups.default_stipend)


stud_1 = "Oleh:Syp:T-12sp:4000"
new_stud1 = Groups.from_string(stud_1)

temp = vars(new_stud1)
for item in temp:
    print(item, ':', temp[item])


date = datetime.date(2021, 4, 11)
Groups.is_study_day(date)

print(student1.stipend)
print(student2.stipend)
print(student3.stipend)
print(Groups.numbers_of_students)
student1.student()
student2.student()
student3.student()
print(student1)
print("Sum of 2 workers salary:")
print(worker1+worker2)
