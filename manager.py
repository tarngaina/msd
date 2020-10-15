import random, datetime
import constant, item, area

def check_cd(p, key):
  now = datetime.datetime.now()
  sec = (now - p.cd[key]).total_seconds()
  if sec > constant.CDs[key]:
    p.cd[key] = now
    return True, 0
  return False, int(constant.CDs[key] - sec)

def farm(p):
  if not p.area.is_town:
    hp_lost = get_hp_lost(p.get_att(), p.area.mob_att, p.area.mob_hp)
    i = item.nothing()
    num = 0
    lvup = False
    meso = p.area.meso
    meso += meso * random.randint(1, 20) / 100
    meso = int(meso)
    xp = p.area.xp * p.area.xp_rate
    xp += xp * random.randint(1, 100) / 100
    xp = int(xp)
    die = p.get_hit(hp_lost)
    if not die:
      p.gain_meso(meso) 
      lvup = p.gain_xp(xp)
      if random.randint(0, 100) > 15:
        i = p.area.random_item()
        num = random.randint(1, 5)
        p.gain_item(i.id, num)
    return True, meso, xp, lvup, i, num, hp_lost, die
  else:
    return False, 'dumbass, go to hunting maps first, type msd map list', '', '', '', '', '',''

def go_to_area(p, id):
  if id != p.area.id and id != p.area.name:
    a = area.find(id)
    if a == None:
      a = area.find_name(id)
    if a != None:
      p.area = a
      return True, a.name
    else:
      return False, 'cannot find that map'
  else:
    return False, 'already in dat map'
  
def advance_job(p, job):
  if p.joblv == 0:
    if job in constant.Job.jobs:
      if p.lvl > 9:
        if p.job == 'beginner':
          p.gain_job(job, 1)
          return True, job
        else:
          return False, 'you already in job'
      else:
        return False, 'not enough lvl'
    else:
      return False, 'wrong type job'
      
def get_hp_lost(att, mob_att, mob_hp):
  if att >= int(mob_hp * 1.5):
    return 0
  if att >= mob_hp:
    return 1
  hp_lost = mob_att
  hp_lost += hp_lost * random.randint(1, 100) / 100
  hp_lost = int(hp_lost)
  return hp_lost
  
   