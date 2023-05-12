from django.db import models
from django.urls import reverse


# Create your models here.
def upload_photo_to(self, filename):
    return f'products/{self.slug}/{filename}'


class Product(models.Model):
    materials = [
        ('Ясень', 'Ясень'),
        ('Дуб', 'Дуб'),
        ('Бук', 'Бук'),
    ]
    lamps = [
        ('ИН-8', 'ИН-8'),
        ('ИН-12', 'ИН-12'),
        ('ИН-14', 'ИН-14'),
        ('ИН-16', 'ИН-16'),
        ('ИН-17', 'ИН-17'),
        ('ИН-18', 'ИН-18'),
    ]
    currency = [
        ('4', '4'),
        ('6', '6'),
    ]
    views = [
        ('string', 'строка'),
        ('card', 'карточка')
    ]
    material = models.CharField(max_length=50, choices=materials, verbose_name='Материал', db_index=True, blank=True,
                                null=True)
    lamp_currency = models.CharField(max_length=1, choices=currency, verbose_name='Кол-во ламп', db_index=True,
                                     blank=True, null=True)
    lamp_type = models.CharField(max_length=10, choices=lamps, verbose_name='Тип ламп', db_index=True, blank=True,
                                 null=True)
    name = models.CharField(max_length=200, verbose_name='Название', db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image1 = models.ImageField(upload_to=upload_photo_to, verbose_name='Главная картинка', blank=True)
    image2 = models.ImageField(upload_to=upload_photo_to, verbose_name='Картинка №2', blank=True)
    image3 = models.ImageField(upload_to=upload_photo_to, verbose_name='Картинка №3', blank=True)
    description = models.TextField(blank=True, verbose_name='Описание', )
    width = models.PositiveIntegerField(blank=True, verbose_name='Ширина', null=True)
    height = models.PositiveIntegerField(blank=True, verbose_name='Высота', null=True)
    length = models.PositiveIntegerField(blank=True, verbose_name='Длина', null=True)
    price = models.DecimalField(max_digits=10, decimal_places=3, verbose_name='Цена')
    stock = models.PositiveIntegerField(verbose_name='Наличие')
    available = models.BooleanField(default=True, verbose_name='Доступно')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создано', )
    updated = models.DateTimeField(auto_now=True, verbose_name='Изменено', )

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product-detail', args=[self.id, self.slug])


class Review(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя', db_index=True)
    surname = models.CharField(max_length=50, verbose_name='Фамилия', db_index=True)
    review_text = models.CharField(max_length=500, verbose_name='Отзыв', db_index=True)
    available = models.BooleanField(default=False, verbose_name='Доступно')

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'