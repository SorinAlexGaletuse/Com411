def directions():
    directions = [ "Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return directions

def menu():
    print("Please select a direction:")
    direction = directions()
    for index in range (len(direction)):
        print(f"{index}:{direction[index]}")

def run():
    menu()

if __name__ == "__main__":
    run()
