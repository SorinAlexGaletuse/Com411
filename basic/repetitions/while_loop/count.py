print("How many live cables must i avoid?")
number = int(input())
count = 0
while count <number:
    print(f"Avoiding... Done! {count+1} live cable avoided.")
    count = count+1

print("All live cables have been avoided.")