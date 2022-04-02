import pygame
from pygame.locals import *

class Sound():
  @staticmethod
  def play(filename):
    path = "../sound/" + filename + ".wav"
    sound = pygame.mixer.Sound(path).play()

  @staticmethod
  def play_bgm():
    pygame.mixer.music.load("../sound/bgm.mp3")
    pygame.mixer.music.play(-1)