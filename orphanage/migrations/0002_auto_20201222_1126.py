# Generated by Django 3.1.3 on 2020-12-22 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orphanage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='designation',
            field=models.CharField(max_length=30),
        ),
    ]
