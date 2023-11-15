from django.db import models as m
from pytils.translit import slugify
from django.urls import reverse


class Category(m.Model):
    iico_id = m.CharField(max_length=1000, null=True)
    name = m.CharField(max_length=1000, null=False, unique=True)
    slug = m.SlugField(max_length=1000, null=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    objects = m.Manager()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            print(self.name)
            self.slug = slugify(self.name)
            print(self.slug)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('valentino_app:product_list_by_category',
                        args=[self.slug])


class Product(m.Model):
    iico_id = m.CharField(max_length=1000, null=True)
    name = m.CharField(max_length=1000, null=False)
    slug = m.SlugField(max_length=1000, null=True)
    category = m.ForeignKey(to='Category', on_delete=m.CASCADE, related_name='products')
    weight = m.DecimalField(max_digits=10, decimal_places=3)
    currentPrice = m.DecimalField(max_digits=10, decimal_places=2)
    description = m.TextField(blank=True, null=True)
    energyAmount = m.DecimalField(max_digits=10, decimal_places=3)
    energyFullAmount = m.DecimalField(max_digits=10, decimal_places=3)
    proteinsAmount = m.DecimalField(max_digits=10, decimal_places=3)
    fatAmount = m.DecimalField(max_digits=10, decimal_places=3)
    carbohydratesAmount = m.DecimalField(max_digits=10, decimal_places=3)
    proteinsFullAmount = m.DecimalField(max_digits=10, decimal_places=3)
    fatFullAmount = m.DecimalField(max_digits=10, decimal_places=3)
    carbohydratesFullAmount = m.DecimalField(max_digits=10, decimal_places=3)
    additionalInfo = m.TextField(blank=True, null=True)
    imageLinks = m.ImageField(upload_to='image/', verbose_name='image')
    modifiers = m.ManyToManyField(to='Modifier')

    class Meta:
        ordering = ['iico_id']
        indexes = [m.Index(fields=['iico_id']),
                   m.Index(fields=['name'])]

    objects = m.Manager()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            print(self.name)
            self.slug = slugify(self.name)
            print(self.slug)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('valentino_app:product_detail',
                        args=[self.slug, self.pk])


class Modifier(m.Model):
    iico_id = m.CharField(max_length=1000, null=True, unique=True)
    name = m.CharField(max_length=1000, null=False, unique=True)

    class Meta:
        ordering = ['name']
        indexes = [m.Index(fields=['iico_id'])]
        verbose_name = 'modifier'
        verbose_name_plural = 'modifiers'

    objects = m.Manager()


