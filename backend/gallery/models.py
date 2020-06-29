from django.db import models
from django.contrib.auth.admin import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from time import time
from django.utils.text import slugify


def gen_slug(s):
    '''  генерирую слаг.
    на вход получаю строку с иеменем. библиотека slugify преобразует это имя:
    убирает не подходящие символы и транслитерирует в латиницу.
    например: это строка с именем = eto-stroka-s-imenem
    так слагифай преодразут имя. Кроме этого я для уникальности добавляю
    декущую дату и время в значентях секунд
    в результате слаг будет выглядеть так: 1589003123-download-2jpg
    '''
    new_slug = slugify(s, allow_unicode=True)
    return str(int(time())) + '-' + new_slug


def get_path_image(uname, iname):
    '''формирую имя файла картинки.
    к имени спереди добавляю путь - папку, с именем пользователя, где будет
    храниться картинка.
    Если этого не делать все будут в одной папке и имена будут перезатираться'''
    # print('========>', uname)
    # print('========>', iname)
    path = str(uname).lower() + '/' + str(iname)
    #    print('========>', path)
    return path


class Photo(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Фото', max_length=50, blank=True, null=True, default='описание', unique=False)
    image = models.ImageField(verbose_name='Фотография',
                              upload_to='gallery/')
    created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    slug = models.SlugField(verbose_name='url', max_length=200, unique=True)

    def save(self, *args, **kwargs):
        ''' переопределяю метод save
        чтоб изменить значения slug и image.name
        '''
        self.slug = gen_slug(self.image.name)
        self.image.name = get_path_image(self.user, self.image.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


class Gallery(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=50)
    photos = models.ManyToManyField(Photo, verbose_name='Фото')
    created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    slug = models.SlugField(verbose_name='url', max_length=200, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галереи'
