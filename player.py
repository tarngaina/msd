import datetime
import constant, pref, area

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
    self.lvl = 1
    self.stat = {}
    self.stat['str'] = 5
    self.stat['dex'] = 5
    self.stat['int'] = 5
    self.stat['luk'] = 5
    self.main_stat = 'str'
    self.stat_point = 0
    self.job = 'beginner'
    self.joblv = 0
    self.inventory = {}
    self.area = area.areas[0]
    self.cd = {'farm':datetime.datetime.min}

    
  def get_att(self):
    return 10 + self.lvl * (int(self.stat[self.main_stat] / 10.0)+1)
      
  def gain_meso(self, meso):
    self.meso += meso
	  
  def gain_xp(self, xp):
    self.xp += xp
    flag = self.xp >= constant.TableExp[self.lvl]
    while self.xp >= constant.TableExp[self.lvl]:
      self.level_up()
    return flag
      
  def level_up(self):
    self.lvl += 1
    self.max_hp += 50
    self.hp = self.max_hp
    self.stat_point += 5

  def gain_item(self, id, number):
    if id not in self.inventory:
      self.inventory[id] = 0
    self.inventory[id] += number
    
  def gain_job(self, job, joblv):
    self.joblv = joblv
    self.job = job
    self.main_stat = constant.Job.main_stat[job]
    self.stat[self.main_stat] += 10

  def get_hit(self, hp):
    self.hp -= hp
    if self.hp <= 0:
      self.die()
      return True
    return False
      
  def die(self):
    self.xp -= self.xp * 16 / 100
    self.xp = int(self.xp)
    if self.xp < 0:
      self.xp = 0
    if self.xp < constant.TableExp[self.lvl]:
      self.xp = constant.TableExp[self.lvl]
    self.hp = self.max_hp