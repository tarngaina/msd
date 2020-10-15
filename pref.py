import os.path
import player, area


def save(id):
  p = player.find(id)
  if p != None:
    f = open(f'data/{p.id}', 'w+')

    s = f'{p.hp} {p.max_hp} {p.lvl} {p.xp} {p.meso}\n'
    f.write(s)

    s = f'{p.job} {p.joblv} {p.stat["str"]} {p.stat["dex"]} {p.stat["int"]} {p.stat["luk"]} {p.main_stat} {p.stat_point}\n'
    f.write(s)

    s = f'{p.meso} {len(p.inventory)}\n'
    f.write(s)
    for id in p.inventory:
      f.write(f'{id} {p.inventory[id]}\n')

    s = f'{p.area.id}\n'
    f.write(s)

    f.close()


def load(id):
  f = None
  if not os.path.isfile(f'data/{id}'):
    f = open(f'data/{id}', 'w+')
  else:
    f = open(f'data/{id}', 'r')
  lines = f.readlines()
  p = player.Player(id)
  if len(lines) > 0:

    l = lines[0][:-1].split(' ')
    p.hp = int(l[0])
    p.max_hp = int(l[1])
    p.lvl = int(l[2])
    p.xp = int(l[3])
    lines = lines[1:]

    l = lines[0][:-1].split(' ')
    p.job = l[0]
    p.joblv = int(l[1])
    p.stat['str'] = int(l[2])
    p.stat['dex'] = int(l[3])
    p.stat['int'] = int(l[4])
    p.stat['luk'] = int(l[5])
    p.main_stat = l[6]
    p.stat_point = int(l[7])
    lines = lines[1:]

    l = lines[0][:-1].split(' ')
    p.meso = int(l[0])
    inventory_length = int(l[1])
    lines = lines[1:]
    i = 0
    while i < inventory_length:
      l = lines[i].split(' ')
      p.inventory[l[0]] = int(l[1])
      i += 1
    
    lines = lines[inventory_length:]
    l = lines[0][:-1].split(' ')
    p.area = area.find(l[0])
    
  f.close()
  player.add(p)
  save(id)
  return p
