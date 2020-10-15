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
	s = (f'job: {p.job}\n'
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
	res, msg = p.plus_stat_point('str', pts)
	if res:
		await ctx.send('done')
		pref.save(p.id)
	else:
		await ctx.send(msg)


@stat.command(description='add point to dex stat')
async def dex(ctx, pts: int):
	p = player.find(ctx.author.id)
	res, msg = p.plus_stat_point('dex', pts)
	if res:
		await ctx.send('done')
		pref.save(p.id)
	else:
		await ctx.send(msg)


@stat.command(description='add point to str stat')
async def luk(ctx, pts: int):
	p = player.find(ctx.author.id)
	res, msg = p.plus_stat_point('luk', pts)
	if res:
		await ctx.send('done')
		pref.save(p.id)
	else:
		await ctx.send(msg)


@stat.command(description='add point to int stat')
async def int(ctx, pts: int):
	p = player.find(ctx.author.id)
	res, msg = p.plus_stat_point('int', pts)
	if res:
		await ctx.send('done')
		pref.save(p.id)
	else:
		await ctx.send(msg)


@bot.command(description='go farming')
async def farm(ctx):
	p = player.find(ctx.author.id)
	res, msg = manager.check_cd(p, 'farm')
	if res:
		res2, meso, xp, lvup, item, num, hp, die = manager.farm(p)
		xp_next_lvl = constant.TableExp[p.lvl]
		if res2:
			if die:
				await ctx.send(
				    f'{ctx.author.name} lost {hp}hp: {p.hp}/{p.max_hp} and died'
				)
			else:
				s = (f'{ctx.author.name} farmed\n'
				     f'lost {hp}hp: {p.hp}/{p.max_hp}\n'
				     f'get {meso}meso\n'
				     f'get {xp}xp: {p.xp}/{xp_next_lvl}')
				s = s + f'\ngratz, you level up to {p.lvl}' if lvup else s
				s = s + f'\nand get: {num} {item.name}' if num > 0 else s
				await ctx.send(s)
			pref.save(p.id)
		else:
			await ctx.send(meso)
	else:
		await ctx.send(f'you need to wait more {msg}s')


@bot.group(description='show where you are now', invoke_without_command=True)
async def map(ctx):
	p = player.find(ctx.author.id)
	await ctx.send(f'you are in {p.area.name}')


@map.command(description='go to map with id, add find map by name later')
async def go(ctx, *, id):
	p = player.find(ctx.author.id)
	res, msg = manager.go_to_area(p, id)
	if res:
		await ctx.send(f'done, you are in {msg} now')
		pref.save(p.id)
	else:
		await ctx.send(msg)


@map.command(description='show all map')
async def list(ctx):
	s = 'how to go to map:\nmsd map go id/name\n'
	for a in area.areas:
		s += f'{a.name}, id:{a.id}'
		s = s + f' (lv.{a.lvl_recommended}+)' if not a.is_town else s
		s += '\n'
	await ctx.send(s)


@bot.command(description='show your inventory')
async def inventory(ctx):
	s = f'{ctx.author.name} has:\n'
	p = player.find(ctx.author.id)
	for id in p.inventory:
		s += f'{item.find(id).name}: {p.inventory[id]}\n'
	await ctx.send(s)


@bot.group(
    description='advance job, advjob list for list of jobs',
    invoke_without_command=True)
async def advjob(ctx, job):
	p = player.find(ctx.author.id)
	res, msg = manager.advance_job(p, job)
	if res:
		await ctx.send(f'job avanced to {job}')
		pref.save(p.id)
	else:
		await ctx.send(msg)


@advjob.command(description='show list of jobs')
async def list(ctx):
	s = 'list of jobs:\n'
	for j in constant.Job.jobs:
		s += f'{j}\n'
	await ctx.send(s)


keep_alive.keep_alive()
bot.run(token, bot=True, reconnect=True)
