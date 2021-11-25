import matplotlib.pyplot as plt
import matplotlib.animation as animation


def animate(frame):
    print(f"Frame:{frame}")

def run():
    global fig
    fig, ax = plt.subplots()
    frame = animation.FuncAnimation(fig, animate, frames=10, interval=1000)
    plt.show()

run()