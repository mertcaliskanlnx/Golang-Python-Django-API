# Generated by Django 3.2.4 on 2021-11-29 23:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bigdata',
            name='price',
        ),
    ]