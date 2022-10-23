import time
from weapon import Weapon
from random import randint
import json
import random
from colorama import Fore
import os

possessions = json.load(open('varu.json', 'r'))
youssefux_blade = Weapon("Lame de Youssefux", 15, "melee", 5)
ismux_staff = Weapon("Baton de Ismux", 10, "magic", 5)
baka_bat = Weapon("Le bat des baka", 20, "heavy", 10)
bae_hammer = Weapon("Bae Hammer", 26, "heavy", 15)
hand_of_bae = Weapon("La main", 5, "light", 8)
bibost_dagger = Weapon("La dague des Bibost", 11, "light", 13)
kaws_superkodeurs_sharp_keyboard = Weapon("Le Clavier Tranchant De Kaw Et Des SuperKodeurs", 20, "magic", 20)
armes = [youssefux_blade, ismux_staff, baka_bat, bae_hammer, hand_of_bae, bibost_dagger,
         kaws_superkodeurs_sharp_keyboard]
default_characters = []


def wait():
    for i in range(2):
        print("...")
        time.sleep(1)


class Player:
    def __init__(self, pseudo, health, attack, pm, speed):

        global color
        self.protection = False
        self.has_got_weapon = False
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        self.pm = pm
        self.speed = speed
        self.again = False
        if self.pseudo not in possessions:
            possessions[self.pseudo] = {"argent": 0, "items": [hand_of_bae.get_name()]}
            with open("varu.json", "w+") as file:
                json.dump(possessions, file)
        self.money = possessions[self.pseudo]["argent"]
        self.items = possessions[self.pseudo]["items"]

        print(f'Bienvenue au joueur {self.pseudo} !')
        if str(input("Voulez-vous faire un tour à la YouBoutique pour acheter des armes ? (Y/N)")) == 'Y':
            session = Shop(self)
        while not self.has_got_weapon:
            print(f"{self.pseudo}, quelle arme voulez vous ?", end="")
            for i in armes:
                if i.get_name() in self.items:
                    if armes.index(i) == 4:
                        color = Fore.GREEN
                    if armes.index(i) == 3:
                        color = Fore.BLUE
                    if armes.index(i) == 2:
                        color = Fore.YELLOW
                    if armes.index(i) == 1:
                        color = Fore.RED
                    else :
                        color = Fore.LIGHTMAGENTA_EX
                    print(f'{color + i.get_name() + Fore.RESET} ({armes.index(i) + 1})', end=' ')
            var = str(input(" "))
            wait()
            if var == "1" and youssefux_blade.name in self.items:
                self.weapon = youssefux_blade
                print("Votre arme est le", self.weapon.get_name())
                self.has_got_weapon = True

            elif var == "2" and ismux_staff.name in self.items:
                self.weapon = ismux_staff
                print(f"Votre arme est {self.weapon.get_name()} ")
                self.has_got_weapon = True
            elif var == "3" and baka_bat.name in self.items:
                self.weapon = baka_bat
                print(f"Votre arme est {self.weapon.get_name()} ")
                self.has_got_weapon = True

            elif var == "4" and bae_hammer.name in self.items:
                self.weapon = bae_hammer
                print(f"Votre arme est {self.weapon.get_name()} ")
                self.has_got_weapon = True

            elif var == "5" and hand_of_bae.name in self.items:
                self.weapon = hand_of_bae
                print(f"Votre arme est {self.weapon.get_name()} ")
                self.has_got_weapon = True

            elif var == "6" and bibost_dagger.name in self.items:
                self.weapon = bibost_dagger
                print(f"Votre arme est {self.weapon.get_name()} ")
                self.has_got_weapon = True
            elif var == "7" and kaws_superkodeurs_sharp_keyboard.name in self.items:
                self.weapon = kaws_superkodeurs_sharp_keyboard
                print(f"Votre arme est {self.weapon.get_name()} ")
                self.has_got_weapon = True

            else:
                print("Vous ne possédez pas cette arme")

        print(f'Bienvenue au joueur {pseudo} ! \nIl a {health} PV')
        if self.has_got_weapon:
            print(f"et il a une arme : {self.weapon.get_name()} de type {self.weapon.get_type()}\n")
        else:
            print(f'et il fait {self.attack} dégâts !\n')

    def get_pseudo(self):
        return self.pseudo

    def get_health(self):
        return self.health

    def get_attack(self):
        return self.attack

    def get_weapon(self):
        return self.weapon

    def damage(self, damage):
        if self.protection:
            print(
                f"Quelle chance ! {self.get_pseudo()}, vous étiez protégé, vous n'avez reçu que la moitié des dégâts ({damage / 2})")
            self.health -= (damage / 2)
            self.protection = False
        else:
            print(f"Ouch ! {self.get_pseudo()}, vous avez reçu {damage} dégâts !")
            self.health -= damage
            print(f"Et il  reste à {self.pseudo} {self.health} PV")

    def attack_player(self, target, attack):
        target.damage(self.weapon.get_attacks(attack).get_damage_amount())
        if self.weapon.get_attacks(attack).get_consu() is not None:
            self.pm -= self.weapon.get_attacks(attack).get_consu()
            print("Il reste", self.pm, "PM à", self.pseudo, "qui a consommé  pour son attaque")
        if self.weapon.get_attacks(attack).get_counter() is not None:
            self.health -= self.weapon.get_attacks(attack).get_counter()
            print("Il reste ", self.health, "PV à", self.pseudo, " qui a subit des dégâts collatéraux")
        if randint(self.speed, 20) == 20:
            self.again = True

    def has_weapon(self):
        return self.has_got_weapon

    def defend(self):
        self.protection = True

    def get_speed(self):
        return self.speed

    def printstats(self):
        return [self.pseudo, self.health, self.pm, self.speed, self.money]

    def update(self):
        self.money = possessions[self.pseudo]["argent"]
        self.items = possessions[self.pseudo]["items"]


