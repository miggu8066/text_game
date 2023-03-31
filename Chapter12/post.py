class Post:
    """
        게시물 클래스
        param id: 순서
        param To_do_title: To_do제목
        param To_do_content: To-do글내용
        param To_do_success: 성공유무
        param view_count: 조회수
    """
    def __init__(self, id, To_do_title, To_do_content, To_do_success, view_count):
        self.id = id
        self.To_do_title = To_do_title
        self.To_do_content = To_do_content
        self.To_do_success = To_do_success
        self.view_count = view_count
    
    def set_post(self, id, To_do_title, To_do_content, To_do_success, view_count):
        self.id = id
        self.To_do_title = To_do_title
        self.To_do_content = To_do_content
        self.To_do_success = To_do_success
        self.view_count = view_count
    
    def add_view_count(self):
        self.view_count += 1
    
    def get_id(self):
        return self.id

    def get_To_do_title(self):
        return self.To_do_title

    def get_To_do_content(self):
        return self.To_do_content
    
    def get_To_do_success(self):
        return self.To_do_success
    
    def get_view_count(self):
        return self.view_count
    
if __name__ == "__main__":
    todo = Post(1, '오늘할일', '오늘할일내용', '성공유무', 0)
    todo.get_view_count()
    print(f"{todo.get_id()} {todo.get_To_do_title()} {todo.get_To_do_content()} {todo.get_To_do_success()} {todo.get_view_count()}")