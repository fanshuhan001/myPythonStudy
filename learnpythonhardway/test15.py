# -- coding:utf-8 --

from sys import argv

script, filename = argv

txt = open(filename, 'r')

print("Here is your file %r:" %filename)
print(txt.read())
print("please type the filename again:")
file_again = input("> ")

txt_again = open(file_again, 'r')

print(txt_again.read())
