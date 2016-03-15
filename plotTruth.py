import matplotlib
matplotlib.use('TkAgg')   #backend works well for interactive purposes
import numpy as np
import os, glob, time
from matplotlib import pyplot as plt
import matplotlib.image as mpimg

# S.B.Strong (03/2016)
# Purpose: create int array of keystroke values associated with images in a 
#          directory for training data/truth data

if __name__ == '__main__':
dir='*.jpg'   #input full path to image directory with extensions like: /mnt/data/*.jpg
Array=[]
plt.ion() # turn on interactive mode, non-blocking `show`
for f in glob.glob(dir):            #loop over all image files in path
    image = mpimg.imread(f)         #plot one
    plt.figure()                    # create a new figure
    plt.imshow(image)               # plot the figure
    plt.show()                      # show the figure, non-blocking
    d = raw_input("0 no square in image or 1 for square in image. Then press [enter] to continue.") # wait for input from the user
    Array.append(d)
    plt.close()    # close the figure to show the next one.

Array = [int(i) for i in Array]

        
        
        
 