import matplotlib.pyplot as plt

def read_data(file_path):
    temp = []
    with open(file_path) as file:
        for line in file:
            temp.append(float(line.strip()))
    return temp

def run():
    data = read_data('C:/Users/user/PycharmProjects/Com411/visual/subplots/temps.txt')
    fig,(ax1,ax2) = plt.subplots(1,2)
    ax1.plot(range(len(data)),data)
    ax2.bar(range(len(data)),data)
    plt.show()

run()