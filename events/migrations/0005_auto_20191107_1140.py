# Generated by Django 2.2.7 on 2019-11-07 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20190819_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventpage',
            name='attended',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