class Partie:
    def __init__(self, player1, player2):
        self.running = True
        self.player1 = player1
        self.player2 = player2

    def play(self):
        tour = randint(0, 1)
        while self.running:
            json.dump((J1.printstats() + J2.printstats()), open('variu.json', 'w+'))
            tour += 1
            if tour % 2 == 1:
                joueur = self.player1
                cible = self.player2
            else:
                joueur = self.player2
                cible = self.player1
            var = int(
                input(f"{joueur.get_pseudo()}, voulez-vous attaquer avec l'attaque "
                      f"{Fore.BLACK + joueur.get_weapon().get_attacks(1).get_name() + Fore.RESET} (1) "
                      f", {Fore.YELLOW + joueur.get_weapon().get_attacks(2).get_name() + Fore.RESET} (2) ou "
                      f"{Fore.RED + joueur.get_weapon().get_attacks(3).get_name() + Fore.RESET} (3), {Fore.MAGENTA}défendre {Fore.RESET} (4) ou n'importe quel nombre pour passer le tour prochain \n"))
            if var == 4:
                joueur.defend()
            elif var not in [1, 2, 3]:
                print('Tour passé')
            else:
                joueur.attack_player(cible, var)
            if randint(joueur.get_speed(), 20) == 20:
                var = int(
                    input(
                        f"Quelle rapdité ! Vous attaquez une seconde fois\n{joueur.get_pseudo()}, voulez-vous attaquer avec l'attaque "
                        f"{Fore.BLACK + joueur.get_weapon().get_attacks(1).get_name() + Fore.RESET} (1) "
                        f" {Fore.YELLOW + joueur.get_weapon().get_attacks(2).get_name() + Fore.RESET} (2) ou "
                        f"{Fore.RED + joueur.get_weapon().get_attacks(3).get_name() + Fore.RESET} (3), {Fore.MAGENTA}défendre {Fore.RESET} (4) ou n'importe quel nombre pour passer le tour prochain \n"))
                if var == 4:
                    joueur.defend()
                else:
                    joueur.attack_player(cible, var)
            if cible.health <= 1:
                print(f'Aïe vous êtes morts {cible.get_pseudo()}...')
                wait()
                cible.money -= 5
                joueur.money += 5
                print(f"{joueur.get_pseudo()}Vous avez gagner 5 BaeBucks et il vous reste {joueur.money} BaeBucks")
                if cible.money < 0:
                    cible.money = 0
                print(f"{cible.get_pseudo()}, vous avez perdu 5 BaeBucks et il vous reste {cible.money} BaeBucks ")
                possesions = json.load(open('varu.json', 'r'))
                self.player1.update()
                self.player2.update()
                with open("varu.json", "w+") as file:
                    json.dump(possesions, file)
                global possessions
                if str(input("Voulez-vous faire une seconde manche ? (Y/N)")) != 'Y':
                    self.running = False
                    quit()
                print("Et c'est reparti pour une manche !")


