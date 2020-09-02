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
    player.choose_action()
    choice = input("Choose action:")
    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for", dmg, "points of damage. Enemy HP is", enemy.get_hp())

    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg, ".", "Player HP is", player.get_hp())