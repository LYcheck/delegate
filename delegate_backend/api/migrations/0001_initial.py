# Generated by Django 3.2.6 on 2021-08-29 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='None', max_length=255)),
                ('author', models.CharField(default='None', max_length=36)),
                ('description', models.CharField(default='None', max_length=255)),
                ('parent_list', models.CharField(default='None', max_length=36)),
                ('parent_group', models.CharField(default='None', max_length=36)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='None', max_length=255)),
                ('author', models.CharField(default='None', max_length=36)),
                ('description', models.CharField(default='None', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='None', max_length=100)),
                ('type', models.CharField(default='None', max_length=50)),
                ('description', models.CharField(default='None', max_length=255)),
                ('parent_list', models.CharField(default='None', max_length=36)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='None', max_length=100)),
                ('type', models.CharField(default='None', max_length=50)),
                ('description', models.CharField(default='None', max_length=255)),
                ('author', models.CharField(default='None', max_length=36)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(default='None', max_length=255)),
                ('password', models.TextField(default='None', max_length=255)),
                ('email', models.EmailField(default='None', max_length=254)),
            ],
        ),
    ]