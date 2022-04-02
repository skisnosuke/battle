import pygame
import time
from pygame.locals import *

class Sound():
  @staticmethod
  def play_attack():
    pygame.mixer.Sound("../sound/attack.wav").play()
    time.sleep(1)
    pygame.mixer.Sound("../sound/attacked.wav").play()

  @staticmethod
  def play_cast_spell():
    pygame.mixer.Sound("../sound/spell.wav").play()
    time.sleep(1)
    pygame.mixer.Sound("../sound/attacked.wav").play()
  
  @staticmethod
  def play_escape():
    pygame.mixer.Sound("../sound/escape.wav").play()

  @staticmethod
  def play_cursor():
    pygame.mixer.Sound("../sound/cursor.wav").play()

  @staticmethod
  def play_bgm():
    pygame.mixer.music.load("../sound/bgm.mp3")
    pygame.mixer.music.play(-1)