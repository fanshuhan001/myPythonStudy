# --coding:utf-8 --

from sys import argv
from os.path import exists

script, from_file, to_file =argv

print("copy form %r to %r"%(from_file, to_file))

print("now, we copy the content from %r"%from_file)
content = open(from_file).read()
lenth = len(content)
print("the file is %d bytes long"% lenth)

print("now, write the content to %r"%to_file)
isExist = exists(to_file)
print("check! does the target file exsit?%r"%isExist)
output = open(to_file, "w")
output.write(content)

print('done!')
output.close()
#close(from_file)
