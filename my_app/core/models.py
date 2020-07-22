from django.db import models

# Create your models here.


class SampleUser(models.Model):
    name = models.TextField(max_length=100, blank=True)
    phone_no = models.CharField(max_length=300, blank=True)
    email_id = models.EmailField()
