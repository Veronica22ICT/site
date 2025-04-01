# Generated by Django 5.1.7 on 2025-03-30 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knife', '0002_alter_care_image_alter_knife_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='care',
            name='image',
            field=models.ImageField(default='path/to/default_image.jpg', upload_to='cares/'),
        ),
        migrations.AlterField(
            model_name='repair',
            name='image',
            field=models.ImageField(default='path/to/default_image.jpg', upload_to='repairs/'),
        ),
    ]
