import datetime
import job, constant, pref, area

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
    self.str = 5
    self.dex = 5
    self.int = 5
    self.luk = 5
    self.free_stat_point = 0
    self.job = job.jobs[0]
    self.area = area.areas[0]
    self.inventory = {
      'equip':{},
      'consume':{},
      'etc':{}
    }
    self.cd = {'farm':datetime.datetime.min}

  def to_dic(self):
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
    return dic

  def inventory_to_dic(self):
    pass

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

  def get_att(self):
    return self.att + int(self.att * self.lv / 200 * 20 / 100)  + (int(self.get_main_stat() / 4.0) + (self.get_sub_stat() / 16.0) + 1)
      
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
      return
    else:
      return
    
  def gain_job(self, name)
    self.job = job.find_name(name)
    self.free_stat_point += 10

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
