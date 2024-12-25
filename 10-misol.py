text = input("Matnni kiriting: ")

words = text.split()
max_word = text[0]

for word in words:
    if len(word) > len(max_word):
        max_word = word

print("Eng uzun so'z:", max_word)
