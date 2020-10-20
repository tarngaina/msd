jobs = []

def add(j):
  jobs.append(j)

def find_name(name):
  for j in jobs:
    if j.name == name:
      return j
  return None

class Job():
  def __init__(self, name, job_grade, main_stat, sub_stat, previous):
    self.name = name
    self.job_grade = job_grade
    self.main_stat = main_stat
    self.sub_stat = sub_stat
    self.previous = previous

add(
  Job(
    name = 'beginner',
    job_grade = 0,
    main_stat = 'str',
    sub_stat = 'str',
    previous = None
  )
)
add(
  Job(
    name = 'warrior',
    job_grade = 1,
    main_stat = 'str',
    sub_stat = 'dex',
    previous = 'beginner'
  )
)
add(
  Job(
    name = 'bowman',
    job_grade = 1,
    main_stat = 'dex',
    sub_stat = 'str',
    previous = 'beginner'
  )
)
add(
  Job(
    name = 'magician',
    job_grade = 1,
    main_stat = 'int',
    sub_stat = 'luk',
    previous = 'beginner'
  )
)
add(
  Job(
    name = 'thief',
    job_grade = 1,
    main_stat = 'dex',
    sub_stat = 'luk',
    previous = 'beginner'
  )
)
add(
  Job(
    name = 'pirate',
    job_grade = 1,
    main_stat = 'str',
    sub_stat = 'dex',
    previous = 'beginner'
  )
)
