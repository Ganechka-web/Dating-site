import re

from django.core.exceptions import ValidationError
from django.db import models


class PhoneField(models.CharField):
    def pre_save(self, model_instance, add):
        phone = getattr(model_instance, self.attname)
        if phone is not None:
            result = re.fullmatch(
                r'^(\+?8|7)?[\- ]?(\(\d{3}\)|\d{3})[\- ]?(\d{3})[\- ]?(\d{2})[\- ]?(\d{2})$',
                phone
            )
            if result:
                setattr(model_instance, self.attname, phone)
                return super().pre_save(model_instance, add)
            raise ValidationError('Incorrect phone number format')
        return super().pre_save(model_instance, add)
