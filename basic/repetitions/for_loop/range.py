print("What level of brightness is required?")
level = int(input())

print("Adjusting brightness...")

for count in range(2,level+1,2):
    print(f"Beep's brightness level:{'*'* count}")
    print(f"Bop's brightness level:{'*'* count}")

print("Adjustments complete!")