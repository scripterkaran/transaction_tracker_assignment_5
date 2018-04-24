from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return "%s" % (self.name,)

    def get_json(self):
        return {
            'name': self.name
        }

class Transaction(models.Model):
    DEBIT = 1
    CREDIT = 2

    TRANSACTION_TYPE = (
        (DEBIT, 'Debit'),
        (CREDIT, 'Credit'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="transactions")
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    transaction_type = models.PositiveSmallIntegerField(choices=TRANSACTION_TYPE)
    value = models.DecimalField(max_digits=12, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="transactions")

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        return super(Transaction, self).save(force_insert=False, force_update=False, using=None,
             update_fields=None)

    def get_absolute_url(self):
        return reverse('transaction-detail', kwargs={'pk': self.pk})

    def get_transaction_type(self):
        if self.transaction_type == 1:
           return "Debit"
        return "Credit"

    def get_json(self):
        return {
            'user': self.user.username,
            'name': self.name,
            'type': self.get_transaction_type(),
            'created_at': self.created_at,
            'value': self.value,
            'category': self.category.name
        }
