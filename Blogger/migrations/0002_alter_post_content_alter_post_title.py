# Generated by Django 4.1.4 on 2022-12-14 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blogger', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
