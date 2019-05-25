# -- coding:utf-8 --

from sys import exit

def gold_room():
    print("this room is full of gold. How much do you take?")
    next = input(">>")

    if str(next).isdigit():
        howmuch = int(next)
    else:
        dead("you dead! should input a number")

    if (howmuch <= 50):
        print("win!")
        exit(0)
    else:
        dead("XXXXXXXXXX 太贪心")

def bear_room():
    print('''
    there is a bear in front of a door,
    there are some honney,
    type \"bear\" or \"honney\" or 'door'
    ''')
    bear_move = False

    while(True):
        next = input(">>")

        if (next == "bear"):
            print("the bear move!")
            bear_move = not bear_move
        elif (next == "honney"):
            dead("the bear kills you!")
        elif (next == "door"  and bear_move):
            gold_room()
        elif (next == "door" and not bear_move):
            dead("stupid! the bear eat you!")
        else:
            print("i don't understand what you said. ")

def monster_room():
    print("""
    you see a monster!
    go back to the room or fight for life?
    input "back" or "fight" or "wait"
    """)

    times = 0
    while (True):
        next = input(">>")
        times += 1
        if (times > 5):
            dead("too slow! the monster realizes you and eat you!")
        elif (next == "fight"):
            dead("you are brave! but you die@@!")
        elif (next == "back"):
            print("right choice!")
            start()
        else:
            print("hurry up!")

def dead(why):
    print(why, "\nHAHA")
    end()

def end():
    print("""
    ----------------------------------------------------------
    |       replay        OR      quit                       |
    ----------------------------------------------------------
    please input replay or quit.
    """)

    next = input(">>")
    while ((next != "quit") and (next != "replay")):
        next = input(">>")

    if (next == "quit"):
        exit(0)
    else:
        start()

def init():
    print("""
    ----------------------------------------------------------
    |       play        OR      quit                       |
    ----------------------------------------------------------
    please input play or quit.
    """)

    next = input(">>")
    while ((next != "quit") and (next != "play")):
        next = input(">>")

    if (next == "quit"):
        exit(0)
    else:
        start()



def start():
    print("""
    2 rooms, left or right
    choose one
    """)

    next = input(">>")

    if (next == "left"):
        print("you go to the right room :)")
        bear_room()
    elif(next == "right"):
        print("you go to the right room :(")
        monster_room()
    else:
        print("what do you mean?")
        start()

init()
