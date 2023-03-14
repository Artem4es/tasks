from django.db import models


class Product(models.Model):
    article = models.CharField(verbose_name='Артикул', max_length=255)
    brand = models.CharField(verbose_name='Бренд', max_length=255)
    title = models.CharField(verbose_name='Наименование', max_length=255)

    def __str__(self):
        return self.article
