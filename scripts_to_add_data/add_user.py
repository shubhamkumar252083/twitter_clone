from user.models import User
from django.contrib.auth.hashers import make_password, check_password
from faker import Faker
import random

# Create a Faker instance
fake = Faker()

# print(f'password encryption ==  {make_password("skmd")}')
# print(f'password check == {check_password("skmd", "pbkdf2_sha256$600000$YV5eFRaO4J0r0S73wXU70q$s7PoaSO6ZeqxPBnn43O2WC97tTxoWY93nuIDFiDVaS8=")}')

for i in range(500):
  name = fake.name()
  address = fake.address()
  email = fake.email()  
  mobile = str(random.randint(1000000000, 9999999999))
  password = "pbkdf2_sha256$600000$YV5eFRaO4J0r0S73wXU70q$s7PoaSO6ZeqxPBnn43O2WC97tTxoWY93nuIDFiDVaS8="
  user = User.objects.create(name=name, address=address, email=email, mobile=mobile, password=password, raw_password = "skmd")