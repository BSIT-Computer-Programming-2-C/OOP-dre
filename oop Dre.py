import random

class Character:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
    
    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
    
    def is_alive(self):
        return self.health > 0

    def attack_enemy(self, enemy):
        damage = random.randint(self.attack - 3, self.attack + 3)  #
        print(f"{self.name} attacks {enemy.name} for {damage} damage.")
        enemy.take_damage(damage)
        print(f"{enemy.name} has {enemy.health} health left.")


class RankB(Character):
    def __init__(self, taguro):
        super().__init__(taguro, health=120, attack=20)


class RankS(Character):
    def __init__(self, yujin):
        super().__init__(yujin, health=80, attack=15)


def battle(taguro, yujin):
    while taguro.is_alive() and yujin.is_alive():
        taguro.attack_enemy(yujin)
        if yujin.is_alive():
            yujin.attack_enemy(taguro)
    
    if taguro.is_alive():
        print(f"{taguro.name} wins the battle!")
    else:
        print(f"{yujin.name} wins the battle!")


if __name__ == "__main__":
    RankB = RankB("taguro")
    RankS = RankS("yujin")
    
    print(f"\nBattle Start: {RankB.name} vs {RankS.name}")
    battle(RankB ,RankS)