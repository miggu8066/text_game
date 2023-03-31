from monster import Monster
import csv
import os
from m_data import M_data
import random

M_file = "./Chapter13/monster2.csv"

M_list = []

if os.path.exists(M_file):
    print("\n\n파일 여는중...")
    
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
    
def create_monster():
    print("\n- 몬스터를 랜덤으로 생성합니다-")
    print("")
    random_list = random.sample(M_list, 1)
    for randoms in random_list:
        if randoms.call_id() == 1:
            print("슬라임 을 만났습니다!")
        elif randoms.call_id() == 2:
            print("독두꺼비 를 만났습니다!")
        elif randoms.call_id() == 3:
            print("고블린 을 만났습니다!")
        elif randoms.call_id() == 4:
            print("고블린 기사 를 만났습니다!")
        elif randoms.call_id() == 5:
            print("불완전 골렘 를 만났습니다!")
        elif randoms.call_id() == 6:
            print("스켈레톤 을 만났습니다!")
        elif randoms.call_id() == 7:
            print("스켈레톤 병사 를 만났습니다!")
        elif randoms.call_id() == 8:
            print("스켈레톤 궁수 를 만났습니다!")
        elif randoms.call_id() == 9:
            print("스켈레톤 기사 를 만났습니다!")
        elif randoms.call_id() == 10:
            print("성체 골렘 을 만났습니다!")
        elif randoms.call_id() == 11:
            print("악령사신 을 만났습니다!")
        elif randoms.call_id() == 12:
            print("드래곤 를 만났습니다!")
        elif randoms.call_id() == 13:
            print("아이언 드래곤 을 만났습니다!")
        elif randoms.call_id() == 14:
            print("사이보그 를 만났습니다!")
        elif randoms.call_id() == 15:
            print("크라켄 을 만났습니다!")
    print("\n공격한다 : 1번 , 도망간다 : 2번")
        
    while True:
        try:
            choice = int(input("커맨드 입력 >>> "))
            if choice == 1:
                if randoms.call_id() == 1:
                    print("슬라임을 물리쳤다")
                break
            elif choice == 2:
                print("도망간다")
                break
            else:
                print("다시 입력하세요")
        except ValueError:
            print("반드시 숫자를 입력하세요")

while True:
    print("\n\n- 몬스터 생성 게임 -")
    print("\n메뉴를 선택하세요")
    print("\nCREATE MONSTER : 1번")
    print("\nMONSTER LIST: 2번")
    print("\n프로그램 종료 : 3번\n")
    try:
        choice = int(input(">>>"))
        if choice == 1:
            create_monster()
        elif choice == 2:
            print("몬스터 목록")
        elif choice == 3:
            print("*프로그램을 종료했습니다*")
            break
        else:
            print("올바른 번호를 입력하세요")
    except ValueError:
        print("반드시 숫자를 입력해주세요")