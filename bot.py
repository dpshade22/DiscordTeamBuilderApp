import discord
from discord.ext import commands

import random

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print("Bot is ready")
    
top = ["Vayne", "Aatrox", "Gnar", "Fiora", "Kled", "Yorick", "Mordekaiser", "Kayle", "Sylas", "Ornn", "Teemo", "Urgot", "Yasuo", "Poppy", "Singed", "Tryndamere", "Renekton", "Sion", "Sett", "Jax", "Riven", "Volibear", "Nasus", "Akali", "Shen", "Illaoi", "Jayce", "Cho'Gath", "Vladimir", "Wukong", "Malphite", "Irelia", "Dr. Mundo", "Camille", "Kennen", "Darius", "Gangplank", "Maokai", "Garen", "Quinn", "Pantheon", "Swain", "Zilean", "Kalista"]
jg = ["Lee Sin", "Amumu", "Sylas", "Hecarim", "Shyvana", "Nunu & Willump", "Nocturne", "Ekko", "Udyr", "Olaf", "Rengar", "Fiddlesticks", "Sett",  "Jax", "Evelynn", "Ivern", "Rammus", "Kayn", "Volibear", "Karthus", "Shaco", "Warwick", "Nidalee", "Xin Zhao", "Kindred", "Trundle", "Master Yi", "Graves", "Jarvan IV", "Taliyah", "Sejuani", "Wukong", "Kha'Zix", "Zac", "Rek'Sai", "Vi", "Gragas", "Elise", "Skarner", "Pantheon", "Swain"]
mid = ["Brand", "Sylas", "Zoe", "Yasuo", "Ekko", "Fizz", "Aurelion Sol", "Katarina", "Lucian", "Akali", "Zed", "Pantheon", "Malzahar", "Veigar", "Zilean", "Qiyana", "Kassadin", "Diana", "Xerath", "Anivia", "Ryze", "Neeko", "Ahri", "Vladimir", "Azir", "Corki", "Ziggs", "Irelia", "Lux", "Twisted Fate", "Galio", "Syndra", "LeBlanc", "Cassiopeia", "Viktor", "Talon", "Vel'Koz", "Heimerdinger", "Lissandra", "Annie", "Rumble", "Orianna", "Morgana", "Lulu"]
bot = ["Jhin", "Vayne", "Miss Fortune", "Draven", "Yasuo", "Ashe", "Kai'Sa", "Xayah", "Varus", "Aphelios", "Twitch", "Sivir", "Lucian", "Caitlyn", "Kalista", "Jinx", "Tristana", "Ezreal", "Kog'Maw", "Heimerdinger", "Senna"]
support = ["Blitzcrank", "Thresh", "Fiddlesticks", "Sett", "Senna", "Braum", "Alistar", "Pyke", "Yuumi", "Bard", "Morgana", "Zilean", "Tahm Kench", "Brand", "Rakan", "Xerath", "Taric", "Lux", "Nautilus", "Swain", "Karma", "Lulu", "Vel'Koz", "Janna", "Soraka", "Nami", "Sona", "Leona", "Zyra", "Annie"]
    
@client.command()
async def League(ctx):

    topPick = random.choice(top)
    jgPick = random.choice(jg)
    midPick = random.choice(mid)
    botPick = random.choice(bot)
    suppPick = random.choice(support)
    
    allRoles = [topPick, jgPick, midPick, botPick, suppPick]
    
    while len(allRoles) != len(set(allRoles)):
        topPick = random.choice(top)
        jgPick = random.choice(jg)
        midPick = random.choice(mid)
        botPick = random.choice(bot)
        suppPick = random.choice(support)
        allRoles = [topPick, jgPick, midPick, botPick, suppPick]
    
    print(allRoles)
    
    await ctx.send(f'Top: {allRoles[0]}\nJungle: {allRoles[1]}\nMiddle: {allRoles[2]}\nBottom: {allRoles[3]}\nSupport: {allRoles[4]}')

@client.command()
async def league(ctx):

    topPick = random.choice(top)
    jgPick = random.choice(jg)
    midPick = random.choice(mid)
    botPick = random.choice(bot)
    suppPick = random.choice(support)
    
    allRoles = [topPick, jgPick, midPick, botPick, suppPick]
    
    while len(allRoles) != len(set(allRoles)):
        topPick = random.choice(top)
        jgPick = random.choice(jg)
        midPick = random.choice(mid)
        botPick = random.choice(bot)
        suppPick = random.choice(support)
        allRoles = [topPick, jgPick, midPick, botPick, suppPick]
    
    print(allRoles)
    
    await ctx.send(f'Top: {allRoles[0]}\nJungle: {allRoles[1]}\nMiddle: {allRoles[2]}\nBottom: {allRoles[3]}\nSupport: {allRoles[4]}')

#League commands for random role

@client.command()
async def leaguetop(ctx):
    await ctx.send(random.choice(top))

@client.command()
async def leaguejg(ctx):
    await ctx.send(random.choice(jg))

