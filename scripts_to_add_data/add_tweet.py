from database.models import Tweet
from user.models import User
from faker import Faker
import random
fake = Faker()

def add(user_id):
  for i in range(random.randint(1, 50)):
    tweet_message = fake.text(max_nb_chars=random.randint(100, 250))  # You can adjust the character limit
    Tweet.objects.create(user_id=user_id, tweet=tweet_message)



user_obj = User.objects.only("id").all()
for user_id in user_obj:
  add(user_id)


