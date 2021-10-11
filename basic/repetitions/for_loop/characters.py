print("What strange markings do you see?")
user_input = input()

print("Identifying...\n")

for count in range (0,len(user_input),1):
    print(f"item {count}:", user_input[count] )

print("Done!")