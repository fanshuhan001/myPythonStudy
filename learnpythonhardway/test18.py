# --coding:utf-8 --

def print_two(*args):
    arg1, arg2 = args
    print("arg1:%r, arg2:%r"%(arg1, arg2))

def print_two_again(arg1, arg2):
    print("arg1:%r, arg2:%r"%(arg1, arg2))

def print_one(arg1):
    print("arg1:%r"%(arg1))

def print_none():
    print("********************")


print_two("w ","555")
print_two_again("dfsgdfg", "fdsgdfgsfdg")
print_one("???????????")
print_none()
