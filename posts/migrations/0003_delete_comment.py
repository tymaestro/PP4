# Generated by Django 3.2.13 on 2022-05-18 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20220515_1705'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
