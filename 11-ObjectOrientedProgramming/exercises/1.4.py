# ===== Zadanie 4 =====

# definicja klasy
class SocialMediaProfile:

    def __init__(self, username):  # konstruktor
        self.username = username  # nazwa użytkownika
        self.posts = []  # lista postów, typ list

    def add_post(self, content):  # dodanie posta
        self.posts.append(content)  # zapis posta

    def display_timeline(self):  # wyświetlenie tablicy postów
        print(f"User: {self.username}")  # nazwa użytkownika

        for i, post in enumerate(self.posts, start=1):  # numerowanie wpisów
            print(f"{i}. {post}")  # wyświetlenie wpisu


user = SocialMediaProfile("johndoe")  # utworzenie użytkownika

user.add_post("Hello, world!")  # pierwszy wpis
user.add_post("Had a great day at the park!")  # drugi wpis
user.add_post("What's up, Natalie? How are you?")  # trzeci wpis

user.display_timeline()  # wyświetlenie osi czasu