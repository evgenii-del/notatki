# Generated by Django 3.1.4 on 2020-12-13 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0002_auto_20201201_1225'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='archive',
            field=models.BooleanField(blank=True, null=True, verbose_name='archive'),
        ),
        migrations.AlterField(
            model_name='note',
            name='created',
            field=models.DateTimeField(blank=True, null=True, verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='note',
            name='image',
            field=models.ImageField(blank=True, upload_to='images', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='note',
            name='updated',
            field=models.DateTimeField(blank=True, null=True, verbose_name='updated'),
        ),
    ]
