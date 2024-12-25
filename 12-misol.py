word = input("So'zni kiriting >> ")
count = 1
result = word[0]

for i in range(1,len(word)):
    if word[i - 1] == word[i]:
        count+=1
    else:
        if count > 1:
            print(f"{word[i - 1]}{count}", end="")
        count = 1
if count > 1:
            print(f"{word[i - 1]}{count}", end="")