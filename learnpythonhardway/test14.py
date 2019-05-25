# -- coding:utf-8 --

from sys import argv

script, user_name = argv
prompt = '>'

print("hi %s, I'm the %s script."%(user_name, script))
print("I'd like to ask you a few questions.")
print("do you like me? %s"%user_name)
likes = input(prompt)

print("what kind of computer do you have?")
computer = input(prompt)

print('''
你说你%r喜欢我
你有一个%r的电脑，真棒！
'''%(likes, computer))
