# Generated by Django 2.1.5 on 2019-04-14 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20190414_1327'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movie_id',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]
