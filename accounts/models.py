from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username, password=None, is_active=True, is_staff=False, is_admin=False):
        if not username:
            raise ValueError("User tidak boleh kosong / tidak valid!")
        if not password:
            raise ValueError("Password tidak boleh kosong")
        
        user_obj = self.model()
        user_obj.username = username
        user_obj.set_password(password)
        user_obj.active = is_active
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.save(using=self._db)
        
        return user_obj
    
    def create_staffuser(self, username, password=None):
        user = self.create_user(
            username,
            password=password,
            is_staff=True
        )
        return user

    def create_superuser(self, username, password=None):
        user = self.create_user(
            username,
            password=password,
            is_admin=True,
            is_staff=True
        )

        return user

class User(AbstractBaseUser):
    username = models.CharField(max_length=8, unique=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(default=False) # buat login
    staff = models.BooleanField(default=False) # staff user non superuser
    admin = models.BooleanField(default=False) # superuser
    status = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = []

    objects = UserManager()


    def __str__(self):
        return self.username

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        if self.full_name:
            return self.full_name.split()[0]
        return self.full_name

    def has_perm(self, perm, object=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_active(self):
        return self.active

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_login(self):
        return self.status

