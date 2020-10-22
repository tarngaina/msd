import os.path
import player, area
import json

def save(id):
  p = player.find(id)
  path = f'data/{id}.json'
  if p != None:
    f = open(path, 'w+')
    json.dump(p.to_dict(), f)
    f.close()


def load(id):
  p = player.Player(id)
  path = f'data/{id}.json'
  if not os.path.isfile(path):
    f = open(path, 'w+')
    json.dump(p.to_dict(), f)
    f.close()
  else:
    f = open(path, 'r')
    p.from_dict(json.load(f))
    f.close()
  player.add(p)
  return p
