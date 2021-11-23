import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate(frame):
  global ax
  ax.cla()
  x = [1,2,3,4,5]
  y = [2,4,6,8,10]
  ax.plot(x[:frame],y[:frame] , 'ro--')
  ax.set_xlim(0,5)
  ax.set_ylim(0,10)


fig, ax = plt.subplots(1,1)
some_animation = animation.FuncAnimation(fig, animate, frames = 5, interval = 1000, repeat=False)

plt.show()