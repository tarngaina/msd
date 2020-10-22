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
  def __init__(self, id, name, is_safe, **dic):
    self.id = id
    self.name = name
    self.is_safe = is_safe
    if not self.is_safe:
      self.lv = dic['lv']
      self.att = dic['att']
      self.hp = dic['hp']
      self.xp = dic['xp']
      self.xp_rate = dic['xp_rate']
      self.meso = dic['meso']
      self.items = dic['items']
    
  def random_item(self):
    return random.choice(self.items)

add(
  Area(
    id = 'fm',
    name = 'free market',
    is_safe = True
  )
)
add(
  Area(
    id = 'hsys',
    name = 'henesys',
    is_safe = False,
    lv = 1,
    att = 24,
    hp = 11,
    xp = 33,
    xp_rate = 1.4,
    meso = 31,
    items = [
      item.find('mcap'),
      item.find('snail')
    ]
  )
)
add(
  Area(
    id = 'ef',
    name = 'ellinia',
    is_safe = False,
    lv = 10,
    att = 99,
    hp = 90,
    xp = 198,
    xp_rate = 1.6,
    meso = 63,
    items = [
      item.find('sliquid'),
      item.find('ltail')
    ] + item.get_burning_set()
  )
)
add(
  Area(
    id = 'kc',
    name = 'kerning city',
    is_safe = False,
    lv = 20,
    att = 154,
    hp = 209,
    xp = 463,
    xp_rate = 1.8,
    meso = 150,
    items = [
      item.find('bwing'),
      item.find('lskin')
    ] + item.get_burning_set()
  )
)
add(
  Area(
    id = 'nts',
    name = 'nautilus harbor',
    is_safe = False,
    lv = 30,
    att = 223,
    hp = 468,
    xp = 890,
    xp_rate = 1.9,
    meso = 230,
    items = [
      item.find('ribbon'),
      item.find('starfish')
    ] + item.get_burning_set()
  )
)