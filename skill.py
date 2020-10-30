class Skill():
  def __init__(self, id, name, type, **dic):
    self.id = id
    self.name = name
    self.type = type

  def get_name(self):
    s = ''
    s += f'**{self.name}**'
    return s