import discord, json
from random import choice
from discord.ext import commands

with open('cogs/ping_facts.json', 'r', encoding='UTF-8') as local_file:
	ping_easter_eggs = json.load(local_file)["ping_facts"]
	easter_eggs_amount = len(ping_easter_eggs)

about_embed = discord.Embed(title="About me!", description='', color = 0x26e1da)
about_embed.set_thumbnail(url='https://media.discordapp.net/attachments/467737191934853132/1407755720354435224/image.png?ex=68a7422e&is=68a5f0ae&hm=7481e83cf1a564cf8aa3b4241e0803effd007caa10782f72170515f15c984056&=&format=webp&quality=lossless&width=868&height=868')
about_embed.add_field(name='', value='Hello, I am a very nutricious and delicious drink called Kefir! Though my name is **Kefirka**... nevermind. Just in case, if you have any suggestion for me or found a bug, you can contact the developer directly or through support server called **The Web Realm**! *(the button link is still in W.I.P, uhm, oopsie!)*. In any case, I am here to: ', inline=False)
about_embed.add_field(name='Roleplay', value='Enchance your roleplays sessions by adding several "game" mechanics, such as character profiles', inline=True)
about_embed.add_field(name='Fun (W.I.P)', value='Add some funny commands to entertain you', inline=True)
about_embed.add_field(name='Moderation (W.I.P)', value='Add some moderation utility to ensure safety of the server', inline=True)
about_embed.add_field(name='', value='I will have much more features with time, just be patient!', inline=False)
about_embed.add_field(name='', value='-# k!help for a list of available commands', inline=False)
about_embed.add_field(name='', value='-# The bot is currently a prototype, not so much exist for now and a lot features may change in the future. Bugs also may be present.', inline=False)
about_embed.set_footer(text="made by CrazyDrozd", icon_url="https://media.discordapp.net/attachments/467737191934853132/1407759570641883156/f0d79c2a8a60e972b0125f0d74222f90.png?ex=68a745c4&is=68a5f444&hm=c4e4a294d4e417796f216c923e7aad8c74472f1251f97d3f9f910217f986e11f&=&format=webp&quality=lossless&width=207&height=207")
about_embed.set_author(name="Kefirka", icon_url="https://media.discordapp.net/attachments/467737191934853132/1407755720354435224/image.png?ex=68a7422e&is=68a5f0ae&hm=7481e83cf1a564cf8aa3b4241e0803effd007caa10782f72170515f15c984056&=&format=webp&quality=lossless&width=868&height=868")

class General(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.hybrid_command(name="about", description="Shows information of the bot.")
	async def about(self, ctx: commands.Context) -> None:
		await ctx.send(embed=about_embed)
		print(f'{ctx.author.name} has called "about" command.')

	@commands.hybrid_command(name="ping", description="Shows latency of the bot with an easter egg.", aliases=['Ping', 'pong', 'Pong', 'latency', 'Latency', 'ms'])
	async def ping(self, ctx: commands.Context) -> None:
		ping_fact = choice(ping_easter_eggs)
		await ctx.send(f'*({round(self.bot.latency * 1000)}ms)* {ping_fact}')
		print(f'{ctx.author.name} has called "ping" command.')

	@commands.hybrid_command(name="eastereggs", description="Shows the amount of easter eggs.")
	async def eastereggs(self, ctx: commands.Context) -> None:
		await ctx.send(f'There are **{easter_eggs_amount}** easter eggs in **k!ping** at the moment.')
		print(f'{ctx.author.name} has called "eastereggs" command.')

	@commands.hybrid_command(name="ip", description="Generates a completely random IP.")
	async def ip(self, ctx: commands.Context) -> None:
		sentence = []
		number = randint(100, 255)
		sentence.append(number)
		for i in range(3):
			number = randint(1, 255)
			sentence.append(number)
		sentence_string = '.'.join(map(str, sentence))
		await ctx.send(f'{sentence_string}')
		print(f'{ctx.author.name} has called "ip" command.')

async def setup(bot: commands.Bot):
	await bot.add_cog(General(bot))
