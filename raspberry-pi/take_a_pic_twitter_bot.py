#!/usr/bin/env python
import sys
from twython import Twython
import os
 
import pygame
import pygame.camera
from pygame.locals import *
 
# https://www.makeuseof.com/tag/how-to-build-a-raspberry-pi-twitter-bot/

pygame.init()
pygame.camera.init()
cam = pygame.camera.Camera("/dev/video0",(640,480))
cam.start()
image = cam.get_image()
pygame.image.save(image,'webcam.jpg')
 
CONSUMER_KEY = 'jmyBuGoaMKS05x85qFCNRw'
CONSUMER_SECRET = 'U2Ay9nv0CxdopruNk4DR9aRDyhry98ML7mYMCStdaI'
ACCESS_KEY = '354540970-nMZVfXJqTbEP8ddj3jwRNs8UMXlZapZpbxiaLg0v'
ACCESS_SECRET = 'L9MnMvXLROx76CT9NzjR7PFrtMcIb1U9venQwK1ygY'
 
#photo = open('webcam.jpg','rb')
#api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)
#api.update_status_with_media(media=photo, status='My RPi be tweeting images now => ')