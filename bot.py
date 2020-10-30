import os, datetime
import discord
from discord.ext import commands
import keep_alive
import constant, manager, pref, player, item, area, job
import event

# hide token in .env
token = os.getenv("TOKEN")
prefix = 'msd '
bot = commands.Bot(command_prefix=prefix, case_insentitive=True)
event.bot = bot

@bot.event
async def on_ready():
  print(f'Logged in as {bot.user.name} - {bot.user.id}')
  return


@bot.event
async def on_message(message):
  if message.content.lower().startswith(prefix):
    message.content = 'msd' + message.content[3:]
    await bot.process_commands(message)


@bot.command(aliases = ['p'], description='show some stuffs')
async def profile(ctx):
  p = player.find(ctx.author.id)
  embed = discord.Embed(
    title = f'**{ctx.author.name}**',
    description = f'{p.job.get_name().upper()} Lv.{p.lv}',
    color = constant.ColorHex.pink
  )
  embed.set_thumbnail(url = ctx.author.avatar_url)
  embed.add_field(
    name = 'GENERAL',
    value = (
      f'**Exp**: {p.xp:,.0f} ({p.get_xp_percent():.2f}%)\n'
      f'{p.get_xp_bar_texture()}\n'
      f'**Guild**: \n'
      f'**Fame**: \n'
    ),
    inline = False
  )
  embed.add_field(
    name = 'STAT',
    value = (
      f'**HP**: {p.hp}/{p.max_hp}\n'
      f'{p.get_hp_bar_texture()}\n'
      f'**ATT**: {p.get_att()}\n'
      f'**{p.job.main_stat.upper()}**: {p.get_main_stat()}'
    ),
    inline = False
  )
  embed.add_field(
    name = 'INVENTORY',
    value = (
      f'{constant.Texture.meso} **Meso**: {p.meso:,.0f}'
    ),
    inline = False
  )
  await ctx.send(embed = embed)


@bot.command(description='show your stats')
async def stat(ctx):
  p = player.find(ctx.author.id)
  embed = discord.Embed(
    title = f'**{ctx.author.name}**',
    description = '**STAT**',
    color = constant.ColorHex.green
  )
  embed.set_thumbnail(url = ctx.author.avatar_url)
  embed.add_field(
    name = '**INFO**',
    value = (
      f'**ATT**: {p.get_att()}\n'
      f'**HP**: {p.hp}/{p.max_hp}'
    ),
    inline = False
  )
  embed.add_field(
    name = f'{p.job.get_name().upper()}, **AP**: {p.free_stat_point}',
    value = (
      f'**STR**: {p.str}\n'
      f'**DEX**: {p.dex}\n'
      f'**INT**: {p.int}\n'
      f'**LUK**: {p.luk}'
    ),
    inline = False
  )
  await ctx.send(embed = embed)


@bot.command(name = 'str', description='add point to str stat')
async def str_(ctx, pts: int):
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


@bot.command(name = 'int', description='add point to int stat')
async def int_(ctx, pts: int):
  p = player.find(ctx.author.id)
  res, msg = manager.plus_stat_point(p, 'int', pts)
  if res:
    pref.save(p.id)
  await ctx.send(msg)

@bot.group(description = 'show your skills', invoke_without_command = True)
async def skill(ctx):
  s = ''
  p = player.find(ctx.author.id)
  if p.job.name.lower() != 'beginner':
    embed = discord.Embed(
      title = f'**{ctx.author.name}**',
      description = '**SKILL**',
      color = constant.ColorHex.cyan
    )
    embed.set_thumbnail(url = ctx.author.avatar_url)
    embed.add_field(
      name = '',#f'{p.job.get_name().upper()}, **SP**: {p.free_skill_point}',
      value = (
        f'{p.job.skills[0].get_name()} Lv.{p.skill_att}\n'
        f'Increase your base attack point by {p.skill_att * 2}.\n'
        f'{p.job.skills[1].get_name()} Lv.{p.skill_stat}\n'
        f'Boost your {p.job.main_stat.upper()} by {p.skill_stat * 5} and {p.job.sub_stat.upper()} by {p.skill_stat * 2}.\n'
        f'{p.job.skills[2].get_name()} Lv.{p.skill_attack}\n'
        f'Land an attack of {100 + p.skill_attack * 2}% damage on your enemy.\n'
        f'{p.job.skills[3].get_name()} Lv.{p.skill_buff}\n'
        f'In next {(p.skill_buff // 30) + 1} turn(s), your next attack deal bonus {p.skill_buff}% damage.\n'
        f'{p.job().skills[4].get_name()} Lv.{p.skill_iframe}\n'
        f'Instantly deal {p.skill_iframe}% damage on enemy and become invsible for next {(p.skill_buff // 30) + 1} turn(s).'
      )
    )
    await ctx.send(embed = embed)
  else:
    await ctx.send('beginner has no skills')

@skill.command(description = 'add point to skill')
async def add(ctx, *, id):
  p = player.find(ctx.author.id)
  s = id.split(' ')
  if s[-1].isnumeric():
    pts = int(s[-1])
    id = ' '.join(s[:-1])
    res, msg = manager.plus_skill_point(p, id, pts)
    if res:
      pref.save(p.id)
    await ctx.send(f'**{ctx.author.name}**{msg}')
  else:
    await ctx.send('not found number of point')


@bot.command(aliases = ['f'], description='go farming')
async def farm(ctx):
  p = player.find(ctx.author.id)
  res, msg = manager.check_cd(p, 'farm')
  if res:
    res2, msg = manager.farm(p)
    if res2:
      pref.save(p.id)
    await ctx.send(f'**{ctx.author.name}**{msg}')
    await event.trigger_event(ctx.channel, ctx.author)
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
    num = int(param[-1])
  p = player.find(ctx.author.id)
  res, msg = manager.sell_item(p, id, num)
  if res:
    pref.save(p.id)
  await ctx.send(msg)


@bot.group(description='advance job, advjob list for list of jobs', invoke_without_command=True)
async def advance(ctx, *, job=None):
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
  #p = player.find(ctx.author.id)
  #print(vars(p))
  s = ''
  for e in ctx.guild.emojis:
    s += f':{e.name}:{e.id}\n'
  await ctx.send(s)


keep_alive.keep_alive()
bot.run(token, bot=True, reconnect=True)
