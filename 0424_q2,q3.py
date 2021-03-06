# -*- coding: utf-8 -*-
"""0424_Q2,Q3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SvIwoavXRQU71Phld-jyXStG_84WO0rL
"""

from google.colab import drive
drive.mount('/content/gdrive')

import math

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt
# %matplotlib inline

class Circle(object): 

  def __init__(self, radius, color):
    self.radius = radius
    self.color = color 

  def size(self):
    r = self.radius
    return(r*r*math.pi)

  def drawCircle(self): 
    plt.gca().add_patch(plt.Circle((0,0), radius = self.radius, fc = self.color)) 
    plt.axis('scaled') 
    plt.show()

class Rectangle(object):

  def __init__(self, width, height, color):
    self.width = width
    self.height = height
    self.color = color 
  
  def size(self):
    a = self.width
    b = self.height 
    return(a*b)

  def drawRectangle(self):
    plt.gca().add_patch(plt.Rectangle((0,0), self.width, self.height, fc = self.color))
    plt.axis('scaled')
    plt.show()

cir = "/content/gdrive/My Drive/circle.txt"

f = open(cir, 'r')
while True:
  line = f.readline()
  if line=='':
    break
  circle = Circle(int(line[0]), line[3:].rstrip('\n'))
  circle.drawCircle()

f.close()

rec = "/content/gdrive/My Drive/rectangle.txt"

f = open(rec, 'r')
while True:
  line = f.readline()
  if line=='':
    break
  rectangle = Rectangle(int(line[0]), int(line[3]), line[6:].rstrip('\n'))
  rectangle.drawRectangle()

f.close()

f = open(cir, 'r')
while True:
  line = f.readline()
  if line=='':
    break
  circle = Circle(int(line[0]), line[3:].rstrip('\n'))
  print(circle.size())

f.close()

f = open(rec, 'r')
while True:
  line = f.readline()
  if line=='':
    break
  rectangle = Rectangle(int(line[0]), int(line[3]), line[6:].rstrip('\n'))
  print(rectangle.size())

f.close()

