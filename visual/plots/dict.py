import matplotlib.pyplot as plt
import random

def data():
    paths = {}
    print("What types of lines would you prefer(: , -- or -):")
    lines = input()
    print("What colour would you prefer(r , g or b):")
    colour = input()
    print("What style of markers would you like(o , s or ^):")
    marker = input()
    paths['lines'] = lines
    paths['colour'] = colour
    paths['marker'] = marker
    return paths

def generate():
    print("How many lines would you like to display?")
    lines_to_create = int(input())
    for count in range(lines_to_create):
        values = data()
        x = random.sample(range(1,10),lines_to_create)
        y = random.sample(range(1,10),lines_to_create)
        display = f"{values['colour']}{values['lines']}{values['marker']}"
        plt.plot(x,y,display)

    plt.show()

def run():
    print("Running...")
    generate()
    print("Done!")

run()