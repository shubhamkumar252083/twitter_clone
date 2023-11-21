from database.models import Tweet, Hashtag
from user.models import User
from faker import Faker
import random
fake = Faker()


my_list = list(Tweet.objects.only("id").all())
previous_tage = set(Hashtag.objects.values_list("name", flat=True))

for i in range(600):
  name = f"#{fake.word()}"
  if name in previous_tage:
    continue
  else:
    previous_tage.add(name)
    sublist_size = random.randint(0, 5000)
    random_sublist = random.sample(my_list, sublist_size)
    hashtag = Hashtag.objects.create(name=name)
    hashtag.tweets.add(*random_sublist)
    print(f'{name} ==> {len(random_sublist)}')


print(previous_tage)