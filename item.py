import random
import constant

items = []

def add(i):
  items.append(i)

def nothing():
  return items[0]

def find(id):
  for item in items:
    if id == item.id:
      return item
  return nothing()

class Item:
  def __init__(self, id, name, type, price):
    self.id = id
    self.name = name
    self.type = type
    self.price = price

add(
  Item(
    id = 'mcap',
    name = 'mushroom cap',
    type = constant.ItemType.etc,
    price = 100
  )
)
add(
  Item(
    id = 'snail',
    name = 'snail',
    type = constant.ItemType.etc,
    price = 35
  )
)
add(
  Item(
    id = 'sliquid',
    name = 'slime liquid',
    type = constant.ItemType.etc,
    price = 60
  )
)
add(
  Item(
    id = 'ltail',
    name = 'lizard tail',
    type = constant.ItemType.etc,
    price = 120
  )
)