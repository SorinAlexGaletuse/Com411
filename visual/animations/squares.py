import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig,ax = plt.subplots()
square = []
def init():
    global square
    square.append({"x":[4,4,5,5,4],"y":[4,5,5,4,4]})
    square.append({"x":[3,3,6,6,3],"y":[3,6,6,3,3]})
    square.append({"x":[1,1,7,7,1],"y":[1,7,7,1,1]})

def animate(frame):
    global square ,ax

    index = frame%3
    ax.set_xlim(0,10)
    ax.set_ylim(0,10)
    ax.plot(square[index]["x"],square[index]["y"])

def run():
    global fig
    square_anime = animation.FuncAnimation(fig, animate, frames=3, interval=1000, init_func=init)
    plt.show()

run()