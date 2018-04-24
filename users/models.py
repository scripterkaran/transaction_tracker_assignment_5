import binascii

import os
from django.contrib.auth.models import User
from django.db import models

class UserToken(models.Model):
    key = models.CharField(max_length=500)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def save(self, **kwargs):
        self.key = self.generate_key()
        return super(UserToken, self).save(**kwargs)

    def generate_key(self):
        return binascii.hexlify(os.urandom(20)).decode()

    def __unicode__(self):
        return self.key
