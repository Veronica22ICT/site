from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    CATEGORY_CHOICES = [
        ('knife', 'Ніж'),
        ('repair', 'Ремонт'),
        ('care', 'Догляд'),
    ]

    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    product_id = models.PositiveIntegerField()  # ID продукту
    product_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    quantity = models.PositiveIntegerField(default=1)
    card_number = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.product_name}"


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