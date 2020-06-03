# Generated by Django 3.0.6 on 2020-06-03 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('info', models.CharField(max_length=1000)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
    ]