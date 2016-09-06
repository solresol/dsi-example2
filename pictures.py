#!/usr/bin/python

import skimage.io
import matplotlib.pyplot
import os

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
def display_dragon():
    pass

######################################################################
# beach scene
def display_beach_scene():
    picname = 'beach.jpg'
    if os.path.exists('beach.jpg'):
        pic = skimage.io.imread('beach.jpg')
        matplotlib.pyplot.imshow(pic)
    else:
	print "Picture does not exist"


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
