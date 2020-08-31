from classes.game import Person, Bcolors

magic = [{"name": "Fire", "cost": 10, "dmg": 60},
         {"name": "Lighting", "cost": 15, "dmg": 80},
         {"name": "Water", "cost": 12, "dmg": 50}]

player = Person(460, 65, 60, 34, magic)

print("Attack Damage:", player.generate_damage())
print("Spell Damage:", player.generate_spell_damage(1))
print("Spell Damage:", player.generate_spell_damage(2))