class Shop:
    def __init__(self, customer):
        print(f'Bienvenue à la YouBoutique d`objets !')
        self.customer = customer
        self.customer_money = possessions[customer.get_pseudo()]["argent"]
        self.customer_items = possessions[customer.get_pseudo()]["items"]
        self.thing_to_buy = []
        for each in armes:
            if each.name not in self.customer_items:
                self.thing_to_buy.append(each)
        for i in range(3):
            print("...")
            time.sleep(1)
        if int(input("Voulez vous acheter (1) ou vendre (2) ?")) == 1:
            self.purchase()
        else:
            self.sell()

    def purchase(self):
        print(f'On peut vous proposer ces objets : ')
        for each in self.thing_to_buy:
            print(
                f'{each.name} : dégâts : {each.damage}, type : {each.type} et prix : {each.cost} ({self.thing_to_buy.index(each)})')
            time.sleep(0.3)
        var = int(input("Saisissez le numéro du produit désiré ou 69 pour quitter"))
        if var == 69:
            self.go()
        else:
            if self.customer_money >= self.thing_to_buy[var].get_cost():
                time.sleep(0.3)
                if str(input("êtes vous sûr ? (Y/N)")) == 'Y':
                    self.customer_money -= self.thing_to_buy[var].get_cost()
                    self.customer_items.append(self.thing_to_buy[var].get_name())
                    print(f"Très bien il vous reste {self.customer_money} BaeBucks")
                    self.go()
                else:
                    self.go()
            else:
                time.sleep(0.3)
                print('Je suis navré de vous annoncer que vous n`avez pas la somme requise sur vous')
                self.go()

    def go(self):
        time.sleep(0.3)
        print(f'Au revoir {self.customer.get_pseudo()}, au plaisir de vous revoir !')
        time.sleep(0.3)

        possessions[self.customer.get_pseudo()]["items"] = self.customer_items
        json.dump(possessions, open('varu.json', 'w+'))
        self.customer.update()

    def sell(self):
        for each in armes:
            if each.get_name() in self.customer_items:
                print(
                    f'{each.name} : dégâts : {each.damage}, type : {each.type} et prix de vente : {each.cost} ({self.customer_items.index(each.get_name())})')
                time.sleep(0.3)
        var = int(input("Saisissez le numéro du produit désiré ou 69 pour quitter"))
        if var == 69:
            self.go()
        else:
            time.sleep(0.3)
            if str(input("êtes vous sûr ? (Y/N)")) == 'Y':
                self.customer_money += self.thing_to_buy[var].get_cost()
                del self.customer_items[var]
                print(f"Très bien il vous reste {self.customer_money} BaeBucks")
                self.go()
            else:
                self.go()


J1 = Player(str(input("Quelle est votre nom J1?")), 50, 2, 15, 10)
J2 = Player(str(input("Quelle est votre nom J2")), 50, 5, 8, 10)
J1.update()
J2.update()
# J1 = Player("Youfmile", 50, 2, 15, 10)
# J2 = Player("Kawthar", 50, 5, 8, 10)
game1 = Partie(J1, J2)
game1.play()
