import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate(frame):
  global axs

  x = [1,2,3,4,5,6,7]
  y = [1,4,9,16,25,36,48]
  axs[0,0].cla()
  axs[0,0].plot(x[:frame],y[:frame],'ro--')
  axs[0,0].set_xlim(min(x),max(y))
  axs[0,0].set_ylim(min(x),max(y))

  axs[0,1].cla()

  axs[0,1].bar(x[:frame], y[:frame])
  axs[0,1].set_xlim(min(x), max(y))
  axs[0,1].set_ylim(min(x), max(y))

  slices = [10,20,50,20]
  axs[1,0].cla()
  axs[1,0].pie(slices[:frame])

  axs[1,1].cla()
  axs[1,1].bar([1,2],[1,2+frame])
  axs[1,1].set_xlim(min(x), max(y))
  axs[1,1].set_ylim(min(x), max(y))


fig, axs = plt.subplots(2,2)
some_animation = animation.FuncAnimation(fig, animate, frames = 80, interval = 1000, repeat=False)

plt.show()