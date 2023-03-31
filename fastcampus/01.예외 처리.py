# 원화를 입력, 환율 입력 -> 달러값을 출력

won = input("원화금액을 입력하세요>>>")
dollar = input("환율을 입력 하세요>>>")

try: # 예외가 발생 할수 있는 코드
    print(int(won) / int(dollar))
except: # 예외가 발생했을 때 실행되는 코드
    print("error")

print("프로그램이 끝났나요?")