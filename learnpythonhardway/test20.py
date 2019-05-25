# --coding:utf-8 --

from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_line(line_count, f):
    print(line_count, f.readline())

with open(input_file, "r") as current_file:
    print("**********all************")
    for x in current_file:
        print(x)
    print_all(current_file)
    print("-----------rewind now-------------")
    rewind(current_file)
    print("-------print 3 lines-------------")
    current_line = 1
    print_line(current_line, current_file)
    current_line = current_line + 1
    print_line(current_line, current_file)
    current_line += 1
    print_line(current_line, current_file)
    print("-----------------------------")
