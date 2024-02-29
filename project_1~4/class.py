class Member():
    members = []
    def __init__(self):
        name = input("이름을 입력하세요 : ")
        username = input("id를 입력하세요 : ")
        password= input("pw를 입력하세요 : ")
        self.name = name
        self.username = username
        self.password = password
        self.my_post = []
        Member.members.append(self.name)
    def display(self):
        print(f"이름 : {self.name} , id : {self.username}")
    def post3(self):
        for i in range(3):
            post = Post(self)
            posting = (post.title, post.contents)
            self.my_post.append(posting)
        for i in self.my_post:
            print(i)
    def print_members(self):
        print(Member.members)
        
class Post():
    posts = []
    def __init__(self, user):
        title = input("게시물 제목을 입력하세요 : ")
        contents = input("게시물 내용을 입력하세요 : ")
        self.title = title
        self.contents = contents
        self.author = user.username
        self.posts.append(title)

user1 = Member() # 유저1 객체 생성되면서 이닛 작동
user2 = Member()
user3 = Member()

user1.print_members() # 멤버 클래스의 멤버 리스트 출력

user1.post3() # 유저1 포스트 3개 작성