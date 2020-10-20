import constant

items = []

def add(i):
  items.append(i)

def find(id):
  for item in items:
    if id == item.id:
      return item
  return None
  
def find_name(name):
  for item in items:
    if name == item.name:
      return item
  return None

class Item:
  def __init__(self, id, name, type, price, **dic):
    self.id = id
    self.name = name
    self.type = type
    self.price = price
    if type == constant.ItemType.consume:
      if 'hp' in dic:
        self.hp = dic['hp']
    if type == constant.ItemType.equip:
      self.lv = dic['lv']
      if 'hp' in dic:
        self.hp = dic['hp']
      if 'att' in dic:
        self.att = dic['att']

add(
  Item(
    id = 'mcap',
    name = 'mushroom cap',
    type = constant.ItemType.etc,
    price = 100
  )
)
add(
  Item(
    id = 'snail',
    name = 'snail',
    type = constant.ItemType.etc,
    price = 35
  )
)
add(
  Item(
    id = 'sliquid',
    name = 'slime liquid',
    type = constant.ItemType.etc,
    price = 60
  )
)
add(
  Item(
    id = 'ltail',
    name = 'lizard tail',
    type = constant.ItemType.etc,
    price = 120
  )
)
add(
  Item(
    id = 'bwing',
    name = 'bat wing',
    type = constant.ItemType.etc,
    price = 150
  )
)
add(
  Item(
    id = 'lskin',
    name = 'ligator skin',
    type = constant.ItemType.etc,
    price = 230
  )
)
add(
  Item(
    id = 'ribbon',
    name = 'pig ribbon',
    type = constant.ItemType.etc,
    price = 180
  )
)
add(
  Item(
    id = 'starfish',
    name = 'starfish',
    type = constant.ItemType.etc,
    price = 280
  )
)


add(
  Item(
    id = 'wpot',
    name = 'white potion',
    type = constant.ItemType.consume,
    price = 300,
    hp = 300
  )
)


add(
  Item(
    id = 'sw',
    name = 'sword',
    type = constant.ItemType.equip,
    price = 280,
    lv = 1,
    att = 5,
    hp = 100
  )
)
