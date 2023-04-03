import random

class Monster:
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        self.hp -= damage

    def __str__(self):
        return self.name


class Player:
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        self.hp -= damage

    def __str__(self):
        return self.name


monsters = [
    Monster("Goblin", 20, 5, 2),
    Monster("Orc", 30, 7, 3),
    Monster("Troll", 50, 10, 5)
]

player = Player("Player", 50, 8, 3)


def attack(monster):
    print(f"{monster.name}를 공격합니다!")
    if random.random() < 0.5:
        damage = player.attack - monster.defense
        if damage < 0:
            damage = 0
        print(f"{monster.name}에게 {damage}의 데미지를 입힙니다!")
        monster.take_damage(damage)
    else:
        print("공격이 빗나갑니다!")

    if not monster.is_alive():
        print(f"{monster.name}을(를) 물리쳤습니다!")


def run_away(monster):
    print(f"{monster.name}으로부터 도망쳤습니다.")


def game():
    while True:
        monster = random.choice(monsters)
        print(f"\n새로운 몬스터가 출현했습니다: {monster.name} (HP: {monster.hp})")
        while monster.is_alive() and player.is_alive():
            print(f"\n{player.name}의 상태: HP {player.hp}")
            choice = input("어떻게 할까요? (1: 공격, 2: 도망) ")
            if choice == "1":
                attack(monster)
                if monster.is_alive():
                    monster_damage = monster.attack - player.defense
                    if monster_damage < 0:
                        monster_damage = 0
                    print(f"{monster.name}의 공격! {player.name}은(는) {monster_damage}의 데미지를 입었습니다.")
                    player.take_damage(monster_damage)
            elif choice == "2":
                run_away(monster)
                break
        if not player.is_alive():
            print("당신은 죽었습니다... 게임 오버!")
            break
game()