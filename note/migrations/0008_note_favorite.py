# Generated by Django 3.1.4 on 2020-12-26 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0007_auto_20201224_2348'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='favorite',
            field=models.BooleanField(default=False, verbose_name='favorite'),
        ),
    ]
