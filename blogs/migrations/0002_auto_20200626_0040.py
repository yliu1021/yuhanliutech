# Generated by Django 3.0.3 on 2020-06-26 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='published_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
