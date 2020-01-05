from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
from skimage import io

def gif(img_files, interval=20):
    fig, ax = plt.subplots()
    img_files = img_files
    length = len(img_files)
    imgs = []
    for i in range(length):
        imgs.append(io.imread(img_files[i]))
    def animate(i):
        i = i % length
        ax.imshow(imgs[i])
        return ax, # , is necessary
    def init():
        ax.imshow(imgs[0])
        return ax, # , is necessary
    ani = animation.FuncAnimation(fig=fig,
                                func=animate,
                                frames=length,
                                init_func=init,
                                interval=interval, 
                                blit=True) # frames : the lenth of gif; interval : update frequency
    plt.show()
#ani.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
#save gif with ffmpeg or mencoder installed

if __name__ == '__main__':
    img_files = ['1.png', '2.png', '3.png']
    gif(img_files)