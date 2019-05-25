# -- coding:utf-8 --

ten_words = "sdjaf slkdajfl asdfjlk klsadjafkl aslkdfj kjasldfj eropqwe"

print("there's not 10 things!")

stuff = ten_words.split(" ")
more_word = ["day", "night", "knight", "people"]

while (len(stuff) != 10):
    next_one = more_word.pop()
    print("now add one word: %s" %next_one)
    stuff.append(next_one)

print(stuff,"\n", stuff[1],)
print(stuff[-1])
print(stuff.pop())
#join()
print(" ".join(stuff))
#3-5 add three #?
print("#".join(stuff))
