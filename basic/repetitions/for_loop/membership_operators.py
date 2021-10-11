print("What phrase do you see?")
word = input()

print("Reversing...")
print("The phrase is :", end="")

reversed = ""

for count in word:
    reversed = count+reversed

print(reversed)