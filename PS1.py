import matplotlib.pyplot as plt
import numpy as np
from astropy.io import ascii
import matplotlib.image as mpimg

def problem1():
  diagram = mpimg.imread('cloud_diagram.png')
  plt.figure(figsize=(10,8))
  plt.imshow(diagram)
  plt.axis('off')


def problem2():
  data = ascii.read('comacluster_mushotzky.csv',format='csv')
  print(data.keys())
