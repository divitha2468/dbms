# Generated by Django 3.1.3 on 2020-12-05 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orphanage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adoption',
            name='orphan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='orphanage.orphan'),
        ),
    ]
