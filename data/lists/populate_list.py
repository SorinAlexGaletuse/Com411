def directions():
    directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return directions

def menu():
        print("Please select a direction:")
        direction = directions()
        for index in range(len(direction)):
            print(f"{index}:{direction[index]}")
        user_input = int(input())
        return direction[user_input]

def run():
    route = []
    print("Working out escape route...")
    for count in range(5):
     route.append(menu())
     print(f"Escape route:{route}")

if __name__ == "__main__":
  run()