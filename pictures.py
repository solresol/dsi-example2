#!/usr/bin/python

import skimage.io
import matplotlib.pyplot
import os
import sys

######################################################################
# bus
def display_bus():
    if os.path.exists('bus.jpg'):
        bus = skimage.io.imread('bus.jpg')
        matplotlib.pyplot.imshow(bus)

######################################################################
# unicorns
def display_unicorn():
    pass

######################################################################
# platypus
def display_platypus():
    pass


######################################################################
# dragon
def display_unicorn():
    if os.path.exists('unicorn.jpg'):
      uni = skimage.io.imread('unicorn.jpg')
      matplotlib.pyplot.imshow(uni)
    else:
        sys.exit("No unicorns here!")

######################################################################
# beach scene
def display_beach_scene():
    pass


######################################################################
# sky
def display_sky():
     if os.path.exists('dragon.jpg'):
        dragon = skimage.io.imread('dragon.jpg')
        matplotlib.pyplot.imshow(dragon)
     else:
      	print "Dragon does not exist"



######################################################################
# Main program

display_bus()
display_unicorn()
display_platypus()
display_dragon()
display_beach_scene()
display_sky()
