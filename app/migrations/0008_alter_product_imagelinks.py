# Generated by Django 4.2.7 on 2023-11-09 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_product_additionalinfo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='imageLinks',
            field=models.ImageField(upload_to='image/', verbose_name='image'),
        ),
    ]