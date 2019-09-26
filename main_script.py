import tools
import InstagramAPI
import json
import os


# В период за месяц с 1 по 30 (31) ведём сбор вовлеченности.
# 1. Количество постов.
# 2. Количество лайков.
# 3. Количество комментариев.
# 4. Количество подписчиков.


# если файл с фидами есть, удаляем его перед началом работы
if os.path.exists("feed.json"):
    os.remove("feed.json")

# узнаем user_id целевого аккаунта
user_id = tools.get_userid_by_username('serpuhov_ru')

# логинимся
current_session = InstagramAPI.InstagramAPI("andrewa374", "1q2w3e4r5t")
current_session.login()

# получаем количество подписчиков целевого аккаунта
followers_count = str(len(current_session.getTotalFollowers(user_id)))

# собираем фид за месяц
feed_as_list = current_session.getTotalUserFeed(user_id, tools.seconds_from_start_month())

# дампим полученный фид в json-файл
with open("feed.json", "w") as f:
    json.dump(feed_as_list, f, indent=4)

# открываем дамп для подсчета метрик
with open("feed.json", "r") as feed:

    # загружаем json
    month_feed = json.load(feed)

    # объявляем пустые массивы для дальнейшей работы
    post_likes, likes_count = [], []
    post_comments, comments_count = [], []
    posts_count = []

    # парсим каждый пост полученного фида
    for post in month_feed:

        # получаем список с количеством лайков для каждого поста
        post_likes.append(post["like_count"])

        # получаем список с количеством комментариев для каждого поста
        post_comments.append(post["comment_count"])

    # считаем количество постов
    str(posts_count.append(len(post_likes)))

    # считаем количество лайков
    str(likes_count.append(sum(post_likes)))

    # считаем количество комментариев
    str(comments_count.append(sum(post_comments)))

    # вуаля!
    print("Количество подписчиков: " + "[" + followers_count + "]" + " Количество постов: " + str(posts_count) +
          " Количество лайков: " + str(likes_count) + " Количество комментариев: " + str(comments_count))
