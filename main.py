from classes.game import Person, Bcolors

magic = [{"name": "Fire", "cost": 10, "dmg": 60},
         {"name": "Lighting", "cost": 10, "dmg": 60},
         {"name": "Water", "cost": 10, "dmg": 60}]

player = Person(460, 65, 60, 34, magic)

print(player.generate_damage())
print(player.generate_damage())
print(player.generate_damage())
