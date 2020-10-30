import skill, constant

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
  def __init__(self, name, lv, main_stat, sub_stat, weapon_types, previous, skills):
    self.name = name
    self.lv = lv
    self.main_stat = main_stat
    self.sub_stat = sub_stat
    self.weapon_types = weapon_types
    self.previous = previous
    self.skills = skills

  def find_skill(self, id):
    for s in self.skills:
      if s.name.lower() == id.lower():
        return s
    return None
    
  def get_name(self):
    s = ''
    s += f'**{self.name}**'
    return s



add(
  Job(
    name = 'Beginner',
    lv = 1,
    main_stat = 'str',
    sub_stat = 'str',
    weapon_types = ['sword'],
    previous = None,
    skills = None,
  )
)


add(
  Job(
    name = 'Hero',
    lv = 10,
    main_stat = 'str',
    sub_stat = 'dex',
    weapon_types = ['sword', 'axe'],
    previous = 'Beginner',
    skills = [
      skill.Skill(
        id = '',
        name = 'Weapon Mastery',
        type = constant.SkillType.att
      ),
      skill.Skill(
        id = '',
        name = 'Physical Training',
        type = constant.SkillType.stat
      ),
      skill.Skill(
        id = '',
        name = 'Raging Blow',
        type = constant.SkillType.attack
      ),
      skill.Skill(
        id = '',
        name = 'Combo Attack',
        type = constant.SkillType.buff
      ),
      skill.Skill(
        id = '',
        name = 'Worldreaver',
        type = constant.SkillType.iframe
      )
    ]
  )
)

add(
  Job(
    name = 'Paladin',
    lv = 10,
    main_stat = 'str',
    sub_stat = 'dex',
    weapon_types = ['sword', 'axe'],
    previous = 'Beginner',
    skills = [
      skill.Skill(
        id = '',
        name = 'Weapon Mastery',
        type = constant.SkillType.att
      ),
      skill.Skill(
        id = '',
        name = 'Physical Training',
        type = constant.SkillType.stat
      ),
      skill.Skill(
        id = '',
        name = 'Heaven\'s Hammer',
        type = constant.SkillType.attack
      ),
      skill.Skill(
        id = '',
        name = 'Parashock Guard',
        type = constant.SkillType.buff
      ),
      skill.Skill(
        id = '',
        name = 'Guardian',
        type = constant.SkillType.iframe
      )
    ]
  )
)

add(
  Job(
    name = 'Dark Knight',
    lv = 10,
    main_stat = 'str',
    sub_stat = 'dex',
    weapon_types = ['spear'],
    previous = 'Beginner',
    skills = [
      skill.Skill(
        id = '',
        name = 'Weapon Mastery',
        type = constant.SkillType.att
      ),
      skill.Skill(
        id = '',
        name = 'Physical Training',
        type = constant.SkillType.stat
      ),
      skill.Skill(
        id = '',
        name = 'Spear of Darkness',
        type = constant.SkillType.attack
      ),
      skill.Skill(
        id = '',
        name = 'Evil Eye',
        type = constant.SkillType.buff
      ),
      skill.Skill(
        id = '',
        name = 'Final Pact',
        type = constant.SkillType.iframe
      )
    ]
  )
)

add(
  Job(
    name = 'Bowmaster',
    lv = 10,
    main_stat = 'dex',
    sub_stat = 'str',
    weapon_types = ['bow'],
    previous = 'Beginner',
    skills = [
      skill.Skill(
        id = '',
        name = 'Archery Mastery',
        type = constant.SkillType.att
      ),
      skill.Skill(
        id = '',
        name = 'Physical Training',
        type = constant.SkillType.stat
      ),
      skill.Skill(
        id = '',
        name = 'Arrow Blaster',
        type = constant.SkillType.attack
      ),
      skill.Skill(
        id = '',
        name = 'Phoenix',
        type = constant.SkillType.buff
      ),
      skill.Skill(
        id = '',
        name = 'Hookshot',
        type = constant.SkillType.iframe
      )
    ]
  )
)

add(
  Job(
    name = 'Marksman',
    lv = 10,
    main_stat = 'dex',
    sub_stat = 'str',
    weapon_types = ['crossbow'],
    previous = 'Beginner',
    skills = [
      skill.Skill(
        id = '',
        name = 'Archery Mastery',
        type = constant.SkillType.att
      ),
      skill.Skill(
        id = '',
        name = 'Physical Training',
        type = constant.SkillType.stat
      ),
      skill.Skill(
        id = '',
        name = 'Surge Bolt',
        type = constant.SkillType.attack
      ),
      skill.Skill(
        id = '',
        name = 'Freezer',
        type = constant.SkillType.buff
      ),
      skill.Skill(
        id = '',
        name = 'Hookshot',
        type = constant.SkillType.iframe
      )
    ]
  )
)

add(
  Job(
    name = 'Arch Mage Fire Posion',
    lv = 10,
    main_stat = 'int',
    sub_stat = 'luk',
    weapon_types = ['staff, wand'],
    previous = 'Beginner',
    skills = [
      skill.Skill(
        id = '',
        name = 'Spell Mastery',
        type = constant.SkillType.att
      ),
      skill.Skill(
        id = '',
        name = 'High Wisdom',
        type = constant.SkillType.stat
      ),
      skill.Skill(
        id = '',
        name = 'Poison Nova',
        type = constant.SkillType.attack
      ),
      skill.Skill(
        id = '',
        name = 'Inferno Aura',
        type = constant.SkillType.buff
      ),
      skill.Skill(
        id = '',
        name = 'Ethereal Form',
        type = constant.SkillType.iframe
      )
    ]
  )
)

