from chatter import ChatterBotFactory, ChatterBotType

factory = ChatterBotFactory()

bot2 = factory.create(ChatterBotType.PANDORABOTS, 'b0dafd24ee35a477')
bot2session = bot2.create_session()

s=input()
s = bot2session.think(s)
print ('bot2> ' + s)
