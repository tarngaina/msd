import os.path
import player, area
import json


def save(id):
  p = player.find(id)
  if p != None:
    f = open(f'data/{id}.json', 'w+')
    json.dump(p.to_dict(), f)
    f.close()


def load(id):
  f = None
  if not os.path.isfile(f'data/{id}'):
    f = open(f'data/{id}.json', 'w+')
  else:
    f = open(f'data/{id}.json', 'r')
  p = player.Player(id)
  p.from_dict(json.load(f))
  f.close()
  player.add(p)
  save(id)
  return p
