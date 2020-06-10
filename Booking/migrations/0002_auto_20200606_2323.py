# Generated by Django 3.0.6 on 2020-06-06 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dinner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dishname', models.CharField(max_length=60)),
                ('img', models.ImageField(upload_to='')),
                ('desc', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Lunch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dishname', models.CharField(max_length=60)),
                ('img', models.ImageField(upload_to='')),
                ('desc', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Dishes',
            new_name='Breakfast',
        ),
    ]
