# Generated by Django 2.2.13 on 2020-12-04 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20201204_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email_confirmed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(max_length=10),
        ),
    ]
