#Exercise 1

x = str(input(""))
print(x.count('b')) 


#Exercise 2

name=input("Enter your name:  ")
while True:
    if name[0].islower()or name [2:].isupper()or name.isdigit():
        print("Start your name with a Capital letter : ")
        name=input("Enter your name:  ")
    else:
        print(name)
        break

#Exercise 3

text="Hello world"
print(sum(list(map(ord,text))))

#Exercise 4 variant 1

import math
a="Pi={:.2f}".format(math.pi)
b="Pi={:.3f}".format(math.pi)
c="Pi={:.4f}".format(math.pi)
d="Pi={:.5f}".format(math.pi)
e="Pi={:.6f}".format(math.pi)
f="Pi={:.7f}".format(math.pi)
g="Pi={:.8f}".format(math.pi)
h="Pi={:.9f}".format(math.pi)
i="Pi={:.10f}".format(math.pi)
j="Pi={:.11f}".format(math.pi)
print(a,b,c,d,e,f,g,h,i,j)

# variant 2

from math import pi
for i in range (2, 11):
    print (round (pi, i))


#Exercse 5

x=("The longest word in the string ")
x=x.split()
print(max(x,key=len))