# Generated by Django 3.2 on 2021-05-11 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='date de parution'),
        ),
        migrations.AlterField(
            model_name='article',
            name='miniature',
            field=models.ImageField(upload_to='blog/miniatures/'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='blog/images/'),
        ),
    ]
