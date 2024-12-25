text = input("Matnni kiriting: ")

words = text.split()

long_word = max(words, key=len)
print("Eng uzun so'z:", long_word)
