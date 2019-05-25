# -- coding:utf-8 --

class Student(object):
    def __init__(self, name, age, sid):
        self.name = name
        self.age = age
        self.sid = sid

    def study(self, course):
        print("%s is taking %s"%(self.name, course))
    
    def watch_tv(self):
        if self.age >= 18:
            print("%s can watch some good things" %self.name)
        else:
            print("%s 学点好吧" %self.name)

class MyTest(object):
    def __init__(self, foo):
        self.__foo = foo
    
    def __bar(self):
        print(self.__foo)
        print("__bar")


def main():
    fan = Student("Fan Shuhan", 25, "001")
    fei = Student("Ren Fei", 28, "002")
    fei.study("工作")
    fan.study("python")
    fei.watch_tv()
    fan.watch_tv()

#--------------------------------------------------------------------------
#定义一个时钟类
from time import sleep
import os

class Clock(object):
    '''数字时钟'''

    def __init__(self, hour=0, minute=0, second=0):
        '''
        初始化方法
        :param hour:时钟
        :param minute:分钟
        :param second:秒钟
        '''
        self._hour = hour
        self._minute = minute
        self._second = second

    def ticktock(self):
        '''
        走字
        '''
        self._second += 1
        if self._second == 60:
            self._minute += 1
            self._second = 0
            if self._minute == 60:
                self._hour += 1
                self._minute = 0
                if self._hour == 24:
                    self._hour = 0
    
    def display(self):
        while True:
            self.ticktock()
            #os.system('cls')
            sleep(1)
            print("%d : %d : %d" %(self._hour, self._minute, self._second))


if __name__ == "__main__":
    '''
    test = MyTest('??')
    #test.__bar()   // 属性错误，MyTest 类没有__bar()这个arttibute
    test._MyTest__bar() # 这样就可以访问私有成员了
    '''

    myclock = Clock()
    myclock.display()