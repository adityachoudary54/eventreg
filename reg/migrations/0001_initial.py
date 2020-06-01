# Generated by Django 3.0.6 on 2020-06-01 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regId', models.CharField(default='', max_length=40)),
                ('date', models.DateField(auto_now_add=True)),
                ('username', models.CharField(max_length=200)),
                ('mobile', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('idcard', models.FileField(upload_to='registerImages/')),
                ('regType', models.CharField(max_length=20)),
                ('noTickets', models.CharField(max_length=10)),
            ],
        ),
    ]