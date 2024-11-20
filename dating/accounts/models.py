from dateutil.relativedelta import relativedelta
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

from .fields import PhoneField


class Interest(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)


class DatingUser(AbstractUser):
    Interests = models.ManyToManyField(Interest,
                                       related_name='users')
    image = models.ImageField(upload_to='media/accounts/',
                              null=True,
                              blank=True)
    city = models.CharField(max_length=100,
                            blank=True,
                            null=True)
    date_birth = models.DateField(blank=True,
                                  null=True)
    description = models.TextField(blank=True,
                                   null=True)
    phone = PhoneField(blank=True, null=True)

    class Meta(AbstractUser.Meta):
        indexes = [
            models.Index(fields=['city'])
        ]

    def get_user_age(self) -> int:
        return relativedelta(datetime.now(),
                             self.date_birth).years
