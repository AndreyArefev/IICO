# Generated by Django 4.2.7 on 2023-11-08 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000, unique=True)),
                ('slug', models.SlugField(max_length=1000, unique=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iico_id', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=1000)),
                ('weight', models.DecimalField(decimal_places=3, max_digits=10)),
                ('currentPrice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(blank=True)),
                ('energyAmount', models.DecimalField(decimal_places=3, max_digits=10)),
                ('energyFullAmount', models.DecimalField(decimal_places=3, max_digits=10)),
                ('proteinsAmount', models.DecimalField(decimal_places=3, max_digits=10)),
                ('fatAmount', models.DecimalField(decimal_places=3, max_digits=10)),
                ('carbohydratesAmount', models.DecimalField(decimal_places=3, max_digits=10)),
                ('proteinsFullAmount', models.DecimalField(decimal_places=3, max_digits=10)),
                ('fatFullAmount', models.DecimalField(decimal_places=3, max_digits=10)),
                ('carbohydratesFullAmount', models.DecimalField(decimal_places=3, max_digits=10)),
                ('additionalInfo', models.TextField(blank=True)),
                ('imageLinks', models.ImageField(upload_to='', verbose_name='image')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='app.category')),
                ('modifiers', models.ManyToManyField(to='app.product')),
            ],
            options={
                'ordering': ['iico_id'],
                'indexes': [models.Index(fields=['iico_id'], name='app_product_iico_id_db88c5_idx'), models.Index(fields=['name'], name='app_product_name_f168ea_idx')],
            },
        ),
    ]