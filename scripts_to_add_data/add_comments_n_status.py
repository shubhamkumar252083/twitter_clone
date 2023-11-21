from database.models import Tweet, CommentsAndStatus
from user.models import User
from faker import Faker
import random
fake = Faker()


all_user_ids = list(User.objects.only("id").all())
sublist_size_for_user_ids = random.randint(500, 800)

all_tweet_ids = list(Tweet.objects.only("id").all())
sublist_size_for_tweet_ids = random.randint(100, 20000)


for user_id in random.sample(all_user_ids, sublist_size_for_user_ids):
    objects_to_create = []
    for tweet_id  in random.sample(all_tweet_ids, sublist_size_for_tweet_ids):
        comment = fake.paragraph(nb_sentences=random.randint(1, 5))
        status = random.choice(["L", "D", "H", "N"])
        objects_to_create.append(CommentsAndStatus(status=status, user_id=user_id, comment=comment, tweet_id=tweet_id))
    CommentsAndStatus.objects.bulk_create(objects_to_create)