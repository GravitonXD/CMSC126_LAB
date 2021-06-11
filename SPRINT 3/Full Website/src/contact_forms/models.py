from datetime import datetime
from django.db import models
from django.db.models.fields import TextField


# Create your models here.
class Form(models.Model):
    date = models.DateTimeField(auto_created=True, default=datetime.now())
    name = models.TextField()
    e_mail = models.EmailField()
    subject = models.TextField()
    service = models.CharField(max_length=15)
    message = TextField()