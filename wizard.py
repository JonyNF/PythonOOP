fireball_damage = 500
potion_mana = 100
fireball_cost = 50

class Wizard:
    def __init__(self, name, stamina, intelligence):
        self.name = name
        self.__stamina = stamina
        self.__intelligence = intelligence
        self.health = self.__stamina * 100
        self.mana = self.__intelligence * 10

    def get_fireballed(self):
        self.health -= fireball_damage

    def cast_fireball(self, target):
        if self.mana < fireball_cost:
            raise Exception(f"{self.name} cannot cast fireball")
        self.mana -= fireball_cost
        target.get_fireballed()
        

    def __is_alive(self):
        if self.health > 0:
            return True
        else : return False


    def drink_mana_potion(self):
        self.mana += potion_mana