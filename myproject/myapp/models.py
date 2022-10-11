from django.db import models
from ordered_model.models import OrderedModel


class User(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Contact(OrderedModel):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    avatar = models.FileField(upload_to='uploads', blank=True, null=True)

    user = models.ForeignKey(
        User, related_name='contacts', on_delete=models.CASCADE)

    order_with_respect_to = 'user'

    def __str__(self):
        return f'{self.name} <{self.email}>'
