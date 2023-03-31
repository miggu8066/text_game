won = input("원화금액을 입력하세요>>>")
dollar = input("환율을 입력 하세요>>>")

# ValueError int 함수에 문자를 썻을때 발생하는 에러

try: # 예외가 발생 할수 있는 코드
    print(int(won) / int(dollar))
except ValueError as e: # 발생할수있는 에러를 직접지정할수있다
    print("문자열 예외가 발생 다시 실행 바람", e)
except ZeroDivisionError as e:
    print("나누기 0은 불가능 합니다", e)

# 발생할수있는 에러 에 별칭을 줄수 있다
# 그리고 프린트문장 옆에 , 별칭 을해주면 추가로 에러메세지가 뜨게된다
else:
    print("예외가 발생하지 않았을때 실행되는 코드")
finally: # 항상 실행될거면 왜쓰냐? 파일을 열고 나서 닫을때, 리소스를 반환을 꼭해줘야되는 코드가 필요할때 써줄필요있따
    print("예외가 발생하던지, 발생하지않던지 항상 실행되는 코드")