@client.command()
async def leaguemid(ctx):
    await ctx.send(random.choice(mid))

@client.command()
async def leaguebot(ctx):
    await ctx.send(random.choice(bot))
    
@client.command()
async def leagueadc(ctx):
    await ctx.send(random.choice(bot))
    
@client.command()
async def leaguesupp(ctx):
    await ctx.send(random.choice(support))
    
@client.command()
async def leaguesup(ctx):
    await ctx.send(random.choice(support))
    
@client.command()
async def leaguesupport(ctx):
    await ctx.send(random.choice(support))

#Valorant commands for random team

@client.command()
async def Valorant(ctx):
    valorantAgents = ["Breach", "Brimstone", "Cypher", "Jett", "Omen", "Phoenix", "Raze", "Sage", "Sova", "Viper"]

    ranAgent = random.choice(valorantAgents)
    ranAgent1 = random.choice(valorantAgents)
    ranAgent2 = random.choice(valorantAgents)
    ranAgent3 = random.choice(valorantAgents)
    ranAgent4 = random.choice(valorantAgents)

    valTeam = [ranAgent, ranAgent1, ranAgent2, ranAgent3, ranAgent4]

    while len(valTeam) != len(set(valTeam)):
        valTeam = [random.choice(valorantAgents), random.choice(valorantAgents), random.choice(valorantAgents), random.choice(valorantAgents), random.choice(valorantAgents)]
    
    print(valTeam)

    await ctx.send(f'{valTeam[0]}\n{valTeam[1]}\n{valTeam[2]}\n{valTeam[3]}\n{valTeam[4]}')
    
@client.command()
async def valorant(ctx):
    valorantAgents = ["Breach", "Brimstone", "Cypher", "Jett", "Omen", "Phoenix", "Raze", "Sage", "Sova", "Viper"]

    ranAgent = random.choice(valorantAgents)
    ranAgent1 = random.choice(valorantAgents)
    ranAgent2 = random.choice(valorantAgents)
    ranAgent3 = random.choice(valorantAgents)
    ranAgent4 = random.choice(valorantAgents)

    valTeam = [ranAgent, ranAgent1, ranAgent2, ranAgent3, ranAgent4]

    while len(valTeam) != len(set(valTeam)):
        valTeam = [random.choice(valorantAgents), random.choice(valorantAgents), random.choice(valorantAgents), random.choice(valorantAgents), random.choice(valorantAgents)]
    
    print(valTeam)

    await ctx.send(f'{valTeam[0]}\n{valTeam[1]}\n{valTeam[2]}\n{valTeam[3]}\n{valTeam[4]}')
    
@client.command()
async def val(ctx):
    valorantAgents = ["Breach", "Brimstone", "Cypher", "Jett", "Omen", "Phoenix", "Raze", "Sage", "Sova", "Viper"]

    ranAgent = random.choice(valorantAgents)
    ranAgent1 = random.choice(valorantAgents)
    ranAgent2 = random.choice(valorantAgents)
    ranAgent3 = random.choice(valorantAgents)
    ranAgent4 = random.choice(valorantAgents)

    valTeam = [ranAgent, ranAgent1, ranAgent2, ranAgent3, ranAgent4]

    while len(valTeam) != len(set(valTeam)):
        valTeam = [random.choice(valorantAgents), random.choice(valorantAgents), random.choice(valorantAgents), random.choice(valorantAgents), random.choice(valorantAgents)]
    
    print(valTeam)

    await ctx.send(f'{valTeam[0]}\n{valTeam[1]}\n{valTeam[2]}\n{valTeam[3]}\n{valTeam[4]}')

@client.command()
async def Val(ctx):
    valorantAgents = ["Breach", "Brimstone", "Cypher", "Jett", "Omen", "Phoenix", "Raze", "Sage", "Sova", "Viper"]

    ranAgent = random.choice(valorantAgents)
    ranAgent1 = random.choice(valorantAgents)
    ranAgent2 = random.choice(valorantAgents)
    ranAgent3 = random.choice(valorantAgents)
    ranAgent4 = random.choice(valorantAgents)

    valTeam = [ranAgent, ranAgent1, ranAgent2, ranAgent3, ranAgent4]

    while len(valTeam) != len(set(valTeam)):
        valTeam = [random.choice(valorantAgents), random.choice(valorantAgents), random.choice(valorantAgents), random.choice(valorantAgents), random.choice(valorantAgents)]
    
    print(valTeam)

    await ctx.send(f'{valTeam[0]}\n{valTeam[1]}\n{valTeam[2]}\n{valTeam[3]}\n{valTeam[4]}')

@client.command()
async def _help(ctx):
    await ctx.send(" List of Commands: \n \n !league (Gives you a random team composition) \n \n !leaguetop !leaguemid etc. (Gives you a random top laner for LoL) \n \n !val or !valorant (Gives you a random team composition for Valorant)")



client.run('NzAyMjg0MDEzNzA3OTg1MDE4.Xp9zDQ.6q2HW5D9GCRyVmviVqoh8Wvu8YI')

