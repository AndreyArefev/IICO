# Generated by Django 4.2.7 on 2023-11-08 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='iico_id',
            field=models.IntegerField(null=True),
        ),
    ]