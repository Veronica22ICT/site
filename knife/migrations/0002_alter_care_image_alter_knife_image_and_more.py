# Generated by Django 5.1.7 on 2025-03-30 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knife', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='care',
            name='image',
            field=models.ImageField(default='path/to/default_image.jpg', upload_to='knives/'),
        ),
        migrations.AlterField(
            model_name='knife',
            name='image',
            field=models.ImageField(default='path/to/default_image.jpg', upload_to='knives/'),
        ),
        migrations.AlterField(
            model_name='repair',
            name='image',
            field=models.ImageField(default='path/to/default_image.jpg', upload_to='knives/'),
        ),
    ]
