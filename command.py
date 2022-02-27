import pygame
import time
from pygame.locals import *
from settings import Settings

class Command:
  def __init__(self):
    self.settings = Settings()
    self.action_idx_selected = 0
    # |0 1|
    # |2 3|
    self.actions = {
      "attack": { "label": "たたかう" },
      "spell": { "label": "じゅもん" },
      "escape": { "label": "にげる" },
      "tool": { "label": "どうぐ" },
    }

    #効果音のロード
    self.attack_sound = pygame.mixer.Sound(self.settings.attack_sound)
    self.attacked_sound = pygame.mixer.Sound(self.settings.attacked_sound)
    self.spell_sound = pygame.mixer.Sound(self.settings.spell_sound)
    self.cursor_sound = pygame.mixer.Sound(self.settings.cursor_sound)
    self.end_sound = pygame.mixer.Sound(self.settings.end_sound)
    self.escape_sound = pygame.mixer.Sound(self.settings.escape_sound)
  
  def _let_attack(self, attacker, target):
      attacker.attack(target)
    
  def _let_cast_spell(self, caster, target, spell):
      caster.cast_spell(target, spell)

  def check_key_event(self, event, player, enemy, log):
      num_of_actions = len(list(self.actions.keys()))
      if event.key == pygame.K_UP:
          self.action_idx_selected = (
              (self.action_idx_selected - 2) % num_of_actions )
          self.cursor_sound.play()
      elif event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
          self.action_idx_selected = (
              self.action_idx_selected + 1
                if self.action_idx_selected % 2 == 0
                  and self.action_idx_selected + 1 < num_of_actions
                else self.action_idx_selected - 1 )
          self.cursor_sound.play()
      elif event.key == pygame.K_DOWN:
              self.action_idx_selected = (
                  (self.action_idx_selected + 2) % num_of_actions )
              self.cursor_sound.play()
      elif event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
          self.cursor_sound.play()
          log.change_action_idx_selected(self.action_idx_selected)
          time.sleep(0.5)
          action_keys = list(self.actions.keys())
          selected_key = action_keys[self.action_idx_selected]
          if selected_key == "attack":
              self._let_attack(player, enemy)
              self._play_sound_attack()
          elif selected_key == "spell":
              self.actions = player.spells
          elif selected_key == "escape":
              self._play_sound_escape()
          else:
              self._let_cast_spell(player, enemy, selected_key)
              self._play_sound_spell()

      elif event.key == pygame.K_BACKSPACE:
          self.actions = { 
            "attack": { "label": "たたかう" },
            "spell": { "label": "じゅもん" },
            "escape": { "label": "にげる" },
            "tool": { "label": "どうぐ" },
          }


  def _play_sound_attack(self):
          self.attack_sound.play()
          time.sleep(1)
          self.attacked_sound.play()

  def _play_sound_spell(self):
        self.spell_sound.play()
        time.sleep(1)
        self.attacked_sound.play()

  def _play_sound_escape(self):
      self.escape_sound.play()

  def draw(self, screen):
    pygame.draw.rect(screen, (255, 255, 255), Rect(self.settings.command_position+self.settings.command_length), 10)
    pygame.draw.rect(screen, (0,0,0), Rect(self.settings.command_position+self.settings.command_length))

    action_labels = list(map(lambda elem: elem["label"], self.actions.values()))
    action_texts = list(map(
      lambda action: self.settings.font.render(action, False, (255, 255, 255)), action_labels
    ))
    command_action_positions = [
      self.settings.command_action_position_upper_left,
      self.settings.command_action_position_upper_right,
      self.settings.command_action_position_lower_left,
      self.settings.command_action_position_lower_right,
    ]
    for idx in range(len(action_texts)):
      screen.blit(action_texts[idx], command_action_positions[idx])

    cursor_positions = [
      (self.settings.command_action_position_upper_left[0]-18,
        self.settings.command_action_position_upper_left[1]),
      (self.settings.command_action_position_upper_right[0]-18,
        self.settings.command_action_position_upper_right[1]),
      (self.settings.command_action_position_lower_left[0]-18,
        self.settings.command_action_position_lower_left[1]),
      (self.settings.command_action_position_lower_right[0]-18,
        self.settings.command_action_position_lower_right[1]),
    ]
    cursor = self.settings.font.render("▶", False, (255, 255, 255))
    screen.blit(cursor, cursor_positions[self.action_idx_selected])
    