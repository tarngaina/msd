import item, random

areas = []

def add(a):
  areas.append(a)

def find_id(id):
  for a in areas:
    if a.id == id:
      return a
  return None

def find_name(name):
  for a in areas:
    if a.name.lower() == name.lower():
      return a
  return None

def find(id):
  a = find_id(id)
  if a == None:
    a = find_name(id)
  return a

class Area():
  def __init__(self, id, name, is_safe, texture = None, **dic):
    self.id = id
    self.name = name
    self.is_safe = is_safe
    self.texture = texture
    if not self.is_safe:
      self.lv = dic['lv']
      self.att = dic['att']
      self.xp = dic['xp']
      self.xp_rate = dic['xp_rate']
      self.meso = dic['meso']
      self.items = dic['items']
    
  def random_item(self):
    return random.choice(self.items)

  def get_name(self):
    s = ''
    if self.texture != None:
      s += self.texture
    s += f'**{self.name}**'
    return s

add(
  Area(
    id = 'hsys',
    name = 'Henesys',
    is_safe = False,
    texture = '<:henesys:771211976374222890>',
    lv = 5,
    att = 24,
    xp = 33,
    xp_rate = 1.4,
    meso = 31,
    items = item.get_victoria_island_etc() + item.get_frozen_set()
  )
)
add(
  Area(
    id = 'ell',
    name = 'Ellinia',
    is_safe = False,
    texture = '<:ef:771211983407284224>',
    lv = 15,
    att = 99,
    xp = 198,
    xp_rate = 1.6,
    meso = 105,
    items = item.get_victoria_island_etc() + item.get_frozen_set()
  )
)
add(
  Area(
    id = 'kc',
    name = 'Kerning City',
    is_safe = False,
    texture = '<:kc:771211996296904755>',
    lv = 25,
    att = 154,
    xp = 463,
    xp_rate = 1.8,
    meso = 230,
    items = item.get_victoria_island_etc() + item.get_frozen_set()
  )
)
add(
  Area(
    id = 'nts',
    name = 'Nautilus Harbor',
    is_safe = False,
    texture = '<:ntls:771212002798338079>',
    lv = 35,
    att = 223,
    xp = 890,
    xp_rate = 1.9,
    meso = 380,
    items = item.get_victoria_island_etc() + item.get_frozen_set()
  )
)
add(
  Area(
    id = 'prn',
    name = 'Perion',
    is_safe = False,
    texture = None,
    lv = 45,
    att = 283,
    xp = 2051,
    xp_rate = 1,
    meso = 450,
    items = item.get_victoria_island_etc() + item.get_frozen_set()
  )
)
