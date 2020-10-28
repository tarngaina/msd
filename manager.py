import random, datetime
import constant, item, area, job

def check_cd(p, key):
  now = datetime.datetime.now()
  sec = (now - p.cd[key]).total_seconds()
  if sec > constant.CDs[key]:
    p.cd[key] = now
    return True, 0
  return False, f' you need to wait more {int(constant.CDs[key] - sec)}s'

def get_xp_on_farm(p):
  gap = p.lv - p.area.lv
  xp = p.area.xp
  bonus_xp = 0
  if gap < -15:
    bonus_xp = xp * random.randint(-65, -30) / 100
  if -15 <= gap < -8:
    bonus_xp = xp * random.randint(-30, -15) / 100
  if -8 <= gap < 0:
    bonus_xp = xp * random.randint(-10, 0) / 100
  if gap >= 0:
    bonus_xp = xp * random.randint(0, 50) / 100
  xp = xp * p.area.xp_rate + bonus_xp
  xp = int(xp)
  return xp
  
def get_meso_on_farm(p):
  gap = p.lv - p.area.lv
  meso = p.area.meso
  bonus_meso = meso * random.randint(0, 30) / 100
  if gap >= 20:
    bonus_meso = meso * random.randint(-100, -50) / 100
  meso = meso + bonus_meso
  meso = int(meso)
  return meso
  
def get_hp_lost_on_farm(p):
  gap = p.lv - p.area.lv
  hp_lost = p.area.att
  if gap < -15:
    bonus_hp_lost = hp_lost * random.randint(70, 400) / 100
  if -15 <= gap < -8:
    bonus_hp_lost = hp_lost * random.randint(30, 100) / 100
  if -8 <= gap < 0:
    bonus_hp_lost = hp_lost * random.randint(0, 60) / 100
  if 0 <= gap < 15:
    bonus_hp_lost = hp_lost * random.randint(-20, 20) / 100
  if gap > 15:
    bonus_hp_lost = hp_lost * random.randint(-99, -20) / 100
  hp_lost = hp_lost + bonus_hp_lost
  hp_lost = int(hp_lost)
  return hp_lost
  

def get_item_on_farm(p):
  i = p.area.random_item()
  if i.type == constant.ItemType.equip:
    if random.randint(0, 100) > 40:
      return True, i, 1
  else:
    if random.randint(0, 100) > 20:
      return True, i, random.randint(1, 21)
  return False, None, 0

def farm(p):
  if not p.area.is_safe:
    s = f' farmed around {p.area.name}\n'
    hp = get_hp_lost_on_farm(p)
    die = p.get_hit(hp)
    if not die:
      s += f'you lost {hp}hp: {p.hp}/{p.max_hp}\n'
      meso = get_meso_on_farm(p)
      xp = get_xp_on_farm(p)
      p.gain_meso(meso) 
      lvup = p.gain_xp(xp)
      s += (
        f'you get {meso}meso\n'
        f'you get {xp}xp: {p.get_xp_percent():.2f}%'
        )
      if lvup:
        s += f'\ngratz, you level up to {p.lv}'
      chance, i, number = get_item_on_farm(p)
      if chance:
        p.gain_item(i, number)
        s += f'\nand you get {number} {i.name}'
      return True, s
    else:
      return False, f' lost {hp} and died'
  else:
    return False, ' dumbass, go to hunting maps first, type msd map list'

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
      
      
def sell_item(p, id, num):
  num = int(num)
  i = item.find(id)
  if i == None:
    i = p.find_equip(id)
  if i != None:
    if i.type == constant.ItemType.equip:
      p.inventory['equip'].remove(i)
      p.meso += i.price
      return True, f' you sold {i.name} for {i.price}meso'
    elif i.type == constant.ItemType.consume:
      if p.inventory['consume'][i.id] <= num:
        p.inventory['consume'][i.id] -= num
        meso = i.price * num
        p.meso += meso
        if p.inventory['consume'][i.id] == 0:
          p.inventory['consume'].pop(i.id)
        return True, f' you sold {num} {i.name} for {meso}meso'
      else:
        return False, f' you dont have {num} of {i.name}'
    else:
      if p.inventory['etc'][i.id] <= num:
        p.inventory['etc'][i.id] -= num
        meso = i.price * num
        p.meso += meso
        if p.inventory['etc'][i.id] == 0:
          p.inventory['etc'].pop(i.id)
        return True, f' you sold {num} {i.name} for {meso}meso'
      else:
        return False, f' you dont have {num} of {i.name}'
  else:
    return False, ' item not found'
    
def equip_item(p, id):
  i = p.find_equip(id)
  if i != None:
    if p.lv >= i.lv:
      if i.type == constant.EquipType.weapon:
        if not i.weapon_type in p.job.weapon_types:
          return False, ' you cant equip this weapon'
      p.equip_item(i)
      return True, f' equipped {i.name}'
    else:
      return False, ' not enough level'
  else:
    return False, ' equip not found'

def go_area(p, id):
  a = area.find(id)
  if a != None:
    p.area = a
    return True, f'moved to {a.name}'
  else:
    return False, 'cannot find that map'

def plus_stat_point(p, stat_name, point):
  if p.job.name != 'beginner':
    if point <= p.free_stat_point:
      p.set_stat(stat_name, point)
      p.free_stat_point -= point
      return True, f'added {point} to your {stat_name}'
    else:
      return False, 'not enough point'
  else:
    return False, 'beginner cant add point, msd advance for job advance'
  

