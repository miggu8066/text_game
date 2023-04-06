from monster import Monster
import csv
import os
from m_data import M_data
import random
from monster import Player



M_file = "./Chapter13/monster2.csv"

M_list = []

if os.path.exists(M_file):
    print("\n\n...게임시작...")
    
    f = open(M_file, "r", encoding="utf8")
    r = csv.reader(f)
    for mon in r:
        monsters = Monster(int(mon[0]), str(mon[1]), int(mon[2]), int(mon[3]), int(mon[4]), str(mon[5]))
        M_list.append(monsters)
else:
    f = open(M_file, "w", encoding="utf8", newline="")
    w = csv.writer(f)
    for mon in M_data:
        w.writerow(mon)

def runaway(randoms):
    while True:
        print(f"{p.name}가 '{randoms.call_name()}' 으로부터 도망쳤습니다...")
        try:
            choice = int(input("\n다시 생성하시려면 아무숫자나 눌러주세요.\n>>>"))
            print("----" * 20)
            if choice < 100000:
                break
            else:
                print("\n다시 입력 해주세요...!")
        except:
            print("\n숫자를 입력해주세요...!")

def attack(randoms):
    print(f"\n{p.name}가 '{randoms.call_name()}' 을 공격했습니다")
    if random.random() < 0.3:
        damage = p.attack - randoms.call_defense()
        if damage < 0:
            damage = 0
        print(f"{randoms.call_name()}에게 {damage}의 데미지를 입혔습니다!")
        randoms.take_damage(damage)
    else:
        print("공격이 빗나갔습니다..!")
    if not randoms.is_alive():
        print("몬스터 를 처치하였습니다!")
        print("----" * 20)

def create_monster():
    while True:
        randoms = random.choice(M_list)
        print(f"\n새로운 몬스터가 출연했습니다!\n'{randoms.call_name()}'\n체력:{randoms.call_health()}\n공격력:{randoms.call_attack()}\n방어력:{randoms.call_defense()}")
        # print("----" * 20)
        while randoms.is_alive() and p.is_alive():
            try:
                print(f"\n\n<플레이어 HP:{p.health}>\n<공격력:{p.attack}>")
                choice = int(input("\n어떻게 할까요?\n1번: 공격\n2번: 도망\n3번: 메뉴로 돌아가기\n>>>"))
                print("----" * 20)
                if choice == 1:
                    attack(randoms)
                    if randoms.is_alive():
                        monster_damage = randoms.call_attack() - p.defense
                        if monster_damage < 0:
                            monster_damage = 0
                        print(f"\n'{randoms.call_name()}'이(가) {p.name}에게 {monster_damage}의 데미지를 입혔습니다!")
                        p.take_damage(monster_damage)
                        print("----" * 20)
                elif choice == 2:
                    runaway(randoms)
                    break
                elif choice == 3:
                    break
                else:
                    print("다시 입력하세요.")
            except ValueError:
                print("반드시 숫자를 입력하세요.")
        if not p.is_alive():
            print(f"\n{p.name}님이 사망하였습니다")
            print("\n-게임오버-\n")
            exit()
        if choice == 3:
            break

def create_monster_list():
    for mlist in M_list:
        print(f"\n{mlist.id}번\n이름:'{mlist.call_name()}'\n등급:{mlist.call_rarity()}")

print("\n\n---random Monster game---")
choiceplayer = str(input("\n플레이어 닉네임을 설정하세요(문자만 가능합니다)\n:"))
p = Player(choiceplayer, 150, 50, 8)
print(f"\n환영합니다! 어서오세요 '{p.name}'님!!")
print("---플레이어 상태---")
print(f"\n이름:{p.name}\n체력:{p.health}\n공격력:{p.attack}\n방어력:{p.defense}")
print("----" * 20)

while True:
    print("\n\n- random monster game -")
    print("\n메뉴를 선택하세요")
    print("\n몬스터 생성! : 1번")
    print("\n몬스터 목록 보기: 2번")
    print("\n프로그램 종료 : 3번\n")
    try:
        choice = int(input("선택 >>>"))
        print("----" * 20)
        if choice == 1:
            create_monster()
        elif choice == 2:
            create_monster_list()
        elif choice == 3:
            print("\n*프로그램을 종료했습니다*\n")
            break
        else:
            print("\n\n올바른 번호를 입력하세요...!")
            print("----" * 20)
    except ValueError:
        print("\n\n반드시 숫자를 입력해주세요...!")
        print("----" * 20)