number = int(input("sonni kiriting >> "))

count = 0
i = 2
while i < number:
    
    for num in range (1, i + 1):
        
        if i % num == 0:
            count += 1
            
    if count <= 2:
        print(i, end = " ")
        count = 0
        
    count = 0
    i += 1