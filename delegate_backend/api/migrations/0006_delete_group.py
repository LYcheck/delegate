# Generated by Django 3.2.6 on 2021-08-30 00:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_group_table'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Group',
        ),
    ]
