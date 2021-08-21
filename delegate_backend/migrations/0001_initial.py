# Generated by Django 3.2.6 on 2021-08-20 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=5)),
                ('title', models.TextField(max_length=20)),
                ('description', models.TextField(max_length=255)),
            ],
        ),
    ]
