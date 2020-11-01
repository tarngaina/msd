import random, datetime
import constant, item, area, job

def check_cd(p, key):
  now = datetime.datetime.now()
  sec = (now - p.cd[key]).total_seconds()
  if sec > constant.CDs[key]:
    p.cd[key] = now
    return True, ''
  return False, f' need to wait more {int(constant.CDs[key] - sec)}s to go {key} again.'

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
  return xp * 100
  
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
  bonus_hp_lost = 0
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
  cd, msg = check_cd(p, 'farm')
  if not cd:
    return False, msg
  if not p.area.is_safe:
    s = f' has farmed around {p.area.get_name()}\n'
    hp = get_hp_lost_on_farm(p)
    die = p.get_hit(hp)
    if not die:
      s += f'Lost {hp} HP, remaining HP: {p.hp}/{p.max_hp}\n'
      meso = get_meso_on_farm(p)
      xp = get_xp_on_farm(p)
      p.gain_meso(meso) 
      lvup = p.gain_xp(xp)
      s += (
        f'Got: {meso:,.0f} {constant.Texture.meso}\n'
        f'Got: {xp:,.0f} XP'
        )
      if lvup:
        s += f'\nLevel up to {p.lv}'
      chance, i, number = get_item_on_farm(p)
      if chance:
        p.gain_item(i, number)
        s += f'\nAnd got {number} {i.get_name()}.'
      return True, s
    else:
      return False, f' lost {hp} HP and died.'
  else:
    return False, ', you need to go to hunting maps first, type "msd map list" for list of maps.'

def advance_job(p, param):
  j = job.find(param)
  if j == None:
    return False, ', job not found.'
  if p.lv < 10:
    return False, ' need to reach lv.10 to advance job.'
  if p.job.name != 'beginner':
    return False, ', you have already got a job.'
    
  p.gain_job(j)
  return True, f' became {p.job.get_name()}.'
      
def sell_item(p, id, num):
  i = item.find(id)
  if i == None:
    i = p.find_equip(id)
  if i != None:
    if i.type == constant.ItemType.equip:
      p.inventory['equip'].remove(i)
      p.meso += i.price
      return True, f' sold {i.name} for {i.price}meso'
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
      if i.equip_type == constant.EquipType.weapon:
        if i.weapon_type not in p.job.weapon_types:
          return False, ' you cant equip this weapon, check your job'
      p.equip_item(i)
      return True, f' equipped {i.name}'
    else:
      return False, ' not enough level'
  else:
    return False, ' equip not found'

def go_area(p, param):
  a = area.find(param)
  if a != None:
    p.area = a
    return True, f' moved to {a.get_name()}.'
  else:
    return False, ', map not found.'

def plus_stat_point(p, param):
  param = param.split(' ')
  point = param[-1]
  if not point.isnumeric():
    return False, ', AP number not found.'
  point = int(point)
  stat_name = ' '.join(param[:-1])
  if stat_name not in ['str', 'dex', 'luk', 'int']:
    return False, ', stat not found.'
  if p.job.name.lower() == 'beginner':
    return False, ', Beginner can not use AP.'
  if point > p.free_stat_point:
    return False, ', you don\'t have enough AP.'
  p.set_stat(stat_name,   point)
 
  p.free_stat_point -= point
  return True, f' added {point} AP to {stat_name}.'
  
  
def plus_skill_point(p, param):
  param = param.split(' ')
  point = param[-1]
  if not point.isnumeric():
    return False, ', SP number not found.'
  point = int(point)
  id = ' '.join(param[:-1])
  s = p.job.find_skill(id)
  print(id)
  if s == None:
    return False, ', skill not found.'
  if point > p.free_skill_point:
    return False, ', you don\'t have enough SP.'
  if s.type == constant.SkillType.att and p.skill_att + point > 100:
    return False, ', invalid point, skill can only be maxed out at lv 100.'
  if s.type == constant.SkillType.stat and p.skill_stat + point > 100:
    return False, ', invalid point, skill can only be maxed out at lv 100.'
  if s.type == constant.SkillType.attack and p.skill_attack + point > 100:
    return False, ', invalid point, skill can only be maxed out at lv 100.'
  if s.type == constant.SkillType.buff and p.skill_buff + point > 100:
    return False, ', invalid point, skill can only be maxed out at lv 100.'
  if s.type == constant.SkillType.iframe and p.skill_iframe + point > 100:
    return False, ', invalid point, skill can only be maxed out at lv 100.'
  
  p.set_skill(s, point)
  return True, f' added {point} SP to {s.get_name()}.'