# import pygame
# from pygame.locals import *
import os

class Sound():
  # bgm = "../sound/bgm.mp3"
  # attack_sound = "../sound/attack.wav"
  # attacked_sound = "../sound/attacked.wav"
  # spell_sound = "../sound/spell.wav"
  # cursor_sound = "../sound/cursor.wav"
  # end_sound = "../sound/end.wav"
  # escape_sound = "../sound/escape.wav"

  @staticmethod
  def play(filename):
    path = "../sound/" + filename + ".wav"
    print(path)
    print(os.path.exists(path))
    print(os.path.exists("..\sound\attack.wav"))
    # pygame.mixer.Sound(path).play()

    # pygame.mixer.music.load(self.settings.bgm)
    # pygame.mixer.music.play(-1)

# pygame.init()
# Sound.play("attack")