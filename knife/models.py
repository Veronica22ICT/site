from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class Knife(models.Model):
    name = models.CharField(max_length=70)
    image = models.ImageField(upload_to='knives/', null=False, default='path/to/default_image')
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    mechanism = models.CharField(max_length=20,null=True, blank=True)
    price = models.IntegerField()
    available = models.IntegerField()
    post_office = models.CharField(max_length=50, null=True, blank=True)
    time = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name


class Care (models.Model):
    name = models.CharField(max_length=45)
    image = models.ImageField(upload_to='knives/', null=False, default='path/to/default_image')
    description = models.TextField()
    price = models.IntegerField()
    available = models.IntegerField()
    post_office = models.CharField(max_length=50, null=True, blank=True)
    time = models.DateTimeField(auto_now_add=True)


class Repair (models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='knives/', null=False, default='path/to/default_image')
    description = models.TextField()
    price = models.IntegerField()
    available = models.IntegerField()
    post_office = models.CharField(max_length=50, null=True, blank=True)
    time = models.DateTimeField(auto_now_add=True)