class Student:
    student = 0
    student_dict_list = []
    student_item = {}
    stu_name = ''
    stu_no = 000000

    @staticmethod
    def gernerate_stuNo():
        Student.stu_no = Student.stu_no + 1  # 学号+1
        return Student.stu_no

    def add_student(self):
        Student.student = Student.student + 1  # 学生数+1
        Student.student_dict_list.append({self.stu_no: self.student_item})  # 加入学生字典列表

    def __init__(self, name):
        self.stu_name = name  # 赋值姓名
        self.stu_no = self.gernerate_stuNo()  # 赋予学号
        self.student_item = {self.stu_no: self.stu_name}
        Student.add_student(self)

    @staticmethod
    def del_student(no=0):
        for i in Student.student_dict_list:
            if no in i.keys():
                Student.student_dict_list.pop(no-1)

    @staticmethod
    def get_student(no=0):
        for i in Student.student_dict_list:
            if no in i.keys():
                return i[no][no]

    @staticmethod
    def updata_student(no=0, name=''):
        for i in Student.student_dict_list:
            if no in i.keys():
                Student.student_dict_list[no-1][no][no] = name

    @staticmethod
    def show_all_students():
        print('学号\t\t\t 姓名')
        print(Student.student_dict_list)
        for i in Student.student_dict_list:
            for k, v in i.items():
                print(k, '\t\t\t', v[k])

