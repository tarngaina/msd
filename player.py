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
    self.hp = 100
    self.max_hp = 100
    self.meso = 0
    self.xp = 0
    self.lv = 1
    self.att = 10
    self.str = 5
    self.dex = 5
    self.int = 5
    self.luk = 5
    self.free_stat_point = 0
    self.job = job.jobs[0]
    self.area = area.areas[0]
    self.inventory = {
      'equip':[],
      'consume':{},
      'etc':{}
    }
    self.cd = {'farm':datetime.datetime.min}

  def to_dict(self):
    dic = {}
    dic['hp'] = self.hp
    dic['max_hp'] = self.max_hp
    dic['meso'] = self.meso
    dic['xp'] = self.xp
    dic['lv'] = self.lv
    dic['str'] = self.str
    dic['dex'] = self.dex
    dic['int'] = self.int
    dic['luk'] = self.luk
    dic['free_stat_point'] = self.free_stat_point
    dic['job'] = self.job.name
    dic['area'] = self.area.id
    dic['inventory'] = self.inventory_to_dict()
    return dic

  def from_dict(self, dic):
    self.hp = dic['hp']
    self.max_hp = dic['max_hp']
    self.meso = dic['meso']
    self.xp = dic['xp']
    self.lv = dic['lv']
    self.str = dic['str']
    self.dex = dic['dex']
    self.int = dic['int']
    self.luk = dic['luk']
    self.free_stat_point = dic['free_stat_point']
    self.job = job.find(dic['job'])
    self.area = area.find(dic['area'])
    self.inventory_from_dict(dic['inventory'])

  def inventory_to_dict(self):
    dic = {}
    dic['etc'] = self.inventory['etc']
    dic['consume'] = self.inventory['consume']
    dic['equip'] = []
    for i in self.inventory['equip']:
      dic['equip'].append(i.name)
    return dic
      
  def inventory_from_dict(self, dic):
    self.inventory['etc'] = dic['etc']
    self.inventory['consume'] = dic['consume']
    for name in dic['equip']:
      i = item.find(name)
      self.inventory['equip'].append(i)
    
  def find_equip(self, id):
    id = int(id[5:])
    return self.inventory['equip'][id]

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

  def get_att(self):
    att = self.att + (self.get_main_stat() / 4.0) + (self.get_sub_stat() / 16.0)
    att += att * self.lv / 10
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
    self.att += self.job.job_grade * 5

  def get_hit(self, hp):
    self.hp -= hp
    if self.hp <= 0:
      self.die()
      return True
    return False
      
  def die(self):
    self.xp -= self.xp * 18 / 100
    self.xp = int(self.xp)
    if self.xp < constant.TableExp[self.lv]:
      self.xp = constant.TableExp[self.lv]
    self.hp = self.max_hp

  def get_xp_percent(self):
    xp_last_lv = constant.TableExp[self.lv-1]
    xp_earned = self.xp - xp_last_lv
    xp_total = constant.TableExp[self.lv] - xp_last_lv
    return xp_earned / xp_total * 100
