import item, random

areas = []

def add(m):
  areas.append(m)

def find(id):
  for m in areas:
    if m.id == id:
      return m
  return None

def find_name(name):
  for m in areas:
    if m.name.lower() == name.lower():
      return m
  return None

class Area():

  def __init__(self, id, name, is_town, mob_att = 0, mob_hp = 0, xp_rate = 0, xp = 0, meso = 0, lvl = 0, items = []):
    self.id = id
    self.name = name
    self.is_town = is_town
    self.mob_att = mob_att
    self.mob_hp = mob_hp
    self.xp_rate = xp_rate
    self.xp = xp
    self.meso = meso
    self.lvl = lvl
    self.items = items
    
  def random_item(self):
    return random.choice(self.items)

add(
  Area(
    id = 'fm',
    name = 'free market',
    is_town = True
  )
)
add(
  Area(
    id = 'hsys',
    name = 'henesys',
    is_town = False,
    mob_att = 23,
    mob_hp = 20,
    xp_rate = 1.4,
    xp = 33,
    meso = 31,
    lvl = 1,
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
    is_town = False,
    mob_att = 99,
    mob_hp = 150,
    xp_rate = 1.6,
    xp = 198,
    meso = 63,
    lvl = 10,
    items = [
      item.find('sliquid'),
      item.find('ltail')
    ]
  )
)
add(
  Area(
    id = 'kc',
    name = 'kerning city',
    is_town = False,
    mob_att = 154,
    mob_hp = 350,
    xp_rate = 1.8,
    xp = 463,
    meso = 150,
    lvl = 20,
    items = [
      item.find('bwing'),
      item.find('lskin')
    ]
  )
)
add(
  Area(
    id = 'nts',
    name = 'nautilus harbor',
    is_town = False,
    mob_att = 223,
    mob_hp = 650,
    xp_rate = 1.9,
    xp = 890,
    meso = 230,
    lvl = 30,
    items = [
      item.find('ribbon'),
      item.find('starfish')
    ]
  )
)