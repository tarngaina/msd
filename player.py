import datetime
import job, item, constant, pref, area

players = []

def find(id):
  for p in players:
    if p.id == id:
      return p
  p = pref.load(id)
  return p
	
def add(p):
  players.append(p)

class Player():
  def __init__(self, id):
    self.id = id
    self.meso = 0
    self.xp = 0
    self.lv = 1
    self.hp = 100
    self.max_hp = 100
    self.att = 10
    self.str = 5
    self.dex = 5
    self.int = 5
    self.luk = 5
    self.free_stat_point = 0
    self.skill_att = 0
    self.skill_stat = 0
    self.skill_attack = 0
    self.skill_buff = 0
    self.skill_iframe = 0
    self.free_skill_point = 0
    self.job = job.jobs[0]
    self.area = area.areas[0]
    self.inventory = {
      'equip':[],
      'consume':{},
      'etc':{}
    }
    self.weapon = None
    self.hat = None
    self.top = None
    self.bottom = None
    self.cape = None
    self.glove = None
    self.shoe = None
    self.shoulder = None
    self.cd = {'farm':datetime.datetime.min}

  def to_dict(self):
    dic = {}
    dic['hp'] = self.hp
    dic['max_hp'] = self.max_hp
    dic['meso'] = self.meso
    dic['xp'] = self.xp
    dic['lv'] = self.lv
    dic['att'] = self.att
    dic['str'] = self.str
    dic['dex'] = self.dex
    dic['int'] = self.int
    dic['luk'] = self.luk
    dic['free_stat_point'] = self.free_stat_point
    dic['skill_att'] = self.skill_att
    dic['skill_stat'] = self.skill_stat
    dic['skill_attack'] = self.skill_attack
    dic['skill_buff'] = self.skill_buff
    dic['skill_iframe'] = self.skill_iframe
    dic['free_skill_point'] = self.free_skill_point
    dic['job'] = self.job.name
    dic['area'] = self.area.id
    dic['inventory'] = self.inventory_to_dict()
    dic['equip'] = self.equip_to_dict()
    return dic

  def from_dict(self, dic):
    self.hp = dic['hp']
    self.max_hp = dic['max_hp']
    self.meso = dic['meso']
    self.xp = dic['xp']
    self.lv = dic['lv']
    self.att = dic['att']
    self.str = dic['str']
    self.dex = dic['dex']
    self.int = dic['int']
    self.luk = dic['luk']
    self.free_stat_point = dic['free_stat_point']
    self.skill_att = dic['skill_att']
    self.skill_stat = dic['skill_stat']
    self.skill_attack = dic['skill_attack']
    self.skill_buff = dic['skill_buff']
    self.skill_iframe = dic['skill_iframe']
    self.free_skill_point = dic['free_skill_point']
    self.job = job.find(dic['job'])
    self.area = area.find(dic['area'])
    self.inventory_from_dict(dic['inventory'])
    self.equip_from_dict(dic['equip'])
    
  def inventory_to_dict(self):
    dic = {}
    dic['etc'] = self.inventory['etc']
    dic['consume'] = self.inventory['consume']
    dic['equip'] = []
    for i in self.inventory['equip']:
      dic['equip'].append(i.to_dict())
    return dic
      
  def inventory_from_dict(self, dic):
    self.inventory['etc'] = dic['etc']
    self.inventory['consume'] = dic['consume']
    for d in dic['equip']:
      self.inventory['equip'].append(item.from_dict(d))
  
  def equip_to_dict(self):
    dic = {}
    if self.weapon != None:
      dic['weapon'] = self.weapon.to_dict()
    if self.hat != None:
      dic['hat'] = self.hat.to_dict()
    if self.top != None:
      dic['top'] = self.top.to_dict()
    if self.bottom != None:
      dic['bottom'] = self.bottom.to_dict()
    if self.shoe != None:
      dic['shoe'] = self.shoe.to_dict()
    if self.glove != None:
      dic['glove'] = self.glove.to_dict()
    if self.cape != None:
      dic['cape'] = self.cape.to_dict()
    if self.shoulder != None:
      dic['shoulder'] = self.shoulder.to_dict()
    return dic
    
  def equip_from_dict(self, dic):
    if 'weapon' in dic:
      self.weapon = item.from_dict(dic['weapon'])
    if 'hat' in dic:
      self.hat = item.from_dict(dic['hat'])
    if 'top' in dic:
      self.top = item.from_dict(dic['top'])
    if 'bottom' in dic:
      self.bottom = item.from_dict(dic['bottom'])
    if 'shoe' in dic:
      self.shoe = item.from_dict(dic['shoe'])
    if 'cape' in dic:
      self.cape = item.from_dict(dic['cape'])
    if 'glove' in dic:
      self.glove = item.from_dict(dic['glove'])
    if 'shoulder' in dic:
      self.shoulder = item.from_dict(dic['shoulder'])
  
  def find_equip(self, id):
    for i in self.inventory['equip']:
      if i.name.lower() == id.lower():
        return i
    if id.startswith('equip'):
      id = int(id[5:])
      return self.inventory['equip'][id]
    return None

  def get_main_stat(self):
    if self.job.main_stat == 'str':
      return self.str
    if self.job.main_stat == 'dex':
      return self.dex
    if self.job.main_stat == 'int':
      return self.int
    return self.luk

  def get_sub_stat(self):
    if self.job.sub_stat == 'str':
      return self.str
    if self.job.sub_stat == 'dex':
      return self.dex
    if self.job.sub_stat == 'int':
      return self.int
    return self.luk

  def set_stat(self, stat_name, point):
    if stat_name == 'str':
      self.str += point
    if stat_name == 'dex':
      self.dex += point
    if stat_name == 'int':
      self.int += point
    if stat_name == 'luk':
      self.luk += point
      
  def set_skill(self, s, point):
    if s.type == constant.SkillType.att:
      self.skill_att += point
      self.att += point * 2
    elif s.type == constant.SkillType.stat:
      self.skill_stat += point
      self.set_stat(self.job.main_stat, point * 5)
      self.set_stat(self.job.sub_stat, point * 2)
    elif s.type == constant.SkillType.attack:
      self.skill_attack += point
    elif s.type == constant.SkillType.buff:
      self.skill_buff += point
    else:
      self.skill_iframe += point
    self.free_skill_point -= point

  def get_att(self):
    att = self.att + (self.get_main_stat() / 4.0) + (self.get_sub_stat() / 16.0)
    att += self.att * self.lv / 100
    att = int(att)
    return att
    
  def gain_meso(self, meso):
    self.meso += meso
	  
  def gain_xp(self, xp):
    self.xp += xp
    flag = self.xp >= constant.TableExp[self.lv]
    while self.xp >= constant.TableExp[self.lv]:
      self.level_up()
    return flag
      
  def level_up(self):
    self.lv += 1
    self.max_hp += 50
    self.hp = self.max_hp
    self.free_stat_point += 5
    self.free_skill_point += 3

  def gain_item(self, item, number):
    if item.type == constant.ItemType.etc:
      if item.id not in self.inventory['etc']:
        self.inventory['etc'][item.id] = 0
      self.inventory['etc'][item.id] += number
    elif item.type == constant.ItemType.consume:
      if item.id not in self.inventory['consume']:
        self.inventory['consume'][item.id] = 0
      self.inventory['consume'][item.id] += number
    else:
      self.inventory['equip'].append(item)
    
  def gain_job(self, job):
    self.job = job
    self.free_stat_point += 10
    self.hp += 100
    self.att += 10
    self.skill_att = 1
    self.skill_stat = 1
    self.skill_attack = 1
    self.skill_buff = 1
    self.skill_iframe = 1

  def get_hit(self, hp):
    self.hp -= hp
    if self.hp <= 0:
      self.die()
      return True
    return False
      
  def die(self):
    self.xp -= self.xp * 36 / 100
    self.xp = int(self.xp)
    if self.xp < constant.TableExp[self.lv]:
      self.xp = constant.TableExp[self.lv]
    self.hp = self.max_hp

  def get_xp_percent(self):
    xp_last_lv = constant.TableExp[self.lv-1]
    xp_earned = self.xp - xp_last_lv
    xp_total = constant.TableExp[self.lv] - xp_last_lv
    return xp_earned / xp_total * 100

  def equip_item(self, item):
    if item.equip_type == constant.EquipType.weapon:
      self.remove_item(self.weapon)
      self.weapon = item
      self.apply_item(self.weapon)
    elif item.equip_type == constant.EquipType.hat:
      self.remove_item(self.hat)
      self.hat = item
      self.apply_item(self.hat)
    elif item.equip_type == constant.EquipType.overall:
      self.remove_item(self.top)
      self.top = item
      self.apply_item(self.top)
      self.remove_item(self.bottom)
      self.bottom = None
    elif item.equip_type == constant.EquipType.top:
      self.remove_item(self.top)
      self.top = item
      self.apply_item(self.top)
    elif item.equip_type == constant.EquipType.bottom:
      self.remove_item(self.bottom)
      self.bottom = item
      self.apply_item(self.bottom)
    elif item.equip_type == constant.EquipType.cape:
      self.remove_item(self.cape)
      self.cape = item
      self.apply_item(self.cape)
    elif item.equip_type == constant.EquipType.shoe:
      self.remove_item(self.shoe)
      self.shoe = item
      self.apply_item(self.shoe)
    elif item.equip_type == constant.EquipType.glove:
      self.remove_item(self.glove)
      self.glove = item
      self.apply_item(self.glove)
    elif item.equip_type == constant.EquipType.shoulder:
      self.remove_item(self.shoulder)
      self.shoulder = item
      self.apply_item(self.shoulder)
      
  def remove_item(self, item):
    if item != None:
      dic = vars(item)
      if 'hp' in dic:
        self.max_hp -= dic['hp']
      if 'att' in dic:
        self.att -= dic['att']
      if 'str' in dic:
        self.str -= dic['str']
      if 'dex' in dic:
        self.dex -= dic['dex']
      if 'int' in dic:
        self.int -= dic['int']
      if 'luk' in dic:
        self.luk -= dic['luk']
      self.inventory['equip'].append(item)

  def apply_item(self, item):
    dic = vars(item)
    if 'hp' in dic:
      self.max_hp += dic['hp']
    if 'att' in dic:
      self.att += dic['att']
    if 'str' in dic:
      self.str += dic['str']
    if 'dex' in dic:
      self.dex += dic['dex']
    if 'int' in dic:
      self.int += dic['int']
    if 'luk' in dic:
      self.luk += dic['luk']
    self.inventory['equip'].remove(item)
    
    
  def get_xp_bar_texture(self):
    percent = self.get_xp_percent()
    percent = int(percent)
    green = percent // 10
    white = 10 - green
    bar = constant.Texture.green_square * green + constant.Texture.white_square * white
    return bar
  
  def get_hp_bar_texture(self):
    percent = self.hp / self.max_hp * 100
    percent = int(percent)
    red = percent // 10
    white = 10 - red
    bar = constant.Texture.red_square * red + constant.Texture.white_square * white
    return bar