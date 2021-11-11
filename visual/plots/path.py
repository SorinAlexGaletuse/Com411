import matplotlib.pyplot as plt


def coordinate():
    print("Please enter a value for X:")
    x = int(input())
    print("Please enter a value for Y:")
    y = int(input())
    return (x,y)

def path():
    print("Retrieving path...")
    x_value = []
    y_value = []
    for count in range(4):
        data = coordinate()
        x_value.append(data[0])
        y_value.append(data[1])
    return [x_value,y_value]

def run():
    values = path()
    plt.plot(values[0],values[1],'r--o')
    plt.xlabel("X Values")
    plt.ylabel("Y Values")
    plt.show()

run()