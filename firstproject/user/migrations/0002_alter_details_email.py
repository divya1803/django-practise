# Generated by Django 4.0.6 on 2022-08-02 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='email',
            field=models.EmailField(max_length=128),
        ),
    ]
