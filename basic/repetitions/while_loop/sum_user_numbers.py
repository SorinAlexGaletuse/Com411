print("How many numbers should i sum up?")
times = int(input())

total = 0

print()

count=0
while total<times:
    print(f"Enter the {total} number of {times}.")
    number= int(input())
    count = count+number
    total = total+1

print(f"The answer is {count}")

