from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.


class AdvUser(AbstractUser):

    class Meta(AbstractUser.Meta):

        pass