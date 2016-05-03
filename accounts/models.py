from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils import timezone


# Create your models here.
class AccountUserManager(UserManager):
    def _create_user(self, username, email, password,
                     is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        #if not email :
        #    raise ValueError('Set Username')
        email = self.normalize_email(email)
        user = self.model(username=email, email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)


        return user

class User(AbstractUser):
    objects=AccountUserManager()


class Profile(models.Model):
    Nickname=models.CharField(max_length=200)
    Image = models.ImageField(upload_to="images/profile-images", blank=True, null=True)








