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
  embed.set_footer(text = 'Some useful commands: "stat", "skill", "inventory", "equip".')
  await ctx.send(embed = embed)


@bot.command(description='show your stats')
async def stat(ctx, *, param = None):
  p = player.find(ctx.author.id)
  if param == None:
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
    embed.set_footer(text = 'Command to increase you stats: "stat <name> <AP>".')
    await ctx.send(embed = embed)
  else:
    res, msg = manager.plus_stat_point(p, param)
    if res:
      pref.save(p.id)
    await ctx.send(f'**{ctx.author.name}**{msg}')


@bot.command(description='show you skills')
async def skill(ctx, *, param = None):
  p = player.find(ctx.author.id)
  if param == None:
    if p.job.name.lower() == 'beginner':
      await ctx.send(f'Sorry **{ctx.author.name}**, Beginner don\'t have skills.')
      return
    embed = discord.Embed(
      title = f'**{ctx.author.name}**',
      description = '**SKILL**',
      color = constant.ColorHex.cyan
    )
    embed.set_thumbnail(url = ctx.author.avatar_url)
    embed.add_field(
      name = f'{p.job.get_name().upper()}, **SP**: {p.free_skill_point}',
      value = (
        f'{p.job.skills[0].get_name()} Lv.{p.skill_att}\n'
        f'Increase your base attack point by {p.skill_att * 2}.\n'
        f'{p.job.skills[1].get_name()} Lv.{p.skill_stat}\n'
        f'Boost your {p.job.main_stat.upper()} by {p.skill_stat * 5} and {p.job.sub_stat.upper()} by {p.skill_stat * 2}.\n'
        f'{p.job.skills[2].get_name()} Lv.{p.skill_attack}\n'
        f'Land an attack of {100 + p.skill_attack * 2}% damage on your enemy.\n'
        f'{p.job.skills[3].get_name()} Lv.{p.skill_buff}\n'
        f'For next {(p.skill_buff // 30) + 1} turn(s), your next attack deal bonus {p.skill_buff}% damage.\n'
        f'{p.job.skills[4].get_name()} Lv.{p.skill_iframe}\n'#
        f'Instantly deal {p.skill_iframe}% damage on enemy and become invsible for next {(p.skill_buff // 30) + 1} turn(s).'
      )
    )
    embed.set_footer(text = 'Command to increase your skills level: "skill <name> <SP>".')
    await ctx.send(embed = embed)
  else:
    res, msg = manager.plus_skill_point(p, param)
    if res:
      pref.save(p.id)
    await ctx.send(f'**{ctx.author.name}**{msg}')

@bot.command(aliases = ['f'], description='go farming')
async def farm(ctx):
  p = player.find(ctx.author.id)
  res, msg = manager.farm(p)
  if res:
      pref.save(p.id)
  await ctx.send(f'**{ctx.author.name}**{msg}')
  if res:
    await event.trigger_event(ctx.channel, ctx.author)


@bot.command(aliases = ['m'], description='show where you are now')
async def map(ctx, *, param = None):
  p = player.find(ctx.author.id)
  if param == None:
    embed = discord.Embed(
      title = f'**{ctx.author.name}**',
      description = '**MAP**',
      color = constant.ColorHex.purple
    )
    embed.set_thumbnail(url = ctx.author.avatar_url)
    embed.add_field(
      name = f'You are currently in \n{p.area.get_name()}',
      value = f'Level recommended: **{p.area.lv}**',
      inline = False
    )
    embed.set_footer(text = 'To see a list of map, use command: "map list".')
    await ctx.send(embed = embed)
  elif param.startswith('list'):
    page = param[-1]
    if page.isnumeric():
      page = int(page)
    else:
      page = 1
    embed = discord.Embed(
      title = '**List of maps:**',
      description = f'Page {page}',
      color = constant.ColorHex.purple
    )
    start = (page-1)*5
    end = start + 5
    for i in range(start, end):
      a = area.areas[i]
      embed.add_field(
        name = f'{a.get_name()}',
        value = f'Lv.{a.lv}',
        inline = True
      )
    embed.set_footer(text = 'To go certain map: "map <name>".')
    await ctx.send(embed = embed)
  else:
    res, msg = manager.go_area(p, param)
    if res:
      pref.save(p.id)
    await ctx.send(f'**{ctx.author.name}**{msg}')


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


@bot.command(aliases = ['adv'], description='advance job, advjob list for list of jobs')
async def advance(ctx, *, param = None):
  if param == None:
    await ctx.send('Use command "advance list" for more information.')
  elif param.startswith('list'):
    page = param[-1]
    if page.isnumeric():
      page = int(page)
    else:
      page = 1
    page_name = 'Explorer'
    embed = discord.Embed(
      title = '**List of jobs:**',
      description = f'{page_name}',
      color = constant.ColorHex.red
    )
    s = ''
    for j in job.jobs:
      if j.name.lower() != 'beginner':
        s += f'{j.get_name()}: {j.main_stat.upper()}; {", ".join(j.weapon_types).upper()}\n'
    embed.add_field(
      name = 'Make sure you are beginner and reached lv 10.',
      value = s
    )
    embed.set_footer(text = 'Advance job command: "advance <name>".')
    await ctx.send(embed = embed)
  else:
    p = player.find(ctx.author.id)
    res, msg = manager.advance_job(p, param)
    if res:
      pref.save(p.id)
    await ctx.send(f'**{ctx.author.name}**{msg}')


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
