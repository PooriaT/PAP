# Generated by Django 4.0.6 on 2022-07-24 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventHandler', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conference',
            name='conferenceName',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='event',
            name='eventName',
            field=models.CharField(max_length=150),
        ),
    ]
