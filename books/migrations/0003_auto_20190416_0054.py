# Generated by Django 2.1.5 on 2019-04-15 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20190414_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_rating',
            name='rating',
            field=models.FloatField(),
        ),
    ]
