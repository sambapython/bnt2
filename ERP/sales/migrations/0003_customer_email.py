# Generated by Django 2.2 on 2019-05-16 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_auto_20190516_2126'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.EmailField(default='', max_length=300, null=True),
        ),
    ]
