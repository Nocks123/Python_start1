# Exercise 1
number_less = int(input("Enter number less then ZERO = "))
if number_less < 0:
    print("Good! It's negative number!")

number_positive = int(input("Don't enter more ZERO! = "))
if number_positive > 0:
    print("It so bad...")

# Exercise 2
value_a = int(input("value_A= "))
if value_a < 20:
    print("It's Good!")
else:
    print("It's Bad")
print("Game Over")

# Exercise 3
while True:
    number = int(input("insert any number: "))
    if number == -1:
        break
    elif number == 0:
        print("True")
    else:
        print("False")

# Exercise 4

x = int(input("Enter number: "))
if x % 2 == 0:
    print("Even number")
else:
    print("Odd number")