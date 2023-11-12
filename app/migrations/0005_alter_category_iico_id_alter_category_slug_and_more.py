# Generated by Django 4.2.7 on 2023-11-08 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_category_iico_id_alter_product_iico_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='iico_id',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='iico_id',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
