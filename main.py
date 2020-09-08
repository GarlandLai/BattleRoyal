from classes.game import Person, Bcolors
from classes.magic import Spell
from classes.inventory import Item
import random

# Create Black Magic
fire = Spell("Wild Fire", 25, 640, "black")
lightning = Spell("Lightning Strike", 30, 700, "black")
water = Spell("Tsunami", 20, 600, "black")
meteor = Spell("Meteor Shower", 40, 1200, "black")
quake = Spell("Earthquake", 28, 850, "black")

# Create White Magic
cure = Spell("Cure", 25, 620, "white")
cura = Spell("Cura", 32, 1500, "white")

# Create some items
potion = Item("Potion", "potion", "Heals 50 HP", 250)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 500)
ultrapotion = Item("Ultra Potion", "potion", "Heals 500 HP", 1000)
elixer = Item("Elixer", 'elixer', "Fully restores HP/MP of one party member", 9999)
megaelixer = Item("MegaElixer", 'elixer', "Fully restores HP/MP of one party member", 9999)

grenade = Item("Grenade", 'attack', "Deals 500 damage", 500)


player_spells = [fire, lightning, water, meteor, quake, cure, cura]
player_items = [{"item": potion, "quantity": 15}, {"item": hipotion, "quantity": 5},
                {"item": ultrapotion, "quantity": 5}, {"item": elixer, "quantity": 5},
                {"item": megaelixer, "quantity": 2}, {"item": grenade, "quantity": 5}]

# Instantiate People
player1 = Person("John: ", 3260, 130, 340, 34, player_spells, player_items)
player2 = Person("Leah: ", 4160, 140, 280, 34, player_spells, player_items)
player3 = Person("Joe : ", 3890, 170, 300, 34, player_spells, player_items)

enemy1 = Person("Imp    ", 1250, 130, 560, 325, [], [])
enemy2 = Person("Magus  ", 11200, 700, 525, 25, [], [])
enemy3 = Person("Imp    ", 1250, 130, 560, 325, [], [])

players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]

running = True
i = 0

print(Bcolors.FAIL + Bcolors.BOLD + "Get Ready! The battle begins!" + Bcolors.ENDC)

while running:
    print("======================")
    print("\n")
    print("NAME                HP                                      MP          ")
    # Printing out each player
    for player in players:
        player.get_stats()
    print("\n")

    for enemy in enemies:
        enemy.get_enemy_stats()

    for player in players:
        player.choose_action()
        choice = input("    Choose action: ")
        index = int(choice) - 1

        if index == 0:
            dmg = player.generate_damage()
            # Player choose which enemy to attack
            enemy = player.choose_target(enemies)
            enemies[enemy].take_damage(dmg)

            print(Bcolors.OKBLUE + Bcolors.BOLD + "You attacked " + enemies[enemy].name + " for", dmg,
                  "points of damage." + Bcolors.ENDC)

            if enemies[enemy].get_hp() == 0:
                print(enemies[enemy].name + " has died!")
                del enemies[enemy]

        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("    Choose magic: ")) - 1

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
                enemy = player.choose_target(enemies)

                enemies[enemy].take_damage(magic_dmg)
                print(Bcolors.OKBLUE + "\n" + spell.name + "deals", str(magic_dmg), "points of damage to " +
                      enemies[enemy].name, Bcolors.ENDC)

                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name + " has died!")
                    del enemies[enemy]

        elif index == 2:
            player.choose_item()
            item_choice = int(input("    Choose item: ")) - 1

            if item_choice == -1:
                continue

            # Check to make sure we have item
            if player.items[item_choice]["quantity"] == 0:
                print(Bcolors.FAIL + "\n" + "None left...." + Bcolors.ENDC)
                continue

            # Reduces items when used
            item = player.items[item_choice]["item"]
            player.items[item_choice]["quantity"] -= 1

            if item.type == "potion":
                player.heal(item.prop)
                print(Bcolors.OKGREEN + "\n" + item.name + "heals for", str(item.prop), "HP", Bcolors.ENDC)

            elif item.type == "elixer":

                if item.name == "MegaElixer":
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp
                else:
                    player.hp = player.maxhp
                    player.mp = player.maxmp
                print(Bcolors.OKGREEN + "\n" + item.name + "fully restores HP/MP" + Bcolors.ENDC)

            elif item.type == "attack":
                enemy = player.choose_target(enemies)

                enemies[enemy].take_damage(item.prop)
                print(Bcolors.FAIL + "\n" + item.name + " deals", str(item.prop), "points of damage to " +
                      enemies[enemy].name + Bcolors.ENDC)

                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name + " has died!")
                    del enemies[enemy]

    enemy_choice = 1
    # Enemy randomly attacks a player. Will select 0,1,2 but not 3 in below case.
    target = random.randrange(0, 3)
    enemy_dmg = enemies[0].generate_damage()
    players[target].take_damage(enemy_dmg)
    print(Bcolors.FAIL + Bcolors.BOLD + "Enemy attacks", players[target].name, "for", enemy_dmg,
          "points of damage" + Bcolors.ENDC)

    defeated_enemies = 0
    defeated_player = 0

    for enemy in enemies:
        if enemy.get_hp() != 0:
            if enemy.get_hp() == 0:
                defeated_enemies += 1

    for player in players:
        if player.get_hp() == 0:
            defeated_player += 1

    if defeated_enemies == 2:
        print(Bcolors.OKGREEN + "YOU HAVE DEFEATED THE ENEMY. YOU WIN!" + Bcolors.ENDC)
        running = False

    elif defeated_player == 2:
        print(Bcolors.FAIL + "YOU HAVE BEEN DEFEATED BY YOUR ENEMIES!" + Bcolors.ENDC)
        running = False
