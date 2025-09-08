import discord, enum
from discord.ext import commands
from Character import Character

Characters = []

class isHidden(str, enum.Enum):
	Yes = "Yes"
	No = "No"

Specials = [
	# {"name": "", "health": , "spell_points": , "defence": ,weapon": "", "armor": "" "icon": "", "description": ""}
	{"name": "Drozd Sandpiper", "health": 80, "spell_points": 5, "defence": 0, "weapon": "Long-Handed Wrench", "armor": None, "icon": "https://media.discordapp.net/attachments/467737191934853132/1409205861175398510/224_20250824190036.png?ex=68ac88bb&is=68ab373b&hm=7aee9cd0ded398d7c964b3085bd8d208646dc65eb03da52de32c1fb6801b4316&=&format=webp&quality=lossless&width=868&height=868", "description": "An anthropomorphic lynx of Russian heritage. He spent his childhood living in the Nordic part which made him be more resilient against cold and harsh weather."},
	{"name": "Painiac", "health": 80, "spell_points": 5,  "defence": 0, "weapon": None, "armor": None, "icon": "https://media.discordapp.net/attachments/467737191934853132/1406556064253743134/i.png?ex=68a2e4ea&is=68a1936a&hm=fc75c27ee5f2247737b6a6a269a327d3126f8f324d81c8c0bd82911e0abb16ef&=&format=webp&quality=lossless&width=288&height=288", "description": "Random sheriff who have slept on Drozd`s girlfriend couch and snored really loud. "},
	{"name": "ChocoCream", "health": 80, "spell_points": 5,  "defence": 0, "weapon": "Scarf-Hands", "armor": None, "icon": "https://media.discordapp.net/attachments/467737191934853132/1409197480767262882/226_20250824182644.png?ex=68ac80ed&is=68ab2f6d&hm=79c2e1ad5e629972cb8b7c23869b717c34d8b5338fcdd71c21abd27ea4edbe22&=&format=webp&quality=lossless&width=872&height=868", "description": "An anthropomorphic rabbit with a kind soul, armed with scarf-hands good for combat and utility."},
	{"name": "Zakuro Hoshizaki", "health": 80, "spell_points": 5,  "defence": 0, "weapon": "Katanas", "armor": None, "icon": "https://media.discordapp.net/attachments/467737191934853132/1409312156045807707/228_20250825020309.png?ex=68acebb9&is=68ab9a39&hm=ad3fc138339681ce39458e30ae2333fbe10e2ecfa017f16a2f4892f2edf2ad62&=&format=webp&quality=lossless", "description": "bruh, your icon outline sucks, dude.."},
	{"name": "Charlatan", "health": 55, "spell_points": 7, "defence": 0, "weapon": "Star Sigil", "armor": "Comedy Mask", "icon": "https://media.discordapp.net/attachments/467737191934853132/1409198647148675152/227_20250824183204.png?ex=68ac8203&is=68ab3083&hm=cd429483185fde506ea054987e0affe31acd85f4afd10cd67a2d423189cf8d62&=&format=webp&quality=lossless&width=553&height=781", "description": "A jester cursed by blood to a mask of comedic despair, with only hanging on to existence by a mere thread."},
	{"name": "Magnesium", "health": 50, "spell_points": 15, "defence": 0, "weapon": None, "armor": None, "icon": "https://media.discordapp.net/attachments/467737191934853132/1409133996780163204/225_20250824141433.png?ex=68ac45cd&is=68aaf44d&hm=c8a70723e0b3308718b5406bb57af1b784a43fc6d92b56a55a710da6c21a69a6&=&format=webp&quality=lossless&width=337&height=371", "description": "Magnesium is very cheerful and positive egoed but also has very weird behavior you will see her staring into other cats souls deeply, randomly loudly sneezing like your average father, eating anything on the floor with the 5 second rule. Whenever she cannnot reach something she uses her tail to become taller to reach but if that does not work she'll get frustrated and get some stairs. She has intrusive thoughts of eating, biting and touching anything. She likes to scare other cats by holding a knife as a joke she would not actually stab someone unless she despises you."},
	{"name": "Frisk", "health": 20, "spell_points": 5, "defence": 0, "weapon": "Stick", "armor": "Bandage", "icon": "https://media.discordapp.net/attachments/467737191934853132/1409317800421363732/229_20250825022534.png?ex=68acf0fb&is=68ab9f7b&hm=da716295a0eaced15e1efffd4eacbb78b962b10b2d8841a866b4086dda4c5681&=&format=webp&quality=lossless&width=777&height=862", "description": "You're filled with.. DETERMINATION. Frisk is a kid with a pacifistic traits and a stick who is able to revive themselves a lot of times during the battle, gaining +1 Defence each death. However, it cannot last for too long..."}
]

