from classes.game import Person, Bcolors
from classes.magic import Spell
from classes.inventory import Item

# Create Black Magic
fire = Spell("Wild Fire", 12, 120, "black")
lightning = Spell("Lightning Strike", 15, 150, "black")
water = Spell("Tsunami", 10, 100, "black")
meteor = Spell("Meteor Shower", 20, 200, "black")
quake = Spell("Earthquake", 14, 140, "black")

# Create White Magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")

# Create some items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
ultrapotion = Item("Ultra Potion", "potion", "Heals 500 HP", 500)
elixer = Item("Elixer", 'elixer', "Fully restores HP/MP of one party member", 9999)
megaelixer = Item("MegaElixer", 'elixer', "Fully restores HP/MP of one party member", 9999)

grenade = Item("Grenade", 'attack', "Deals 500 damage", 500)


player_spells = [fire, lightning, water, meteor, quake, cure, cura]
player_items = [potion, hipotion, ultrapotion, elixer, megaelixer, grenade]

# Instantiate People
player = Person(460, 65, 60, 34, player_spells, player_items)
enemy = Person(1200, 65, 45, 25, [], [])

running = True
i = 0

print(Bcolors.FAIL + Bcolors.BOLD + "Get Ready! The battle begins!" + Bcolors.ENDC)

while running:
    print("======================")
    player.choose_action()
    choice = input("Choose action: ")
    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print(Bcolors.OKBLUE + Bcolors.BOLD + "You attacked for", dmg, "points of damage." + Bcolors.ENDC)
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose magic: ")) - 1

        if magic_choice == -1:
            continue

        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_damage()

        current_mp = player.get_mp()

        if spell.cost > current_mp:
            print(Bcolors.FAIL + "\nNot enough MP\n" + Bcolors.ENDC)
            continue

        player.reduce_mp(spell.cost)

        if spell.type == "white":
            player.heal(magic_dmg)
            print(Bcolors.OKBLUE + "\n" + spell.name + " heals for ", str(magic_dmg), "HP", Bcolors.ENDC)
        elif spell.type == "black":
            enemy.take_damage(magic_dmg)
            print(Bcolors.OKBLUE + "\n" + spell.name + "deals", str(magic_dmg), "points of damage", Bcolors.ENDC)

    elif index == 2:
        player.choose_item()
        item_choice = int(input("Choose item: ")) - 1

        if item_choice == -1:
            continue

        item = player.items[item_choice]

        if item.type == "potion":
            player.heal(item.prop)
            print(Bcolors.OKGREEN + "\n" + item.name + "heals for", str(item.prop), "HP", Bcolors.ENDC)

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