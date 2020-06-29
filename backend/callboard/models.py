from django.contrib.auth.models import User
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.shortcuts import reverse


class Category(MPTTModel):
    name = models.CharField(verbose_name='Категория', max_length=50, unique=True)
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    slug = models.SlugField(verbose_name='url', max_length=200)

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']


class FilterAdvert(models.Model):
    name = models.CharField(verbose_name='Имя фильтра', max_length=50, unique=True)
    slug = models.SlugField(verbose_name='url', max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Фильтр'
        verbose_name_plural = 'Фильтры'


class Advert(models.Model):
    ''' Объявления '''
    user = models.ForeignKey(User, verbose_name='пользователь', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    filter = models.ForeignKey(FilterAdvert, verbose_name='Фильтры', on_delete=models.CASCADE)
    subject = models.CharField(verbose_name='Тема', max_length=200)
    description = models.TextField(verbose_name='Объявление')
    images = models.ForeignKey('gallery.Gallery',
                               verbose_name='галерея',
                               null=True, blank=True,
                               on_delete=models.SET_NULL)
    file = models.FileField(verbose_name='Файл', upload_to='callboard_file/', blank=True, null=True)
    price = models.DecimalField(verbose_name='Цена', max_digits=5, decimal_places=2)
    created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    moderation = models.BooleanField(verbose_name='Активный', default=False)
    # TODO: генератор для слаг (id+subject)
    slug = models.SlugField(verbose_name='url', max_length=200, unique=True)

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def get_absolute_url(self):
        return reverse('advert_detail',
                       kwargs={'category': self.category.slug,
                               'slug': self.slug})
