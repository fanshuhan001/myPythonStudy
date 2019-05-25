# -- coding: utf-8 --

the_count = [1, 2, 3, 4, 5, 6]
fruits = ['apple', '梨', 'stawberry', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for member in the_count:
    print("this is count %d" %member)

for member in fruits:
    print("this is a fruit: %s" %member)

for i in change:
    print("I GOT %r" % i)

element = range(0,6)
'''
for i in range(0,6):
    print("adding %d to the list" %i)
    element.append(i)
'''
for i in element:
    print("find:%d" %i)
