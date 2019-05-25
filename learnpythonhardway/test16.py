# --coding:utf-8 --

from sys import argv

script, filename = argv

print("we are going to erase %r"%filename)
print("if you dont want that, hit CTRL-C(^C).")
print("if you want that, hit RETURN")

input("?：")

print("Opening the file...")
target = open(filename, "w")

print("turncating the file. goodbye!@@")
target.truncate();

print("now i am going to ask you for three lines.")
line1 = input("line 1:")
line2 = input("line 2:")
line3 = input("line 3:")

print("i am going to write these to the file!")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)

print("and finally, we close it")
target.close()