battle_card_description_embed = discord.Embed(title="Battle Actions", description='', color = 0x26e1da)
battle_card_description_embed.add_field(name=f'╰┈➤    PRIMARY. "Wastes your character turn and the turn goes to the next character by initiative."', value=f'''
**[ ⚔︎ Attack]** 
"Basic character's ability. Slash, stab, basic spell and etc. Can be used every turn."
╰┈ **[ ↑ Rev Up ]** 
	  "Spell Points can be used to increase a basic attack power. Every three wasted spell points make an extra hit in a turn."

**[ ➢ Talk | Option ]** 
"Sometimes diplomacy might be more efficent than a useless and harmful fight. You also can use any basic action and/or perform something, such as stealing, lockpicking, hacking or other stuff. Can be used every turn."
╰┈ **[ ➢ Equip ]** 
	  "Equipping or uneqipping a part of character equipment helps to change battle strategy. Can be used every turn."

**[ ➢ Defend ]** 
"Grants a character additional Defence, restores an additional spell point and grants -1 Dodge Point. A character is also immune to stuns during defending stance. Can be used every turn."''', inline=False)
battle_card_description_embed.add_field(name=f'╰┈➤    BONUS. "Does not waste the character turn."', value=f'''
**[ ⚒ Item ]** 
"Character uses one item from their inventory. Can be used every turn."

**[ ᶠᶸᶜᵏᵧₒᵤ! Taunt ]**  
"Character taunts an enemy and causes them to target a character for a turn with 50%. A character gets Resistance I. Can be used once per two turns."

**[ ☘︎ Reroll ]** 
"A dice can be rerolled and give a different result. Can be used once in two turns."''', inline=False)

battle_card_embed = discord.Embed(title="Non-Stop Mob Rush", description='Prototype | Bugs may be present', color = 0x26e1da)
battle_card_embed.set_thumbnail(url="https://media.discordapp.net/attachments/1135944138848739379/1402057599830200342/raw.png?ex=68928764&is=689135e4&hm=b053d14bbd68495cc6ab9d26e5f9dd12a439bfe94749c6c9f99af446b62196de&=&format=webp&quality=lossless&width=315&height=315")

