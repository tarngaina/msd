jobs = []

def add(j):
  jobs.append(j)

def find_name(name):
  for j in jobs:
    if j.name.lower() == name.lower():
      return j
  return None

def find(id):
  j = find_name(id)
  return j

class Job():
  def __init__(self, name, lv, job_grade, main_stat, sub_stat, weapon_types, previous):
    self.name = name
    self.lv = lv
    self.job_grade = job_grade
    self.main_stat = main_stat
    self.sub_stat = sub_stat
    self.weapon_types = weapon_types
    self.previous = previous

add(
  Job(
    name = 'beginner',
    lv = 1,
    job_grade = 0,
    main_stat = 'str',
    sub_stat = 'str',
    weapon_types = ['sword'],
    previous = None
  )
)
add(
  Job(
    name = 'warrior',
    lv = 10,
    job_grade = 1,
    main_stat = 'str',
    sub_stat = 'dex',
    weapon_types = ['sword', 'axe', 'spear'],
    previous = 'beginner'
  )
)
add(
  Job(
    name = 'bowman',
    lv = 10,
    job_grade = 1,
    main_stat = 'dex',
    sub_stat = 'str',
    weapon_types = ['bow', 'crossbow'],
    previous = 'beginner'
  )
)
add(
  Job(
    name = 'magician',
    lv = 10,
    job_grade = 1,
    main_stat = 'int',
    sub_stat = 'luk',
    weapon_types = ['wand', 'staff'],
    previous = 'beginner'
  )
)
add(
  Job(
    name = 'thief',
    lv = 10,
    job_grade = 1,
    main_stat = 'dex',
    sub_stat = 'luk',
    weapon_types = ['dagger', 'claw'],
    previous = 'beginner'
  )
)
add(
  Job(
    name = 'pirate',
    lv = 10,
    job_grade = 1,
    main_stat = 'str',
    sub_stat = 'dex',
    weapon_types = ['knuckle', 'gun'],
    previous = 'beginner'
  )
)
