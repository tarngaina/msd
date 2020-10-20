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
    hp = get_hp_lost(p, p.area)
    die = p.get_hit(hp)
    if not die:
      s += f'you lost {hp}hp: {p.hp}/{p.max_hp}\n'
      meso = p.area.meso
      meso += meso * random.randint(1, 50) / 100
      meso = int(meso)
      xp = p.area.xp * p.area.xp_rate * get_xp_rate_by_level(p, a)
      xp += xp * random.randint(1, random.randint(1, 100)) / 100
      xp = int(xp)
      p.gain_meso(meso) 
      lvup = p.gain_xp(xp)
      s += (
        f'you get {meso}meso\n'
        f'you get {xp}xp: {p.get_xp_percent():.2f}%'
        )
      if lvup:
        s += f'\ngratz, you level up to {p.lv}'
      if random.randint(0, 100) > 15:
        i = p.area.random_item()
        num = random.randint(1, 5)
        p.gain_item(i, num)
        s += f'\nand you get {num} {i.name}'
      return True, s
    else:
      return False, f'you lost {hp} and died'
  else:
    return False, 'dumbass, go to hunting maps first, type msd map list'

def advance_job(p, id):
  j = job.find(id)
  if j != None:
    if p.job.name == j.previous:
      if p.lv >= j.lv:
        p.gain_job(j)
        return True, f'you became {p.job.name}'
      else:
        return False, f'not enough level, you need to reach lv{j.lv}'
    else:
      return False, f'cant advance to {j.name} from {p.job.name}'
  else:
    return False, f'there is no job named that, type msd job list for list of jobs'
      
def get_hp_lost(p, a):
  if p.att >= a.hp * 4:
    return 1
  hp_lost = a.att * random.randint(80, 120) / 100
  if a.lv < p.lv+2:
    hp_lost += hp_lost * random.randint(1, 100) / 100
  hp_lost = int(hp_lost)
  return hp_lost
  
def get_xp_rate_by_level(p, a):
  if p.lv <= a.lv - 8:
    return 0.8
  if p.lv <= a.lv - 4:
    return 0.95
  if p.lv == a.lv:
    return 1.05
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
