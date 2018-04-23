from django.contrib.auth.models import User
from django.db import models
import random
import string


# Create your models here.

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    """
    https://www.codingforentrepreneurs.com/blog/random-string-generator-in-python/
    :param size:
    :param chars:
    :return:
    """
    return ''.join(random.choice(chars) for _ in range(size))


class UserToken(models.Model):
    key = models.CharField(max_length=36)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def save(self, **kwargs):
        if self.key is None:
            self.generate_key()
        return super(UserToken, self).save(**kwargs)

    def generate_key(self):
        return random_string_generator()
