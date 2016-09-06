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
    if os.path.exists('unicorn.jpg'):
    	uni = skimage.io.imread('unicorn.jpg')
    	matplotlib.pyplot.imshow(uni)
    else:
        sys.exit("No unicorns here!")

######################################################################
# platypus
def display_platypus():
    count = 0
    if os.path.exists('platypus.jpg'):
        platypus = skimage.io.imread('platypus.jpg')
        matplotlib.pyplot.imshow(platypus)
        count += 1
        count
    else:
        sys.exit("Platypus down!!")


######################################################################
# dragon
def display_dragon():
    pass

######################################################################
# beach scene
def display_beach_scene():
    pass


######################################################################
# sky
def display_sky():
    pass


######################################################################
# Main program

display_bus()
display_unicorn()
display_platypus()
display_dragon()
display_beach_scene()
display_sky()
