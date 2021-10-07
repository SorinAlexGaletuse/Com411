print("How many bars should be charged?")
bars = int(input())
count = 0
print()

while count<bars:
    count=count+1
    print(f"Charging: {'█'*count}")

print("The battery is fully charged.")