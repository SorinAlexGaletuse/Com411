print("Please enter the first whole number.")
first = int(input())
print("Please enter the second whole number.")
second = int(input())
print("Please enter the third whole number.")
third = int(input())

even = 0
odd = 0

if first % 2 == 0:
    even = even+1
else:
    odd = odd+1

if second % 2 == 0:
    even = even+1
else:
    odd = odd+1

if third % 2 == 0:
    even = even+1
else:
    odd = odd+1

print(f"There were {even} even and {odd} odd numbers.")