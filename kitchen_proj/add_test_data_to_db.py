import os
import random
import sys

import django
from django.db import IntegrityError
from django.utils import timezone
from faker import Faker

# Настройка Django
sys.path.append(".")  # Замените на путь к вашему проекту
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kitchen_receipts_project.settings")
django.setup()

# Импорт моделей
from django.contrib.auth.models import User
from recipes.models import Recipe, Comment
from blog.models import Post, BlogComment
from users.models import Profile
from taggit.models import Tag


def populate_database():
    fake = Faker('ru_RU')

    # Создание пользователей и их профилей
    users = []
    for _ in range(10):
        username = fake.user_name()
        email = fake.email()
        password = 'testpassword123'
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            Profile.objects.get_or_create(user=user, defaults={'bio': fake.text(max_nb_chars=200)})
            users.append(user)
        except IntegrityError:
            # Если пользователь уже существует, пропускаем его создание
            print(f"Пользователь {username} уже существует. Пропускаем.")
            continue

    # Создание тегов
    tags = [
        "Завтрак", "Обед", "Ужин", "Десерт", "Вегетарианское",
        "Мясо", "Рыба", "Суп", "Салат", "Выпечка",
        "Итальянская кухня", "Азиатская кухня", "Русская кухня", "Французская кухня",
        "Быстро и просто", "Праздничное блюдо", "Здоровое питание", "Низкокалорийное"
    ]
    for tag_name in tags:
        Tag.objects.get_or_create(name=tag_name)

    # Создание рецептов
    recipes = []
    for _ in range(50):
        title = fake.sentence(nb_words=4)[:-1]
        description = fake.paragraph(nb_sentences=3)
        ingredients = "\n".join([f"{fake.word()} - {fake.random_int(min=1, max=1000)} {fake.word()}" for _ in range(5)])
        instructions = "\n".join([f"{i + 1}. {fake.sentence()}" for i in range(5)])
        author = random.choice(users)
        recipe = Recipe.objects.create(
            title=title,
            description=description,
            ingredients=ingredients,
            instructions=instructions,
            author=author
        )
        recipe.tags.add(*random.sample(tags, k=random.randint(1, 5)))
        recipes.append(recipe)

    # Добавление лайков к рецептам
    for recipe in recipes:
        for user in random.sample(users, k=random.randint(0, len(users))):
            recipe.likes.add(user)

    # Создание комментариев к рецептам
    for _ in range(200):
        recipe = random.choice(recipes)
        author = random.choice(users)
        text = fake.paragraph(nb_sentences=2)
        created_at = fake.date_time_between(start_date='-1y', end_date='now', tzinfo=timezone.get_current_timezone())
        Comment.objects.create(recipe=recipe, author=author, text=text, created_at=created_at)

    # Создание постов блога
    posts = []
    for _ in range(20):
        title = fake.sentence(nb_words=6)[:-1]
        content = "\n\n".join([fake.paragraph(nb_sentences=5) for _ in range(3)])
        author = random.choice(users)
        created_at = fake.date_time_between(start_date='-1y', end_date='now', tzinfo=timezone.get_current_timezone())
        post = Post.objects.create(title=title, content=content, author=author, created_at=created_at)
        posts.append(post)

    # Создание комментариев к постам блога
    for _ in range(100):
        post = random.choice(posts)
        author = random.choice(users)
        text = fake.paragraph(nb_sentences=2)
        created_at = fake.date_time_between(start_date=post.created_at, end_date='now',
                                            tzinfo=timezone.get_current_timezone())
        BlogComment.objects.create(post=post, author=author, text=text, created_at=created_at)

    print("База данных успешно заполнена тестовыми данными!")


if __name__ == "__main__":
    populate_database()
