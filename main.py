from classes.game import Person, Bcolors
from classes.magic import Spell

# Create Black Magic
fire = Spell("Wild Fire", 12, 120, "black")
lightning = Spell("Lightning Strike", 15, 150, "black")
water = Spell("Tsunami", 10, 100, "black")
meteor = Spell("Meteor Shower", 20, 200, "black")
quake = Spell("Earthquake", 14, 140, "black")

# Create White Magic
heal = Spell("Health Potion", 12, 120, "white")
max_heal = Spell("Max Heal Potion", 18, 200, "white")

# Instantiate People
player = Person(460, 65, 60, 34, [fire, lightning, water, meteor, quake, heal, max_heal])

enemy = Person(1200, 65, 45, 25, [fire, lightning, water, meteor, quake])

running = True
i = 0

print(Bcolors.FAIL + Bcolors.BOLD + "Get Ready! The battle begins!" + Bcolors.ENDC)

while running:
    print("======================")
    player.choose_action()
    choice = input("Choose action:")
    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print(Bcolors.OKBLUE + Bcolors.BOLD + "You attacked for", dmg, "points of damage." + Bcolors.ENDC)
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose magic:")) - 1

        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_damage()

        current_mp = player.get_mp()

        if spell.cost > current_mp:
            print(Bcolors.FAIL + "\nNot enough MP\n" + Bcolors.ENDC)
            continue

        player.reduce_mp(spell.cost)
        enemy.take_damage(magic_dmg)
        print(Bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "points of damage" + Bcolors.ENDC)

    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print(Bcolors.FAIL + Bcolors.BOLD + "Enemy attacks for", enemy_dmg, "points of damage" + Bcolors.ENDC)

    print("_______________________________")
    print("Enemy HP:", Bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + Bcolors.ENDC + "\n")
    print("Your HP:", Bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + Bcolors.ENDC + "\n")
    print("Your MP:", Bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + Bcolors.ENDC + "\n")

    if enemy.get_hp() == 0:
        print(Bcolors.OKGREEN + "YOU HAVE DEFEATED THE ENEMY. YOU WIN!" + Bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(Bcolors.FAIL + "YOU HAVE 0 HP. YOU HAVE BEEN DEFEATED!" + Bcolors.ENDC)
        running = False
