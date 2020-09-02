from classes.game import Person, Bcolors

magic = [{"name": "Fire", "cost": 12, "dmg": 60},
         {"name": "Lighting", "cost": 15, "dmg": 80},
         {"name": "Water", "cost": 10, "dmg": 50}]

player = Person(460, 65, 60, 34, magic)

print("Attack Damage:", player.generate_damage())
print("Spell Damage:", player.generate_spell_damage(1))
print("Spell Damage:", player.generate_spell_damage(2))

enemy = Person(1200, 65, 45, 25, magic)

running = True
i = 0

print(Bcolors.FAIL + Bcolors.BOLD + "AN ENEMY ATTACKS!" + Bcolors.ENDC)

while running:
    print("======================")
    player.choose_magic()
    choice = input("Choose action:")
    index = int(choice) - 1

    print("You chose", player.get_spell_name(int(index)))

    running = False
