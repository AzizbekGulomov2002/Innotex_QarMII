# Generated by Django 4.1.1 on 2022-09-24 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='maqola',
            name='kurishlar',
            field=models.IntegerField(default=1),
        ),
    ]
