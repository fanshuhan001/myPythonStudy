#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from abc import ABCMeta, abstractmethod

class Pet(object, metaclass = ABCMeta):
    '''
    abstract class
    can not creat instances
    '''
    def __init__(self, generic_name):
        self._generic_name =  generic_name

    @abstractmethod
    def talk(self):
        '''
        发出声音
        '''
        pass
    

class Dog(Pet):
    '''狗'''
    def talk(self):
        print("%s:汪汪汪..."%self._generic_name)

class Cat(Pet):
    '''猫'''
    def talk(self):
        print("%s:喵喵喵..."%self._generic_name)

class Buou(Cat):
    '''布偶猫'''
    def __init__(self, generic_name, cat_name):
        super().__init__(generic_name)
        self._cat_name = cat_name

    @property
    def cat_name(self):
        return self._cat_name

    @cat_name.setter
    def cat_name(self, aname):
        self._cat_name = aname

if __name__ == "__main__":
    xiaobai = Buou("猫", "小白")
    print(xiaobai.cat_name, "\n-------------------------------")
    xiaobai.cat_name = "白白"
    print(xiaobai.cat_name)
    xiaobai.talk()