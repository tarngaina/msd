TableExp = {
  1:0,
  2:15,
  3:49,
  4:106,
  5:198,
  6:333,
  7:705,
  8:1265,
  9:2105,
  10:3347,
  11:4589,
  12:5831,
  13:7073,
  14:8315,
  15:9557,
  16:11047,
  17:12835,
  18:14980,
  19:17554,
  20:20642,
  21:24347,
  22:28793,
  23:34128,
  24:40530,
  25:48212,
  26:57430,
  27:68491,
  28:81764,
  29:97691,
  30:999999999
}

CDs = {
  'farm':0.0
}

class ItemType:
  equip = 'equip'
  consume = 'consume'
  etc = 'etc'
  
class Job:
  
  main_stat = {}
  
  warrior = 'warrior'
  main_stat[warrior] = 'str'
  
  bowman = 'bowman'
  main_stat[bowman] = 'dex'
  
  magician = 'magician'
  main_stat[magician] = 'int'
  
  thief = 'thief'
  main_stat[thief] = 'luk'
  
  pirate = 'pirate'
  main_stat[pirate] = 'str'
  
  jobs = [warrior, bowman, magician, thief, pirate]