class Battle(commands.Cog):
	def __init__(self, bot): 
		self.bot = bot

	@commands.hybrid_command(name="create", description="Creates a character profile.")
	async def create(self, ctx: commands.Context, 
			name: str = "Template", 
			health: int = 80, 
			spell_points: int = 5, 
			defence: int = 0, 
			weapon: str = None, 
			armor: str = None, 
			description: str = "this brotha did not bothered to make their character a description.", 
			notes: str = None) -> None:
		try:
			special_found = False
			if (health == 0 or health < 0) or (spell_points == 0 or spell_points < 0):
				await ctx.send(f'```py\nHealth and/or Spell Points must be a positive number.```')
				print(f'{ctx.author.name} called "create" command, but the character they tried to create had Health and/or Spell Pointsnegative or equal to zero.')
			else:
				for special in Specials:
					if special['name'].lower() == name.lower():
						character = Character.create(special['name'], special['health'], special['spell_points'], special['defence'], special['weapon'], special['armor'], special['description'], None)
						special_found = True
						break
				if not special_found:
					character = Character.create(name, health, spell_points, defence, weapon, armor, description, notes)
				print(f'')
		except Exception as e:
			print(f"\nUnexpected error has happened: {e}")
		else:
			Characters.append(character)
			await ctx.send(f'```py\n{character.name} has been added to the battle card.```')
			print(f'{ctx.author.name} has called "create" command.')
			print(f'Next following character has been created by {ctx.author.name}: \n{character}')

	@commands.hybrid_command(name="character", description="Shows character profile.")
	async def character(self, ctx: commands.Context, name: str) -> None:
		await ctx.defer(ephemeral=True)
		try:
			battle_card_embed = discord.Embed(title="Character Information", description='Prototype | Bugs may be present', color = 0x26e1da)
			character = next(character for character in Characters if character.name == name)
			for special in Specials:
				if special['name'].lower() == character.name.lower():
					battle_card_embed.set_thumbnail(url=special['icon'])
					break
				else:
					battle_card_embed.set_thumbnail(url="https://media.discordapp.net/attachments/1135944138848739379/1402057599830200342/raw.png?ex=68928764&is=689135e4&hm=b053d14bbd68495cc6ab9d26e5f9dd12a439bfe94749c6c9f99af446b62196de&=&format=webp&quality=lossless&width=315&height=315")
		except:
			await ctx.send(f"```ERROR: Character isn't found.```")
			print(f'{ctx.author.name} has called "character" command, but the character was not found.')
			return
		def create_bar(filled, total):
			filled_points = int(filled * total)
			return "▰" * filled_points + "▱" * (total - filled_points)

		if character.health <= character.max_health:
			health_bar = create_bar(character.health / character.max_health, 8)
			spell_points_bar = create_bar(character.spell_points / character.max_spell_points, 5)
		elif character.health > character.max_health:
			health_bar = create_bar(character.max_health / character.max_health, 8)
			spell_points_bar = create_bar(character.max_spell_points / character.max_spell_points, 5)

		battle_card_embed.add_field(
			name=f'<:character:1402253467153596527>  {character.name}',
			value=(
				f'✦•·····• **Description** •·····•✦\n{character.description}\n'
				f'\n✦•·····• **Characteristics** •·····•✦\n'
				f'**Health**: [{health_bar}] {character.health}/{character.max_health} <:HP:1340365975429578812>\n'
				f'**Spell Points**: [{spell_points_bar}] {character.spell_points}/{character.max_spell_points} <:DMG:1340365966323744819>\n'
				f'**Defence**: {character.defence} <:DEF:1340365967963852810>\n'
				f'\n✦•·····• **Equipment** •·····•✦\n'
				f'**<:melee:1402254796022616115> Weapon**: {character.weapon} \n**<:shield_ll:1402254810312478780> Armor**: {character.armor} \n'
				f'\n✦•·····• **Notes** •·····•✦\n{character.notes}'
			),
			inline=True
			)
		await ctx.send(embed=battle_card_embed)
		print(f'{ctx.author.name} has called "character" command and opened {character.name} profile.')

	@commands.hybrid_command(name="battlecard", description="Shows battlecard. (obvious)")
	async def battlecard(self, ctx: commands.Context, show_actions_description = "yes") -> None: 
		for character in Characters:
			battle_card_embed.add_field(
				name=f'<:character:1402253467153596527>  {character.name}',
				value=(
					f'✦•·····• **Characteristics** •·····•✦\n'
					f'**Health**: {character.health}/{character.max_health} <:HP:1340365975429578812>\n'
					f'**Spells**: {character.spell_points}/{character.max_spell_points} <:DMG:1340365966323744819>\n'
					f'**Defence**: {character.defence} <:DEF:1340365967963852810>\n'
					f'\n✦•·····• **Equipment** •·····•✦\n'
					f'**<:melee:1402254796022616115> Weapon**: {character.weapon} \n**<:shield_ll:1402254810312478780> Armor**: {character.armor} \n'
					f'\n✦•·····• **Notes** •·····•✦\n{character.notes}'
				),
				inline=True
			)
		await ctx.send(embed=battle_card_embed)
		battle_card_embed.clear_fields()
		if show_actions_description.lower() == "yes":
			await ctx.send(embed=battle_card_description_embed)
		print(f'{ctx.author.name} has called "battlecard" command.')

	@commands.hybrid_command(name="change", description="Changes characteristic of a character.")
	async def change(self, ctx: commands.Context, name: str, characteristic, value) -> None:
		try:
			character = next(character for character in Characters if character.name == name)
		except:
			await ctx.send(f"```ERROR: Character isn't found.```")
			print(f'{ctx.author.name} has called "change" command, but the character was not found.')
			return
		if characteristic in ["health", "spell_points"]:
			try:
				value = int(value)
			except ValueError:
				await ctx.send(f"```VALUE_ERROR: Must be integer.```")
		change_message = ""
		if characteristic == 'health':
			character.change(health=value)  
			change_message = f"got healed by {value} health points." if value > 0 else f"has received {abs(value)} damage." if value < 0 else "didn't feel anything?"
			await ctx.send(f"```py\n{name} {change_message}```")
		elif characteristic == 'spell_points':  
			character.change(spell_points=value)
			change_message = f"has restored {value} spell points." if value > 0 else f"has wasted {abs(value)} spell points." if value < 0 else "didn't feel anything?"
			await ctx.send(f"```py\n{name} {change_message}```")
		elif characteristic in ["name", "description", "max_health", "max_spell_points", "weapon", "armor", "notes"]:
			character.set(**{characteristic: int(value) if characteristic in ["max_health", "max_spell_points"] else value})
			await ctx.send(f"```py\n{name} {characteristic} has been updated.```")
		print(f'{ctx.author.name} has called "change" command and changed {characteristic} of {character.name} to/by {value}.')

	@commands.hybrid_command(name="delete", description="Deletes a character profile.")
	async def delete(self, ctx: commands.Context, name: str) -> None:
		character_name = name
		for character, char in enumerate(Characters):
			if char.name == name:
				print(f'{ctx.author.name} has called "delete" command and removed {char.name}.')
				del Characters[character]
				await ctx.send(f'''```py\n"{character_name}" has left the battle.```''')

async def setup(bot: commands.Bot): 
	await bot.add_cog(Battle(bot))

if __name__ == "__main__":
	character = Character.create("Drozd", 80, 5, 0, "Long-Handed Wrench", "None",  "An anthropomorphic lynx of Russian heritage. He spent his childhood living in the Nordic part which made him be more resilient against cold and harsh weather.", "None")
	character.set(armor = "Knight Armor", notes = "hello world")
	character.change(health = -21, spell_points = -2)
	Characters.append(character)
	for character in Characters:
		print(str(character))
