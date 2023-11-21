from user.models import User
from faker import Faker
import random
fake = Faker()


all_user_ids = User.objects.only("id").all()
ln = len(all_user_ids)
i=1
for user in all_user_ids:
    followers_list = random.sample(list(all_user_ids), random.randint(0, ln))
    try:
      followers_list.remove(user)
    except:
      pass
    user.follows.add(*followers_list)
    print(i)
    i+=1

