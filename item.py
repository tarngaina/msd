import constant

items = []

def add(i):
  items.append(i)

def find_id(id):
  for i in items:
    if id == i.id:
      return i
  return None
  
def find_name(name):
  for i in items:
    if name.lower() == i.name.lower():
      return i
  return None

def find(id):
  i = find_id(id)
  if i == None:
    i = find_name(id)
  return i
  
def from_dict(dic):
  i = find(dic['name'])
  return i


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
      self.equip_type = dic['equip_type']
      if 'weapon_type' in dic:
        self.weapon_type = dic['weapon_type']
      if 'hp' in dic:
        self.hp = dic['hp']
      if 'att' in dic:
        self.att = dic['att']
      if 'str' in dic:
        self.str = dic['str']
      if 'dex' in dic:
        self.dex = dic['dex']
      if 'int' in dic:
        self.int = dic['int']
      if 'luk' in dic:
        self.luk = dic['luk']
        
  def to_dict(self):
    dic = {}
    dic['name'] = self.name
    return dic
    
  def get_name(self):
    return self.name

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
    id = '',
    name = 'burning sword',
    type = constant.ItemType.equip,
    price = 1,
    equip_type = constant.EquipType.weapon,
    weapon_type = constant.WeaponType.sword,
    lv = 10,
    att = 10,
    str = 5,
    dex = 5,
    hp = 100
  )
)
add(
  Item(
    id = '',
    name = 'burning axe',
    type = constant.ItemType.equip,
    price = 1,
    equip_type = constant.EquipType.weapon,
    weapon_type = constant.WeaponType.axe,
    lv = 10,
    att = 10,
    str = 5,
    dex = 5,
    hp = 100
  )
)
add(
  Item(
    id = '',
    name = 'burning spear',
    type = constant.ItemType.equip,
    price = 1,
    equip_type = constant.EquipType.weapon,
    weapon_type = constant.WeaponType.spear,
    lv = 10,
    att = 10,
    str = 5,
    dex = 5,
    hp = 100
  )
)
add(
  Item(
    id = '',
    name = 'burning bow',
    type = constant.ItemType.equip,
    price = 1,
    equip_type = constant.EquipType.weapon,
    weapon_type = constant.WeaponType.bow,
    lv = 10,
    att = 10,
    str = 5,
    dex = 5,
    hp = 100
  )
)
add(
  Item(
    id = '',
    name = 'burning crossbow',
    type = constant.ItemType.equip,
    price = 280,
    equip_type = constant.EquipType.weapon,
    weapon_type = constant.WeaponType.crossbow,
    lv = 10,
    att = 10,
    str = 5,
    dex = 5,
    hp = 100
  )
)
add(
  Item(
    id = '',
    name = 'burning staff',
    type = constant.ItemType.equip,
    price = 1,
    equip_type = constant.EquipType.weapon,
    weapon_type = constant.WeaponType.staff,
    lv = 10,
    att = 10,
    int = 5,
    luk = 5,
    hp = 100
  )
)
add(
  Item(
    id = '',
    name = 'burning wand',
    type = constant.ItemType.equip,
    price = 1,
    equip_type = constant.EquipType.weapon,
    weapon_type = constant.WeaponType.wand,
    lv = 10,
    att = 10,
    int = 5,
    luk = 5,
    hp = 100
  )
)
add(
  Item(
    id = '',
    name = 'burning claw',
    type = constant.ItemType.equip,
    price = 1,
    equip_type = constant.EquipType.weapon,
    weapon_type = constant.WeaponType.claw,
    lv = 10,
    att = 10,
    luk = 5,
    dex = 5,
    hp = 100
  )
)
add(
  Item(
    id = '',
    name = 'burning dagger',
    type = constant.ItemType.equip,
    price = 1,
    equip_type = constant.EquipType.weapon,
    weapon_type = constant.WeaponType.dagger,
    lv = 10,
    att = 10,
    luk = 5,
    dex = 5,
    hp = 100
  )
)
add(
  Item(
    id = '',
    name = 'burning knuckle',
    type = constant.ItemType.equip,
    price = 1,
    equip_type = constant.EquipType.weapon,
    weapon_type = constant.WeaponType.knuckle,
    lv = 10,
    att = 10,
    str = 5,
    dex = 5,
    hp = 100
  )
)
add(
  Item(
    id = '',
    name = 'burning gun',
    type = constant.ItemType.equip,
    price = 1,
    equip_type = constant.EquipType.weapon,
    weapon_type = constant.WeaponType.gun,
    lv = 10,
    att = 10,
    str = 5,
    dex = 5,
    hp = 100
  )
)
add(
  Item(
    id = '',
    name = 'Frozen Hat',
    type = constant.ItemType.equip,
    price = 1,
    equip_type = constant.EquipType.hat,
    lv = 10,
    att = 2,
    str = 10,
    dex = 10,
    int = 10,
    luk = 10,
    hp = 100
  )
)
add(
  Item(
    id = '',
    name = 'Frozen Suit',
    type = constant.ItemType.equip,
    price = 1,
    equip_type = constant.EquipType.overall,
    lv = 10,
    att = 2,
    str = 10,
    dex = 10,
    int = 10,
    luk = 10,
    hp = 100,
  )
)
add(
  Item(
    id = '',
    name = 'Frozen Cape',
    type = constant.ItemType.equip,
    price = 1,
    equip_type = constant.EquipType.cape,
    lv = 10,
    att = 2,
    str = 10,
    dex = 10,
    int = 10,
    luk = 10,
    hp = 100
  )
)
def get_frozen_set():
  s = []
  for i in items:
    if i.name.lower().startswith('frozen'):
      s.append(i)
  return s