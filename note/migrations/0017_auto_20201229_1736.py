# Generated by Django 3.1.4 on 2020-12-29 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0016_folder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='created',
            field=models.DateTimeField(auto_now=True, verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='note',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, verbose_name='updated'),
        ),
    ]
