import os
import csv
from post import Post

# 파일 경로로
to_do_file = "./Chapter12/todo_data.csv"

# post 객체를 저장할 리스트
todo_list = []

# data.csv 파일이 있다면
if os.path.exists(to_do_file):
    print("\n\n로딩중...")
    f = open(to_do_file, "r", encoding="utf8")
    r = csv.reader(f)
    for todo in r:
        # Post 인스턴스 생성하기
        p = Post(int(todo[0]), todo[1], todo[2], todo[3], int(todo[4]))
        todo_list.append(p)
else:
    # 파일 생성하기
    f = open(to_do_file, "w", encoding="utf8", newline="")
    f.close()

# 게시글 쓰기
def write_todo():
    print("\n\n* 할일 쓰기 *\n")
    todo_title = input("제목을 입력해주세요\n>>>")
    todo_content = input("내용을 입력해 주세요\n>>>")
    todo_success = input("성공 유무 체크) 입력\n>>>")
    id = todo_list[-1].get_id() + 1
    p = Post(id, todo_title, todo_content, todo_success, 0)
    todo_list.append(p)
    print("# 게시글이 등록 되었습니다.")

# 게시글 목록
def list_todo():
    print("\n\n- 게시글 목록 -")
    i_list = []
    for todo in todo_list:
        print("번호 :", todo.get_id())
        print("제목 :", todo.get_To_do_title())
        print("")
        i_list.append(todo.get_id())

    while True:
        print("Q) 상세페이지 를 보시려면 번호를 선택해 주세요 (메뉴로 돌아가려면 -1 을 입력해주세요.)")
        try:
            i = int(input(">>>"))
            if i in i_list:
                detail_todo(i)
                break
            elif i == -1:
                break
            else:
                print("없는 글 번호 입니다.")
        except ValueError:
            print("숫자를 입력해 주세요.")

def detail_todo(i):
    print("\n\n- 게시글 상세 -")
    
    for todo in todo_list:
        if todo.get_id() == i:
            todo.add_view_count()
            print("번호 :", todo.get_id())
            print("제목 :", todo.get_To_do_title())
            print("내용 :", todo.get_To_do_content())
            print("성공유무 :", todo.get_To_do_success())
            print("조회수 :", todo.get_view_count())
            target_todo = todo
    
    while True:
        print("Q) 수정: 1 삭제 : 2 (메뉴로 돌아가려면 -1 을 입력)")
        try:
            c = int(input(">>>"))
            if c == 1:
                update_todo(target_todo)
            elif c == 2:
                delete_todo(target_todo)
                break
            elif c == -1:
                print("\n\n메뉴로 돌아갑니다")
                break
            else:
                print("잘못 입력하였습니다.")
        except ValueError:
            print("반드시 숫자를 입력하세요.")

# 게시글 수정
def update_todo(target_todo):
    print("\n\n- 게시글 수정 -")
    t = input("제목을 수정 해주세요\n>>>")
    c = input("본문을 수정 해주세요\n>>>")
    s = input("성공유무를 수정 해주세요\n>>>")
    target_todo.set_post(target_todo.id, t, c, s, target_todo.view_count)
    print("# 게시글 수정 완료")

# 게시글 삭제
def delete_todo(target_todo):
    todo_list.remove(target_todo)
    print("# 게시글 삭제 완료")

# 게시글 저장
def save_todo():
    f = open(to_do_file, 'w', encoding='utf8', newline='')
    w = csv.writer(f)
    for todo in todo_list:
        r = [todo.get_id(), todo.get_To_do_title(), todo.get_To_do_content(), todo.get_To_do_success(), todo.get_view_count()]
        w.writerow(r)
    f.close()
    print("# 저장 완료")
    print("# 프로그램 종료")

# 메뉴 출력하기
while True:
    print("\n\n- TO_DO_LIST -")
    print("\n- 메뉴를 선택해 주세요 -\n")
    print("1. 할일 쓰기\n")
    print("2. 할일 목록\n")
    print("3. 프로그램 종료\n")
    try:
        choice = int(input(">>>"))
    except ValueError:
        print("숫자를 입력해 주세요")
    else:
        if choice == 1:
            write_todo()
        elif choice == 2:
            list_todo()
        elif choice == 3:
            save_todo()
            print('프로그램 종료')
            break