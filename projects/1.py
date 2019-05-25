import argparse

'''
将华氏度转化为摄氏度
F = 1.8C + 32
Author : Fan Shuhan
'''
def temperature_change(fahrenheit):
    if (isinstance(fahrenheit, float) or isinstance(fahrenheit, int)):
        c = float((fahrenheit - 32) / 1.8)
        return c#(fahrenheit - 32) / 1.8
    else:
        raise(TypeError)


'''
输入半径，计算周长和面积
C = 2PI*r
S = PI*r*r
'''
def get_perimeter_area(radius):
    PI = 3.1415926
    c = float(2 * PI * radius)
    s = float(PI * radius * radius)
    return c,s

'''
输出99乘法表
'''
def mul_chart():
    for a in range(1, 10):
        for b in range(1, a + 1):
            print("%d * %d = %d"%(b, a, a*b), end='\t')
        print("\t")

'''
百钱百鸡
公鸡 ￥5 母鸡￥3 小鸡￥1
钱包 ￥100 买100只鸡
'''
def trade():
    for cock in range(0, 21):
        max_hen = (100 - cock * 5) // 3
        for hen in range(0, max_hen+1):
            chick = (100 - 5 * cock - 3 * hen) * 3
            if (100 == chick + hen + cock):
                print("cock:%d\then:%d\tchick:%d"%(cock, hen, chick))

'''
辗转相除法求最大公约数
'''   
def gcd(x, y):
    '''
    :param x,y: two int nums
    :return a int num
    '''
    (x, y) = (x, y) if x > y else (y,x)
    #print(x, '   ', y)
    if y == 0:
        return x
    else:
        return gcd(y, x-y)
    
'''
斐波那契数列生成器
'''
def fibonacci(count):
    '''
    :param count: int, generate #count numbers
    :output: a fibonacci number list
    '''
    n, first, second = 0, 0, 1
    while n < count:
        yield second #调用generator时，遇到yield关键字则返回
        first, second = second, first + second
        n += 1
    return 'done'

'''
杨辉三角
'''
def yanghui_triangle(lines):
    '''
    :param lines: how many lines should be input
    :return: a list
    '''
    n = 1
    aline = [1]
    while n <= lines:
        mid_list = []
        yield aline
        for y in range(len(aline)-1):
            temp = aline[y] + aline[y+1]
            mid_list.append(temp)
        aline = [1] + mid_list + [1]
        n += 1
    return 'done!'

def ad_board():
    '''
    产生跑马灯效果的字母
    '''
    import os, time
    content = "北 京 欢 迎 您 ! "
    while True:
        #os.system('cls')
        print(content)
        content = content[1:] + content[0]
        time.sleep(0.5)

def gen_qr_code(code_lenth):
    '''
    产生一个随机的code_lenth长度的验证码
    :param code_lenth: 验证码的长度
    :return: 大小写英文字母与数字随机组合的码
    '''
    from random import randint
    
    AllCHAR = '0123456789qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM'
    target_code = ''
    lenth = len(AllCHAR)
    
    for i in range(code_lenth):
        target_code += AllCHAR[randint(0, lenth-1)]
    
    return target_code

import os

#-------------------------------------------------------------
def print_board(board):
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
    print('-+-+-')
    print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
    print('-+-+-')
    print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])

#-------------------------------------------------------------
def main():
    init_board = {
        'TL': ' ', 'TM': ' ', 'TR': ' ',
        'ML': ' ', 'MM': ' ', 'MR': ' ',
        'BL': ' ', 'BM': ' ', 'BR': ' '
    }
    begin = True
    while begin:
        curr_board = init_board.copy()
        begin = False
        turn = 'x'
        counter = 0
        os.system('clear')
        print_board(curr_board)
        while counter < 9:
            move = input('轮到%s走棋, 请输入位置: ' % turn)
            if curr_board[move] == ' ':
                counter += 1
                curr_board[move] = turn
                if turn == 'x':
                    turn = 'o'
                else:
                    turn = 'x'
            os.system('clear')
            print_board(curr_board)
        choice = input('再玩一局?(yes|no)')
        begin = choice == 'yes'


if __name__ == "__main__":
    main()

    
