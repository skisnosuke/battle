from configuration import Config


class Spell:
  _spell = Config.spell

  @staticmethod
  def get_label(self, id):
    return self._spell[id]["label"]
  
  @staticmethod
  def get_mp(self, id):
    return self._spell[id]["mp"]

  @staticmethod
  def get_damage(self, id):
    return self._spell[id]["damage"]


  # @staticmethod #TODO
  # def cast(id):
  #   return Spell.
