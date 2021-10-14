def display_ladder(steps):
    for step in range (steps):
        print("| |")
        print("***")

    print("| |")

def create_ladder():
    print("How many steps remaining?")
    steps = int(input())
    display_ladder(steps)

create_ladder()