import sys
sys.path.insert(1, "C:/Users/Drozd/Desktop/Kefirka/cogs")

from random import randint
import discord, os, tracemalloc, asyncio, datetime, colorama
import utils as tool
from utils import current_date, formatted_current_date, colors
from dotenv import load_dotenv
from discord.ext import commands, tasks

load_dotenv()
tracemalloc.start()
colorama.init()

cogs_list = [
	'battle',
	'general'
]

class Kefirka(commands.Bot):
	def __init__(self):
		intents = discord.Intents.default()
		intents.message_content = True
		intents.messages = True
		self.prefix = os.getenv('PREFIX')
		self.token = os.getenv('TOKEN')
		self.guild_id = int(os.getenv('GUILD_ID'))
		self.channel_id = int(os.getenv('CHANNEL_ID'))
		self.version = "v1.0.1-prototype"
		super().__init__(command_prefix=self.prefix, 
						intents=intents)

	async def load_extensions(self):
		print(f"\n{colors['cyan']}Extensions being installed into the main.py{colors['end']}")
		for cog in cogs_list:
			try:
				await self.load_extension(f'cogs.{cog}')
				print(f"—— {colors['yellow']}cogs.{cog}{colors['end']} installed. ——")
			except Exception as e:
				print(f"{colors['red']}An error occured during extension load{colors['end']}: {e}")
		print(f"{colors['cyan']}Finished installing.{colors['end']}")

	async def on_ready(self):
		print((
			f"\n{colors['cyan']}—— Session launched as ——{colors['end']}\n"
			f"{colors['yellow']}Username{colors['end']}: {self.user.name}\n"
			f"{colors['yellow']}ID{colors['end']}: {self.user.id}\n"
			f"{colors['yellow']}Date{colors['end']}: {formatted_current_date}\n"
			f"{colors['yellow']}Version{colors['end']}: {self.version}"
			f"\n{colors['cyan']}———ATTR_TYPES———{colors['end']}\n"
			f"{colors['yellow']}Token{colors['end']}: {type(self.token)}\n"
			f"{colors['yellow']}Prefix{colors['end']}: {type(self.prefix)}\n"
			f"{colors['yellow']}Guild ID{colors['end']}: {type(self.guild_id)}\n"
			f"{colors['yellow']}Channel ID{colors['end']}: {type(self.channel_id)}\n"
			f"{colors['cyan']}———————————{colors['end']}\n"
			f"\n{colors['cyan']}———LOGS———{colors['end']}"
			))
		channel = self.get_channel(self.channel_id)
		await self.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name="how people drink kefir."))
		# await channel.send("boop")

	async def on_guild_join(self, guild):
		for channel in guild.text_channels:
			if channel.permissions_for(guild.me).send_messages:
				await channel.send(embed=general.about_embed)
				break

	async def setup_hook(self):
		try:
			self.tree.copy_global_to(guild=discord.Object(id=self.guild_id))
			await self.tree.sync()
			print(f"\n{colors['cyan']}Command tree has been synced with the guild.")
		except Exception as e:
			await ctx.send(f"An error occured during syncing: {e}")

	async def on_message(self, message):
		await self.process_commands(message)

class HelpCommand(commands.MinimalHelpCommand):
	attributes = {
		'name': "help",
		'aliases': ["helpme"]
	}
	async def send_pages(self):
		destination = self.get_destination()
		for page in self.paginator.pages:
			embed = discord.Embed(description=page, color=0x26e1da)
			await destination.send(embed=embed)

	async def send_error_message(self, error):
		embed = discord.Embed(title="ERROR", description=error, color=discord.Color.red())
		destination = self.get_destination()
		await destination.send(embed=embed)

async def main():
	bot = Kefirka()
	print(f"\n{colors['cyan']}Bot instance created.{colors['end']}")
	bot.help_command = HelpCommand(command_attrs=HelpCommand.attributes)
	print(f"{colors['cyan']}'/help' command has been setup.{colors['end']}")
	await bot.load_extensions()
	try:
		await bot.start(bot.token)
	except KeyboardInterrupt:
		await bot.close()

if __name__ == "__main__":
		print(f"\n{colors['cyan']}Launching{colors['end']} {colors['yellow']}main.py{colors['end']}")
		try:
			asyncio.run(main())
		except Exception as e:
			print("An error occured: {e}")
