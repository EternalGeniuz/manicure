from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


# Create your models here.

class Master(models.Model):
    name = models.CharField(max_length=256)
    surname = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    age = models.IntegerField
    work_experience = models.IntegerField


class Service(models.Model):
    service_name = models.CharField(max_length=256)
    price = models.IntegerField


class Set(models.Model):
    set_name = models.CharField(max_length=256)
    price = models.IntegerField
    time = models.IntegerField
    services = models.ManyToManyField(Service)
    image = models.ImageField(upload_to='sets_image/', null=True, blank=True)


class Record(models.Model):
    date = models.DateField
    start_time = models.TimeField
    end_time = models.TimeField
    master_id = models.ForeignKey(Master, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    set_id = models.ForeignKey(Set, on_delete=models.PROTECT)
