number = input("sonlarni kiriting >> ")

nums = number.split()

for s in nums:
    if int(s) % 3 == 0 or int(s) % 2 == 1:
        print(s, end = " ")
    
