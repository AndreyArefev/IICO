# Generated by Django 4.2.7 on 2023-11-09 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_modifier_alter_product_modifiers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='additionalInfo',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
