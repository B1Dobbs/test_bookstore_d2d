# Generated by Django 3.0.2 on 2020-02-07 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_bookstore_app', '0006_auto_20200207_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='vol_num',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
