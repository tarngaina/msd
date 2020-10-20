import random, datetime
import constant, item, area

def check_cd(p, key):
  now = datetime.datetime.now()
  sec = (now - p.cd[key]).total_seconds()
  if sec > constant.CDs[key]:
    p.cd[key] = now
    return True, 0
  return False, f' you need to wait more {int(constant.CDs[key] - sec)}s'

def farm(p):
  if not p.area.is_safe:
    s = f' farmed around {p.area.name}\n'
    hp = get_hp_lost(p.get_att(), p.area.mob_att, p.area.mob_hp)
    die = p.get_hit(hp)
    if not die:
      s += f'you lost {hp}hp: {p.hp}/{p.max_hp}\n'
      meso = p.area.meso
      meso += meso * random.randint(1, 50) / 100
      meso = int(meso)
      xp = p.area.xp * p.area.xp_rate * get_xp_rate_by_level(p.lvl, p.area.lvl)
      xp += xp * random.randint(1, random.randint(1, 100)) / 100
      xp = int(xp)
      p.gain_meso(meso) 
      lvlup = p.gain_xp(xp)
      s += (
        f'you get {meso}meso\n'
        f'you get {xp}xp: {get_xp_percent(p.xp, p.lvl):.2f}%'
        )
      if lvlup:
        s += f'\ngratz, you level up to {p.lvl}'
      if random.randint(0, 100) > 15:
        i = p.area.random_item()
        num = random.randint(1, 5)
        p.gain_item(i.id, num)
        s += f'\nand you get {num} {i.name}'
      return True, s
    else:
      return False, f'you lost {hp} and died'
  else:
    return False, 'dumbass, go to hunting maps first, type msd map list'

  
def advance_job(p, job):
  if p.joblv == 0:
    if job in constant.Job.jobs:
      if p.lvl > 9:
        if p.job == 'beginner':
          p.gain_job(job, 1)
          return True, f'advanced to {job}'
        else:
          return False, 'you already in job'
      else:
        return False, 'not enough lvl'
    else:
      return False, 'wrong type job'
      
def plus_stat_point(p, stat_name, pts):
  if p.joblv > 0:
    if pts <= p.stat_point:
      p.stat[stat_name] += pts
      p.stat_point -= pts
      return True, f'added {pts} to your {stat_name}'
    else:
      return False, 'not enough point'
  else:
    return False, 'beginner cant add point, msd advjob for job advance'
  
def get_hp_lost(att, mob_att, mob_hp):
  if att >= mob_hp * 5:
    return 1
  hp_lost = mob_att * random.randint(90, 110) / 100
  hp_lost += hp_lost * random.randint(1, 100) / 100
  hp_lost = int(hp_lost)
  return hp_lost
  
  
def get_xp_rate_by_level(plvl, alvl):
  if plvl == alvl:
    return 1.1
  if plvl < alvl - 8:
    return 0.8
  if plvl < alvl - 4:
    return 0.95
  return 1.2
  
def sell_item(p, id, num):
  num = int(num)
  if num < 1:
    return False, 'invalid number'
  i = item.find(id)
  if i == None:
    i = item.find_name(id)
  if i != None:
    if i.id in p.inventory:
      if p.inventory[i.id] >= num:
        p.inventory[i.id] -= num
        meso = i.price * num
        p.meso += meso
        if p.inventory[i.id] == 0:
          p.inventory.pop(i.id)
        return True, f'sold {num} {i.name} for {meso}meso'
      else:
        return False, 'you dont have enough number of this item'
    else:
      return False, 'you dont have that item'
  else:
    return False, 'item not found'
    
def equip_item(p, i):
  if i.type == constant.ItemType.equip:
    if p.lvl < i.lvl:
      pass
    else:
      pass
  else:
    return False, 'cannot equip this item'
