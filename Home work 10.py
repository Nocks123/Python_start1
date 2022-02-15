#Exercise 1
a=[10,20,30,40]
print(max(a))

#Exercise 3
from random import randint
def rect_drawer(slen, llen):
    return slen*"*"+("\n"+("*"+(" "*(slen-2))+"*"))*(llen-2)+("\n"+slen*"*")
print(rect_drawer(randint(2,10),randint (2,10)))

#Exercise 4
def line_x(a,b):
    for i in range(len(a)):
        if(a[i]==b):
            return i
    return -1
print(line_x([1,2,3,4,5],8))