# Generated by Django 5.0.3 on 2024-03-11 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_image', models.CharField(max_length=255)),
                ('xona_soni', models.IntegerField()),
                ('manzil', models.CharField(max_length=255)),
                ('narx', models.IntegerField()),
                ('snippet', models.CharField(max_length=255)),
                ('kun', models.DateField()),
                ('vaqt', models.TimeField()),
            ],
        ),
    ]
