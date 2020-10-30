import asyncio, random
import constant


bot = None

events = []

def add(e):
  events.append(e)

async def trigger_event(channel, author):
  if random.randint(0, 100) < 10:
    e = random_event()
    await asyncio.sleep(5)
    await e.start(channel, author)
  
def random_event():
  return random.choice(events)
  
class Event():
  def __init__(self, id, name, type, **dic):
    self.id = id
    self.name = name
    self.type = type
  
  async def start(self, channel, author):
    if self.type == constant.EventType.elite_monster:
      msg = (
        'An elite monster has appeared.\n'
        'Quickly type `fight` to kill the monster.\n'
        'You only have 5 seconds.\n'
        'Go go go.'
      )
      await channel.send(msg)
      def check(m):
        return m.channel == channel and m.author == author
      try:
        user_type = await bot.wait_for('message', check=check, timeout=5)
        if user_type.content.lower() == 'fight':
          await channel.send(
            f'**{author.name}** has successfully killed the elite monster.\n'
            'Reward: nothing bro, still testing.'
          )
      except asyncio.TimeoutError:
        await channel.send('Sorry, you ran out of time.')
    
add(
  Event(
    id = '',
    name = 'Elite Monster Event',
    type = constant.EventType.elite_monster
  )
)