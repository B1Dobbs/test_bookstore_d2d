# Generated by Django 3.0.2 on 2020-02-07 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_bookstore_app', '0009_auto_20200207_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='vol_num',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
