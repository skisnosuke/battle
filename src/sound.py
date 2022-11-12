import time

from pygame import mixer

from path import Path


class Sound():
  @staticmethod
  def play_attack():
    path = Path.generate_absolute_path("sound/attack.wav")
    mixer.Sound(path).play()
    time.sleep(1)
    path = Path.generate_absolute_path("sound/attacked.wav")
    mixer.Sound(path).play()

  @staticmethod
  def play_cast_spell():
    path = Path.generate_absolute_path("sound/spell.wav")
    mixer.Sound(path).play()
    time.sleep(1)
    path = Path.generate_absolute_path("sound/attacked.wav")
    mixer.Sound(path).play()
  
  @staticmethod
  def play_escape():
    path = Path.generate_absolute_path("sound/escape.wav")
    mixer.Sound(path).play()

  @staticmethod
  def play_cursor():
    path = Path.generate_absolute_path("sound/cursor.wav")
    mixer.Sound(path).play()

  @staticmethod
  def play_bgm():
    path = Path.generate_absolute_path("sound/bgm.mp3")
    mixer.music.load(path)
    mixer.music.play(-1)
