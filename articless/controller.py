from view import UserUnterface
from model import ArticleModel


class Controller:
    def __init__(self):
        self.article_model = None
        self.user_interface = UserUnterface()

    def run(self):
        answer = None
        while answer != "q":
            answer = self.user_interface.wait_user_answer()
            self.check_user_answer(answer)

    def check_answer(self, answer):
        if answer == "1":
            article = self.user_interface.add_user_article()
            print(article)

