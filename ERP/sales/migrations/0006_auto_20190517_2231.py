# Generated by Django 2.2 on 2019-05-17 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0005_auto_20190517_2231'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sample',
            old_name='id',
            new_name='id1',
        ),
    ]