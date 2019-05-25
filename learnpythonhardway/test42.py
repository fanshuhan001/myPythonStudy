# --coding:utf-8 --

class People(object):


    def __init__(self, name, id):
        self.__name = name
        #self.__score = score
        self.__id = id

    def print()



class Student(People):

    def __init__(self, score):
        #self.__name = name
        self.__score = score
        #self.__id = id

    def print_student(self):
        print("ID:%s\tName:%s\tScore:%3.2f"%(super().id, super().name, self.score))


fanShuhan = Student("范舒晗", 95, "001")

fanShuhan.print_student();
