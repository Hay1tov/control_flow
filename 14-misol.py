number = int(input("sonni kiriting >> "))

i = 0
while i < number:
    i += 1
    if number % i == 0:
        print(i, end = " ")
    