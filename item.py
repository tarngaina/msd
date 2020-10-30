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
  def __init__(self, id, name, type, price, texture = None, **dic):
    self.id = id
    self.name = name
    self.type = type
    self.price = price
    self.texture = texture
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
    s = ''
    if self.texture != None:
      s += self.texture + ' '
    s = s + f'**{self.name}**'
    return s

add(
  Item(
    id = 'mcap',
    name = 'Mushroom Cap',
    type = constant.ItemType.etc,
    price = 100,
    texture = '<:mcap:771002172686073886>'
  )
)
add(
  Item(
    id = 'snail',
    name = 'Snail Shell',
    type = constant.ItemType.etc,
    price = 35,
    texture = '<:snail:771002198632038410>'
  )
)
add(
  Item(
    id = 'sliquid',
    name = 'Slime Liquid',
    type = constant.ItemType.etc,
    price = 60,
    texture = '<:sliquid:771002214725976120>'
  )
)
add(
  Item(
    id = 'pribbon',
    name = 'Pig Ribbon',
    type = constant.ItemType.etc,
    price = 180,
    texture = '<:pribbon:771002230433120266>'
  )
)
def get_victoria_island_etc():
  i = []
  i.append(find('mcap'))
  i.append(find('snail'))
  i.append(find('sliquid'))
  i.append(find('pribbon'))
  return i

add(
  Item(
    id = 'hppot',
    name = 'Power Elixir',
    type = constant.ItemType.consume,
    price = 2500
  )
)
  
add(
  Item(
    id = '',
    name = 'Frozen Sword',
    type = constant.ItemType.equip,
    price = 1,
    texture = '<:frozen_sword:771174925817348096>',
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
    name = 'Frozen Axe',
    type = constant.ItemType.equip,
    price = 1,
    texture = '<:frozen_axe:771174942623531008>',
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
    name = 'Frozen Spear',
    type = constant.ItemType.equip,
    price = 1,
    texture = '<:frozen_spear:771174955958272038>',
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
    name = 'Frozen Longbow',
    type = constant.ItemType.equip,
    price = 1,
    texture = '<:frozen_bow:771174969731448832>',
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
    name = 'Frozen Crossbow',
    type = constant.ItemType.equip,
    price = 280,
    texture = '<:frozen_crossbow:771174978280357938>',
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
    name = 'Frozen Staff',
    type = constant.ItemType.equip,
    price = 1,
    texture = '<:frozen_staff:771175033371623446>',
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
    name = 'Frozen Wand',
    type = constant.ItemType.equip,
    price = 1,
    texture = '<:frozen_wand:771175021321650186>',
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
    name = 'Frozen Steer',
    type = constant.ItemType.equip,
    price = 1,
    texture = '<:frozen_steer:771175066314473482>',
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
    name = 'Frozen Cutter',
    type = constant.ItemType.equip,
    price = 1,
    texture = '<:frozen_cutter:771175059519832095>',
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
    name = 'Frozen Grip',
    type = constant.ItemType.equip,
    price = 1,
    texture = '<:frozen_grip:771175075675897876>',
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
    name = 'Frozen Shooter',
    type = constant.ItemType.equip,
    price = 1,
    texture = '<:frozen_shooter:771175093443362836>',
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
    texture = '<:frozen_hat:771174880808796170>',
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
    texture = '<:frozen_suit:771174893710344252>',
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
    texture = '<:frozen_cape:771174907182186548>',
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