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

  def __init__(self, id, name, is_town, mob_att = 0, mob_hp = 0, xp_rate = 0, xp = 0, meso = 0, lvl_recommended = 0, items = []):
    self.id = id
    self.name = name
    self.is_town = is_town
    self.mob_att = mob_att
    self.mob_hp = mob_hp
    self.xp_rate = xp_rate
    self.xp = xp
    self.meso = meso
    self.lvl_recommended = lvl_recommended
    self.items = items
    
  def random_item(self):
    return random.choice(self.items)

add(
  Area(
    id = 'hsys',
    name = 'henesys',
    is_town = True
  )
)
add(
  Area(
    id = 'mg',
    name = 'mushroom garden',
    is_town = False,
    mob_att = 27,
    mob_hp = 30,
    xp_rate = 1.3,
    xp = 57,
    meso = 31,
    lvl_recommended = 1,
    items = [
      item.find('mcap'),
      item.find('snail')
    ]
  )
)

add(
  Area(
    id = 'ct',
    name = 'chimney tree',
    is_town = False,
    mob_att = 128,
    mob_hp = 100,
    xp_rate = 1.5,
    xp = 148,
    meso = 63,
    lvl_recommended = 10,
    items = [
      item.find('sliquid'),
      item.find('ltail')
    ]
  )
)