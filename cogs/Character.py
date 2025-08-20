class Character:
	def __init__(self, 
					name: str = "Template", 
					health: int = 80, 
					spell_points: int = 5, 
					defence: int = 0, 
					weapon: str = None, 
					armor: str = None, 
					description: str = "this brotha did not bothered to make their character a description.", 
					notes: str = None):
		self.name = name
		self.health = health
		self.max_health = health
		self.spell_points = spell_points
		self.max_spell_points = spell_points
		self.defence = defence
		self.weapon = weapon
		self.armor = armor
		self.description = description
		self.notes = notes
		
	@staticmethod
	def create(name: str = "Template", 
					health: int = 80, 
					spell_points: int = 5, 
					defence: int = 0, 
					weapon: str = None, 
					armor: str = None, 
					description: str = "this brotha did not bothered to make their character a description.", 
					notes: str = None):
		return Character(name, health, spell_points, defence, weapon, armor, description, notes)

	def set(self, **kwargs):
		for key, value in kwargs.items():
			if hasattr(self, key):
				setattr(self, key, value)
			else:
				print(f"{key} is not an existing attribute of a class.")

	def change(self, health: int = None, spell_points: int = None):
		def adjust_value(current_value, change_amount):
			return current_value + change_amount
		if health is not None:
			self.health = adjust_value(self.health, health)
		if spell_points is not None:
			self.spell_points = adjust_value(self.spell_points, spell_points)

	def __str__(self):
		return f'''<Character>
	Name | {self.name}
	Description | {self.description}
	Health | {self.health}/{self.max_health}
	Spell Points | {self.spell_points}/{self.max_spell_points}
	Defence | {self.defence}
	Weapon | {self.weapon}
	Armor | {self.armor}
	Notes | {self.notes}
	'''
	
if __name__ == "__main__":
	Characters = []
	character = Character.create("Drozd", 80, 5, 0, "Long-Handed Wrench", "None",  "An anthropomorphic lynx of Russian heritage. He spent his childhood living in the Nordic part which made him be more resilient against cold and harsh weather.", "None")
	character.set(armor = "Knight Armor", notes = "hello world")
	character.change(health = -21, spell_points = -2)
	Characters.append(character)
	for character in Characters:
		print(str(character))
