from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver



class UserManager(BaseUserManager):
    
    def create_superuser(self, email, mobile, password, **other_fields):
        other_fields.setdefault('is_admin', True)
        # other_fields.setdefault('is_superuser', True)
        if other_fields.get('is_admin') is not True:
            raise ValueError(
                'Superuser must be assigned to is_admin = True.')

        return self.create_user(email, mobile, password, **other_fields)

    def create_user(self, email, mobile, password, **other_fields):

        if not email:
            raise ValueError('User must have an email address')

        if not mobile:
            raise ValueError('User must have an phone number')
        
        other_fields.setdefault('raw_password', password)
        email = self.normalize_email(email)
        user = self.model(email=email,
                          mobile=mobile, **other_fields)
        user.set_password(password)
        user.save()
        return user

    '''
    def update_user(self, user, new_data):
        # Your custom update logic here
        print(f'@user ==> {user} == {new_data}')
        for key, value in new_data.items():
            if hasattr(user, key):
                setattr(user, key, value)
                print(f'@update_user {key} ==>  {value}')
        user.save(using=self._db)
        return user

    '''




class User(AbstractBaseUser):
    id = models.BigAutoField(primary_key=True, db_column="fld_ai_id")
    name = models.CharField(
        max_length=100,  default="", db_column="name")
    address = models.CharField(
        max_length=255, default="", db_column="fld_address")
    email = models.EmailField(
        verbose_name='Email',
        max_length=100,
        unique=True, db_column="fld_email")
    mobile = models.CharField(
        max_length=100, unique=True, db_column="fld_mobile")
    password = models.CharField(max_length=255, db_column="fld_password")
    raw_password = models.CharField(max_length=25, default="", db_column="fld_raw_password")
    created_datetime = models.DateTimeField(
        auto_now_add=True, blank=True, null=True, db_column="fld_created_datetime")
    is_admin = models.BooleanField(default=False, db_column="fld_is_admin")

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['mobile', "password"]  # these fields must be entered.

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    
    def save(self, *args, **kwargs):
        if self.email:
            self.email = self.email.lower()
        super(User, self).save(*args, **kwargs)

    class Meta:
        db_table = 'tbl_user'
        verbose_name = "users"

