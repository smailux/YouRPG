
class Weapon:
    def __init__(self, name, damage, type, cost=0):
        self.att3 = None
        self.att2 = None
        self.att1 = None
        self.name = name
        self.damage = damage
        self.type = type
        self.has_melee = False
        self.has_magic = False
        self.has_heavy = False
        self.has_light = False
        self.cost = cost
        if type == "melee":
            self.has_melee = True
        elif type == "magic":
            self.has_magic = True
        elif type == "heavy":
            self.has_heavy = True
        elif type == "light":
            self.has_light = True


    def get_name(self):
        return self.name

    def get_type(self):
        return self.type

    def get_attacks(self, num):
        self.att1 = Attacks("Charge", 5, "melee")
        if self.has_melee:
            self.att2 = Attacks("Slash", 10, "melee")
            self.att3 = Attacks("Aerial Slash", 20, "melee", consu=3)

        elif self.has_magic:
            self.att2 = Attacks("Fire charge", 15, "magic", consu=2)
            self.att3 = Attacks("Ultra Explosion", 35, "magic", consu=7, counter=4)
        elif self.has_heavy:
            self.att2 = Attacks("Boink", 15, "heavy", counter=3)
            self.att3 = Attacks("Big BOOM", 30, "heavy", counter= 6, consu=2)
        elif self.has_light:
            self.att2 = Attacks("SpeedHit",10 ,"light")
            self.att3 = Attacks("ExtremeHit", 25, "light",consu=5)

        if num == 1:
            return self.att1
        elif num == 2:
            return self.att2
        elif num == 3:
            return self.att3

    def get_cost(self):
        return self.cost

class Attacks(Weapon):
    def __init__(self, name, damage, type, consu=None, counter=None):
        super().__init__(name, damage, type)
        self.consu = consu
        self.counter = counter

    def get_name(self):
        return self.name

    def get_type(self):
        return self.type

    def get_damage_amount(self):
        return self.damage

    def get_consu(self):
        return self.consu

    def get_counter(self):
        return self.counter
