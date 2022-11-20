import pathlib


class Path():
  @staticmethod
  def generate_absolute_path(path):
    return str(pathlib.Path(__file__).parents[1]) + "/assets/" + path
