#Exercise 1
a=input("Enter any word: ")
b=input("Enter any word: ")
a=set("#".join(a.split()))
b=set("#".join(b.split()))
print(a&b)

#Exercise 2
from random import randrange 
a=set([randrange(3,50,3)for _ in range(10)])
b=set([randrange(5,50,5)for _ in range(10)])
print(a,b)