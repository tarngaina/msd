import os, datetime
from discord.ext import commands
import keep_alive
import constant, manager, pref, player, item, area, job

# hide token in .env
token = os.getenv("TOKEN")
prefix = 'msd '
bot = commands.Bot(command_prefix=prefix, case_insentitive=True)


@bot.event
async def on_ready():
  print(f'Logged in as {bot.user.name} - {bot.user.id}')
  return


@bot.event
async def on_message(message):
  if message.content.lower().startswith(prefix):
    message.content = 'msd' + message.content[3:]
    await bot.process_commands(message)


@bot.command(description='show some stuffs')
async def profile(ctx):
  p = player.find(ctx.author.id)
  s = (
    f'{ctx.author.mention}\'s profile:\n'
    f'hp: {p.hp}/{p.max_hp}\n'
    f'lv: {p.lv}, xp: {p.get_xp_percent():.2f}%\n'
    f'job: {p.job.name}\n'
    f'meso: {p.meso:n}'
  )
  await ctx.send(s)


@bot.command(description='show your stats')
async def stat(ctx):
  p = player.find(ctx.author.id)
  s = (f'{ctx.author.mention} stats:\n'
       f'job: {p.job.name}\n'
       f'att: {p.get_att()}\n'
       f'free point: {p.free_stat_point}\n'
       f'str: {p.str}\n'
       f'dex: {p.dex}\n'
       f'int: {p.int}\n'
       f'luk: {p.luk}\n')
  await ctx.send(s)


@bot.command(description='add point to str stat')
async def str(ctx, pts: int):
  p = player.find(ctx.author.id)
  res, msg = manager.plus_stat_point(p, 'str', pts)
  if res:
    pref.save(p.id)
  await ctx.send(msg)


@bot.command(description='add point to dex stat')
async def dex(ctx, pts: int):
  p = player.find(ctx.author.id)
  res, msg = manager.plus_stat_point(p, 'dex', pts)
  if res:
    pref.save(p.id)
  await ctx.send(msg)


@bot.command(description='add point to str stat')
async def luk(ctx, pts: int):
  p = player.find(ctx.author.id)
  res, msg = manager.plus_stat_point(p, 'luk', pts)
  if res:
    pref.save(p.id)
  await ctx.send(msg)


@bot.command(description='add point to int stat')
async def int(ctx, pts: int):
  p = player.find(ctx.author.id)
  res, msg = manager.plus_stat_point(p, 'int', pts)
  if res:
    pref.save(p.id)
  await ctx.send(msg)


@bot.command(aliases = ['f'], description='go farming')
async def farm(ctx):
  p = player.find(ctx.author.id)
  res, msg = manager.check_cd(p, 'farm')
  if res:
    res2, msg = manager.farm(p)
    if res2:
      pref.save(p.id)
    await ctx.send(ctx.author.mention + msg)
  else:
    await ctx.send(msg)


@bot.group(description='show where you are now', invoke_without_command=True)
async def map(ctx):
  p = player.find(ctx.author.id)
  await ctx.send(f'{ctx.author.mention}, you are in {p.area.name}\nmsd map list for list of maps')


@bot.command(description='go to map with id, add find map by name later')
async def go(ctx, *, id):
  p = player.find(ctx.author.id)
  res, msg = manager.go_area(p, id)
  if res:
    pref.save(p.id)
  await ctx.send(msg)


@map.command(description='show all map')
async def list(ctx):
  s = '\nmsd go name (or id)\n\n'
  for a in area.areas:
    s += f'{a.name}, id:{a.id}'
    s = s + f' (lv.{a.lv}+)' if not a.is_safe else s
    s += '\n'
  await ctx.send(s)


@bot.group(aliases=['i', 'inv'], description='show your inventory', invoke_without_command=True)
async def inventory(ctx):
  p = player.find(ctx.author.id)
  s = (
    f'{ctx.author.mention} has:\n'
    f'meso: {p.meso}\n\n'
    'type msd inventory <category> to see your items\n' 'categories:\n' 'equip\nconsume\netc')
  await ctx.send(s)


@inventory.command(description='show your equip tab')
async def equip(ctx):
  s = f'{ctx.author.name} has equips:\n'
  p = player.find(ctx.author.id)
  count = 0
  for i in p.inventory['equip']:
    s += f'{i.name} (id:equip{count})\n'
    count += 1
  await ctx.send(s)


@inventory.command(description='show your consume tab')
async def consume(ctx):
  s = f'{ctx.author.name} has consumes:\n'
  p = player.find(ctx.author.id)
  for id in p.inventory['consume']:
    i = item.find(id)
    s += f'{item.find(id).name}: {p.inventory["consume"][id]}\n'
  await ctx.send(s)


@inventory.command(description='show your etc tab')
async def etc(ctx):
  s = f'{ctx.author.name} has etcs:\n'
  p = player.find(ctx.author.id)
  for id in p.inventory['etc']:
    i = item.find(id)
    s += f'{item.find(id).name}: {p.inventory["etc"][id]}\n'
  await ctx.send(s)


@bot.command(description='equip an item')
async def equip(ctx, *, id):
  p = player.find(ctx.author.id)
  if id == 'info':
    e = ''
    s = (
      f'{ctx.author.mention} equips: \n'
      f'weapon: {p.weapon.get_name() if p.weapon != None else e}\n'
      f'hat: {p.hat.get_name() if p.hat != None else e}\n'
      f'top: {p.top.get_name() if p.top != None else e}\n'
      f'bottom: {p.bottom.get_name() if p.bottom != None else e}\n'
      f'shoe: {p.shoe.get_name() if p.shoe != None else e}\n'
      f'glove: {p.glove.get_name() if p.glove != None else e}\n'
      f'cape: {p.cape.get_name() if p.cape != None else e}\n'
      f'shoulder: {p.shoulder.get_name() if p.shoulder != None else e}\n'
      )
    await ctx.send(s)
  else:
    res, msg = manager.equip_item(p, id)
    if res:
      pref.save(p.id)
    await ctx.send(msg)

@bot.command(description='sell your item with number')
async def sell(ctx, *, param):
  param = param.split(' ')
  id = ' '.join(param)
  num = 1
  if param[-1].isnumeric():
    id = ' '.join(param[:-1])
    num = param[-1]
  p = player.find(ctx.author.id)
  res, msg = manager.sell_item(p, id, num)
  if res:
    pref.save(p.id)
  await ctx.send(msg)


@bot.group(description='advance job, advjob list for list of jobs', invoke_without_command=True)
async def advance(ctx, job=None):
  if job == None:
    await ctx.send('msd advance list for list of jobs')
  else:
    p = player.find(ctx.author.id)
    res, msg = manager.advance_job(p, job)
    if res:
      pref.save(p.id)
    await ctx.send(msg)


@advance.command(description='show list of jobs')
async def list(ctx):
  p = player.find(ctx.author.id)
  s = 'list of jobs:\n'
  for j in job.jobs:
    if j.previous == p.job.name:
      s += f'{j.name}\n'
  await ctx.send(s)


@bot.command()
async def test(ctx):
  p = player.find(ctx.author.id)
  print(vars(p))


keep_alive.keep_alive()
bot.run(token, bot=True, reconnect=True)
