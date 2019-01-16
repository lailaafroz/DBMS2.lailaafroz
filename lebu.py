from tkinter import *
from tkinter import *
from tkinter import filedialog
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

root = Tk()
root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                           filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
print(root.filename)

from pylab import imread,subplot,imshow,show

import matplotlib.pyplot as plt

image = imread(root.filename)
#// choose image location
plt.imshow(image)
plt.show()