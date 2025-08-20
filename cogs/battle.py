import discord, enum
import utils as tool
from discord.ext import commands
from .Character import Character

Characters = []

class isHidden(str, enum.Enum):
	Yes = "Yes"
	No = "No"

Specials = [
	# {"name": "", "weapon": "", "icon": "", "description": ""}
	{"name": "Drozd Sandpiper", "weapon": "Long-Handed Wrench", "icon": "https://media.discordapp.net/attachments/467737191934853132/1406368863922294946/image.png?ex=68a23692&is=68a0e512&hm=9cf484c1b79c80370f030d2c3d80a30df37229757326b1b070f2121c3a8eed8a&=&format=webp&quality=lossless&width=868&height=868", "description": "An anthropomorphic lynx of Russian heritage. He spent his childhood living in the Nordic part which made him be more resilient against cold and harsh weather."},
	{"name": "Painiac", "weapon": None, "icon": "https://media.discordapp.net/attachments/467737191934853132/1406556064253743134/i.png?ex=68a2e4ea&is=68a1936a&hm=fc75c27ee5f2247737b6a6a269a327d3126f8f324d81c8c0bd82911e0abb16ef&=&format=webp&quality=lossless&width=288&height=288", "description": None},
	{"name": "ChocoCream", "weapon": "Scarf-Hands", "icon": "https://media.discordapp.net/attachments/467737191934853132/1406571800602869931/Mack_n_Choco_again_yay.png?ex=68a2f392&is=68a1a212&hm=8a5b63d68fe1378e55eeb98fcdd54fc8f8f1352c6df59cadde23c18d5db67651&=&format=webp&quality=lossless&width=700&height=697", "description": "An anthropomorphic rabbit with a kind soul, armed with scarf-hands good for combat and utility."},
	{"name": "Zakuro Hoshizaki", "weapon": "Katanas", "icon": "https://media.discordapp.net/attachments/467737191934853132/1406574708492734584/Simp.png?ex=68a2f647&is=68a1a4c7&hm=5a4a897e61dbc08f954f1b09a9b853c3bb7483bd194b78b9f85b108f58e5e702&=&format=webp&quality=lossless&width=754&height=781", "description": None}
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
					character.description = special['description'] if special['description'] is not None else "this brotha did not bothered to make their character a description."
					character.weapon = special['weapon'] if special['weapon'] is not None else None
					break
				else:
					battle_card_embed.set_thumbnail(url="https://media.discordapp.net/attachments/1135944138848739379/1402057599830200342/raw.png?ex=68928764&is=689135e4&hm=b053d14bbd68495cc6ab9d26e5f9dd12a439bfe94749c6c9f99af446b62196de&=&format=webp&quality=lossless&width=315&height=315")
		except:
			await ctx.send(f"```ERROR: Character isn't found.```")
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
					f'**Spell Points**: {character.spell_points}/{character.max_spell_points} <:DMG:1340365966323744819>\n'
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
		print(f'{ctx.author.name} has called "change" command and changed {characteristic} of {character.name} to {value}.')

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
