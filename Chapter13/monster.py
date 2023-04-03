class Player:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
    def player_name(self):
        return self.player_name
    
    def is_alive(self):
        return self.health > 0
    
    def take_damage(self, damage):
        self.health -= damage
    
    
class Monster:
    def __init__(self, id, name, health, attack, defense, rarity):
        self.id = id
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.rarity = rarity

    def take_damage(self, damage):
            self.health -= damage

    def is_alive(self):
        return self.health > 0
                
    def attack_up(self):
        self.attack += 1

    def call_id(self):
        return self.id

    def call_name(self):
        return self.name
    
    def call_health(self):
        return self.health
    
    def call_attack(self):
        return self.attack
    
    def call_defense(self):
        return self.defense
    
    def call_rarity(self):
        return self.rarity

# if __name__ == "__main__":    
#     m = Monster('동물', 290, 1700, 600, '희귀')
#     # # m.attack_up()
#     # # m.set_monster('늑대', 300, 1080, 3241, '일반')
#     print(f"{m.call_name()} {m.call_health()} {m.call_attack()} {m.call_defense()} {m.call_rarity()}")