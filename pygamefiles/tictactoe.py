from email import message
import pygame, time,os,random, math, sys
pygame.init()

WIDTH = 700
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH,HEIGHT))
colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(153,255,51)}

clr = colors.get("limeGreen")
MessageMenu = ["instructions", "settings", "game 1", "game 2" ,"settings", "exit"]
messagesettings = ["background colors", "screen size"]
maintitle = "circle eats square menu"

