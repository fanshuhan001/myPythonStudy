#!/usr/bin/env python3
# -*-coding:utf-8 -*-

from abc import ABCMeta, abstractmethod
from random import randint, randrange

class Fighter(object, metaclass = ABCMeta):
    '''能打架的生物'''
    __slots__ = ('_name', '_hp', '_power')

    def __init__(self, name, hp, power):
        '''
        初始化方法
        param
            name: 名字
            hp:生命值
            power：攻击力
        '''
        self._name = name
        self._hp = hp
        self._power = power

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @property
    def power(self):
        return self._power

    @hp.setter
    def hp(self, hp):
        self._hp = hp

    @property
    def alive(self):
        return self._hp >= 0

    @abstractmethod
    def fightwith(self, other):
        '''和别的生物打架
        ：param 
            other： 打的对象
        '''
        pass
    
class Ultraman(Fighter):
    __slots__ = ('_name', '_hp', '_power', '_mp')

    def __init__(self, name, hp, power, mp):
        '''初始化方法
        ：param:
            name:名字
            hp:血量
            power:攻击力
            mp:能量值
        '''
        super().__init__(name, hp, power)
        self._mp = mp

    def fightwith(self, other):
        '''和别人打架'''
        delta = self.power - other.power
        if  delta >= 0:
            other.hp -= delta * randint(5, 10)
        else:
            self.hp -= -delta * randint(5, 10) 
    
    def ultimate(self, other):
        '''
        用大招攻击,消耗50点mp, 
        造成0.8倍武力值*敌方当前生命值的3/4的伤害
        :param other:被攻击方
        :return 成功返回true,失败则进行一次普通攻击并返回false   
        '''
        if self._mp >= 50:
            self._mp -= 50
            # injury = self._power * 0.8 * other.hp * 3 // 4
            injury = self._power * 0.8 * other.hp * 3 // 4
            injury = injury if injury <= 3000 else 3000
            other.hp -= injury
            return True
        else:
            self.fightwith(other)
            return False

    def magic_att(self, others):
        '''
        魔法攻击，范围攻击，消耗20点mp，对所有敌方随机造成10-20点伤害
        :param others:被攻击方
        :return ：成功返回true, 失败返回false
        '''
        if self._mp >= 20:
            self._mp -= 20
            for target in others:
                if target.alive:
                    target.hp -= randint(100,200)
            return True
        else:
            return False
    
    def resume(self):
        '''恢复一次魔法值,数值随机1-10'''
        increase_value = randint(1,10)
        self._mp += increase_value
        return increase_value
    
    #__str__提供一个供print()使用的字符串
    def __str__(self):
        return "*****%s奥特曼*****有%d生命值和%d魔法值，它的攻击力是%d"%(self._name,
                self._hp, self._mp, self._power)
            
class Monster(Fighter):
    '''怪兽'''
    __slots__ = ("_nme", "_hp", "_power")

    def fightwith(self, other):
        other.hp -= randint(10,50)

    def __str__(self):
        return "*****%s*****有%d生命值，它的攻击力是%d"%(self._name,
                self._hp, self._power)


def has_alive_monster(monsters):
    '''判断是否有怪兽活着'''
    for one in monsters:
        if one.alive:
            return True    
    return False
    
def choose_one(monsters):
    '''选择一直活的怪兽打架'''
    lenth = len(monsters)
    while True:
        monster = monsters[randrange(lenth)]
        if monster.alive:
            return monster
    

def display_info(ultraman, monsters = []):
    '''展示当前奥特曼和怪兽的信息'''
    print(ultraman)
    for monster in monsters:
        print(monster)
    print("-----------------------------------------------")

def fight():
    jack = Ultraman('杰克', 1800, 150, 100)
    udian = Monster('尤迪安', 2500, 80)
    lucifa = Monster('路西法', 3000, 100)
    kabuda = Monster('卡布达', 3750, 130)
    xiaoyj = Monster('小妖精', 5000, 145)
    monsters = [udian, lucifa, kabuda, xiaoyj]

    fight_round = 1
    display_info(jack, monsters)
    print("---------------------------------------战斗开始-------------------------------------")

    while (jack.alive) and has_alive_monster(monsters):
        print("\t\t\t\tround %02d" %fight_round)

        target = choose_one(monsters)#选择一只活着的怪兽

        skill_use_rate = randint(1,10)
        if skill_use_rate <= 6:  # 60%几率使用普通攻击
            print("%s 使用普通攻击攻击了%s" %(jack.name, target.name))
            jack.fightwith(target)
            print("%s恢复魔法值%d" %(jack.name, jack.resume()))
        elif skill_use_rate <=9: # %30几率使用魔法范围攻击
            if jack.magic_att(monsters):
                print("%s 使用了魔法攻击攻击，对所有怪兽造成了伤害" %(jack.name))
            else:
                print("%s 使用魔法攻击攻击失败，发了一下呆" %(jack.name))
        else:                    # %10使用大招
            if jack.ultimate(target):
                print("%s 使用大招攻击攻击了%s" %(jack.name, target.name))
            else:
                print("%s 使用普通攻击攻击了%s" %(jack.name, target.name))
                print("%s恢复魔法值%d" %(jack.name, jack.resume()))
        
        #怪兽反击
        if target.alive:
            print("%s反击了%s"%(target.name, jack.name))
            target.fightwith(jack)
        
        #交战后打印所有信息
        display_info(jack, monsters)
        fight_round += 1
    
    print("\n---------------------------战斗结束-----------------------\n")
    if jack.alive:
        print("奥特曼胜利")
        display_info(jack)
    else:
        print("怪兽胜利！")
        display_info(jack, monsters)

if __name__ == "__main__":
    fight()