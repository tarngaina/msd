import os, datetime
from discord.ext import commands
import keep_alive
import constant, manager, pref, player, item, area

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
	s = (f'{ctx.author.name} has:\n'
	     f'{p.hp}/{p.max_hp}hp\n'
	     f'{p.lvl}lv, {p.xp}xp\n'
	     f'{p.meso}meso')
	await ctx.send(s)


@bot.group(description='show your stats', invoke_without_command=True)
async def stat(ctx):
	p = player.find(ctx.author.id)
	s = (f'{ctx.author.mention} stats:\n'
	     f'job: {p.job}\n'
	     f'att: {p.get_att()}\n'
	     f'free point: {p.stat_point}\n'
	     f'str: {p.stat["str"]}\n'
	     f'dex: {p.stat["dex"]}\n'
	     f'int: {p.stat["int"]}\n'
	     f'luk: {p.stat["luk"]}\n')
	await ctx.send(s)


@stat.command(description='add point to str stat')
async def str(ctx, pts: int):
	p = player.find(ctx.author.id)
	res, msg = manager.plus_stat_point(p, 'str', pts)
	if res:
		pref.save(p.id)
	await ctx.send(msg)


@stat.command(description='add point to dex stat')
async def dex(ctx, pts: int):
	p = player.find(ctx.author.id)
	res, msg = manager.plus_stat_point(p, 'dex', pts)
	if res:
		pref.save(p.id)
	await ctx.send(msg)


@stat.command(description='add point to str stat')
async def luk(ctx, pts: int):
	p = player.find(ctx.author.id)
	res, msg = manager.plus_stat_point(p, 'luk', pts)
	if res:
		pref.save(p.id)
	await ctx.send(msg)


@stat.command(description='add point to int stat')
async def int(ctx, pts: int):
	p = player.find(ctx.author.id)
	res, msg = manager.plus_stat_point(p, 'int', pts)
	if res:
		pref.save(p.id)
	await ctx.send(msg)


@bot.command(description='go farming')
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


@map.command(description='go to map with id, add find map by name later')
async def go(ctx, *, id):
	p = player.find(ctx.author.id)
	res, msg = manager.go_to_area(p, id)
	if res:
		pref.save(p.id)
	await ctx.send(msg)


@map.command(description='show all map')
async def list(ctx):
	s = '\nmsd map go name (or id)\n\n'
	for a in area.areas:
		s += f'{a.name}, id:{a.id}'
		s = s + f' (lv.{a.lvl}+)' if not a.is_town else s
		s += '\n'
	await ctx.send(s)


@bot.group(description='show your inventory', invoke_without_command=True)
async def inventory(ctx):
	s = f'{ctx.author.name} has:\n'
	p = player.find(ctx.author.id)
	for id in p.inventory:
		s += f'{item.find(id).name}: {p.inventory[id]}\n'
	await ctx.send(s)


@inventory.command(description='show your equip tab')
async def equip(ctx):
	s = f'{ctx.author.name} has equips:\n'
	p = player.find(ctx.author.id)
	for id in p.inventory:
		i = item.find(id)
		if i.type == constant.ItemType.equip:
			s += f'{item.find(id).name}: {p.inventory[id]}\n'
	await ctx.send(s)


@inventory.command(description='show your consume tab')
async def consume(ctx):
	s = f'{ctx.author.name} has consumes:\n'
	p = player.find(ctx.author.id)
	for id in p.inventory:
		i = item.find(id)
		if i.type == constant.ItemType.consume:
			s += f'{item.find(id).name}: {p.inventory[id]}\n'
	await ctx.send(s)


@inventory.command(description='show your etc tab')
async def etc(ctx):
	s = f'{ctx.author.name} has etcs:\n'
	p = player.find(ctx.author.id)
	for id in p.inventory:
		i = item.find(id)
		if i.type == constant.ItemType.etc:
			s += f'{item.find(id).name}: {p.inventory[id]}\n'
	await ctx.send(s)


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


@bot.group(
    description='advance job, advjob list for list of jobs',
    invoke_without_command=True)
async def advjob(ctx, job=None):
	if job == None:
		await ctx.send('msd advjob list for list of jobs')
	else:
		p = player.find(ctx.author.id)
		res, msg = manager.advance_job(p, job)
		if res:
			pref.save(p.id)
		await ctx.send(msg)


@advjob.command(description='show list of jobs')
async def list(ctx):
	s = 'list of jobs:\n'
	for j in constant.Job.jobs:
		s += f'{j}\n'
	await ctx.send(s)


keep_alive.keep_alive()
bot.run(token, bot=True, reconnect=True)
