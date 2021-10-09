class School(object):
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr
        self.students = []
        self.teachers = []
        self.staffs = []

    def enroll(self, stu_obj):
        print("为%s办理注册手续" % stu_obj.name)
        self.students.append(stu_obj)

    def hire(self, staff_obj):
        print("招聘了一名老师：%s" % staff_obj.name)
        self.staffs.append(staff_obj)


class SchoolMember(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def tell(self):
        pass


class Teacher(SchoolMember):
    def __init__(self, name, age, sex, salary, course):
        super(Teacher, self).__init__(name, age, sex)
        self.salary = salary
        self.course = course

    def tell(self):
        print('''
        ---- info of the %s 
        name : %s
        age ： %s
        sex：%s
        salary : %s
        course : %s
        ''' % (self.name, self.name, self.age, self.sex, self.salary, self.course))

    def teach(self):
        print("%s is teaching course [%s]" % (self.name, self.course))


class Students(SchoolMember):
    def __init__(self, name, age, sex, stu_id, grade):
        super(Students, self).__init__(name, age, sex)
        self.stu_id = stu_id
        self.grade = grade

    def tell(self):
        print('''
        ---- info of student : %s 
        name : %s
        age  : %s
        sex  : %s
        stu_id : %s 
        grade: %s 
        ''' % (self.name, self.name, self.age, self.sex, self.stu_id, self.grade))

    def pay_tuition(self, amount):
        print("%s has paid tution for ￥%s" % (self.name, amount))


School = School("Tener", "HangZhou")

t1 = Teacher("qwe", "22", "M", 8000, "Python")
t2 = Teacher("asd", "25", "F", 6000, "Linux")

s1 = Students("qaz", "18", "M", 10, 2101)
s2 = Students("rfv", "17", "M", 11, 2101)

t1.tell()
s1.tell()

School.enroll(t1)
