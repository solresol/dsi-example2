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
    else:
        sys.exit("No such file: bus.jpg")

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