add(
  Job(
    name = 'Arch Mage Ice Lightning',
    lv = 10,
    main_stat = 'int',
    sub_stat = 'luk',
    weapon_types = ['staff, wand'],
    previous = 'Beginner',
    skills = [
      skill.Skill(
        id = '',
        name = 'Spell Mastery',
        type = constant.SkillType.att
      ),
      skill.Skill(
        id = '',
        name = 'High Wisdom',
        type = constant.SkillType.stat
      ),
      skill.Skill(
        id = '',
        name = 'Ice Age',
        type = constant.SkillType.attack
      ),
      skill.Skill(
        id = '',
        name = 'Bolt Barrage',
        type = constant.SkillType.buff
      ),
      skill.Skill(
        id = '',
        name = 'Ethereal Form',
        type = constant.SkillType.iframe
      )
    ]
  )
)

add(
  Job(
    name = 'Bishop',
    lv = 10,
    main_stat = 'int',
    sub_stat = 'luk',
    weapon_types = ['staff, wand'],
    previous = 'Beginner',
    skills = [
      skill.Skill(
        id = '',
        name = 'Spell Mastery',
        type = constant.SkillType.att
      ),
      skill.Skill(
        id = '',
        name = 'High Wisdom',
        type = constant.SkillType.stat
      ),
      skill.Skill(
        id = '',
        name = 'Big Bang',
        type = constant.SkillType.attack
      ),
      skill.Skill(
        id = '',
        name = 'Benediction',
        type = constant.SkillType.buff
      ),
      skill.Skill(
        id = '',
        name = 'Holy Magic Shell',
        type = constant.SkillType.iframe
      )
    ]
  )
)

add(
  Job(
    name = 'Night Lord',
    lv = 10,
    main_stat = 'luk',
    sub_stat = 'dex',
    weapon_types = ['claw'],
    previous = 'Beginner',
    skills = [
      skill.Skill(
        id = '',
        name = 'Claw Mastery',
        type = constant.SkillType.att
      ),
      skill.Skill(
        id = '',
        name = 'Physical Training',
        type = constant.SkillType.stat
      ),
      skill.Skill(
        id = '',
        name = 'Shurrikane',
        type = constant.SkillType.attack
      ),
      skill.Skill(
        id = '',
        name = 'Bleed Dart',
        type = constant.SkillType.buff
      ),
      skill.Skill(
        id = '',
        name = 'Invisible Potion',
        type = constant.SkillType.iframe
      )
    ]
  )
)

add(
  Job(
    name = 'Shadower',
    lv = 10,
    main_stat = 'luk',
    sub_stat = 'dex',
    weapon_types = ['dagger'],
    previous = 'Beginner',
    skills = [
      skill.Skill(
        id = '',
        name = 'Dagger Mastery',
        type = constant.SkillType.att
      ),
      skill.Skill(
        id = '',
        name = 'Physical Training',
        type = constant.SkillType.stat
      ),
      skill.Skill(
        id = '',
        name = 'Sonic Blow',
        type = constant.SkillType.attack
      ),
      skill.Skill(
        id = '',
        name = 'Meso Explosion',
        type = constant.SkillType.buff
      ),
      skill.Skill(
        id = '',
        name = 'Trickblade',
        type = constant.SkillType.iframe
      )
    ]
  )
)

add(
  Job(
    name = 'Buccaneer',
    lv = 10,
    main_stat = 'str',
    sub_stat = 'dex',
    weapon_types = ['knuckle'],
    previous = 'Beginner',
    skills = [
      skill.Skill(
        id = '',
        name = 'Knuckle Mastery',
        type = constant.SkillType.att
      ),
      skill.Skill(
        id = '',
        name = 'Physical Training',
        type = constant.SkillType.stat
      ),
      skill.Skill(
        id = '',
        name = 'Serpent Vortex',
        type = constant.SkillType.attack
      ),
      skill.Skill(
        id = '',
        name = 'Supercharge',
        type = constant.SkillType.buff
      ),
      skill.Skill(
        id = '',
        name = 'Meltdown',
        type = constant.SkillType.iframe
      )
    ]
  )
)

add(
  Job(
    name = 'Corsair',
    lv = 10,
    main_stat = 'dex',
    sub_stat = 'str',
    weapon_types = ['gun'],
    previous = 'Beginner',
    skills = [
      skill.Skill(
        id = '',
        name = 'Gun Mastery',
        type = constant.SkillType.att
      ),
      skill.Skill(
        id = '', 
        name = 'Physical Training',
        type = constant.SkillType.stat
      ),
      skill.Skill(
        id = '',
        name = 'Bullet Barrage',
        type = constant.SkillType.attack
      ),
      skill.Skill(
        id = '',
        name = 'Jolly Roger',
        type = constant.SkillType.buff
      ),
      skill.Skill(
        id = '',
        name = 'Nautilus Assault',
        type = constant.SkillType.iframe
      )
    ]
  )
)