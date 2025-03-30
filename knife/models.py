from django.db import models


class Knife(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='knives/', null=False, default='path/to/default_image.jpg')
    description = models.TextField()
    types = models.CharField(max_length=100)
    mechanism = models.CharField(max_length=100)
    price = models.IntegerField()
    available = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Care (models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='cares/', null=False, default='path/to/default_image.jpg')
    description = models.TextField()
    price = models.IntegerField()
    available = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)


class Repair (models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='repairs/', null=False, default='path/to/default_image.jpg')
    description = models.TextField()
    price = models.IntegerField()
    available = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)