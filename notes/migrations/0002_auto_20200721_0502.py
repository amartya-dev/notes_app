# Generated by Django 3.0.8 on 2020-07-21 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='note',
            field=models.BinaryField(),
        ),
    ]
