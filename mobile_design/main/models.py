from django.db import models

# Create your models here.
from .utilities import get_timestamp_path


class Developer(models.Model):
    name = models.CharField(max_length=30, verbose_name='Компания')
    destination = models.CharField(max_length=100, default='Плонета жопа', verbose_name='Расположение')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название категории')

    def __str__(self):
        return self.name


class Application(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название приложения')
    developer = models.ForeignKey(Developer, default=None, null=True, on_delete=models.PROTECT, verbose_name='Разработчик')
    description = models.TextField(verbose_name='Описание')
    categories = models.ManyToManyField(Category, default=None, null=True, verbose_name='Категории')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата создания на сайте')

    def __str__(self):
        return self.name

    def versions(self):
        self.versions = self.version_set.all()
        return self.versions

    def version(self, version_number):
        self.version = self.version_set.get(number=version_number)
        return self.version

    def last_version(self):
        self.last_version = self.version_set.all()[0]
        return self.last_version

    versions.short_description = 'Версии'
    version.short_description = 'Версия'
    last_version.short_secription = 'Последняя версия'

    class Meta:
        verbose_name = 'Приложения'
        verbose_name_plural = 'Приложение'
        ordering = ['-created_at']


class Version(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE, verbose_name='Приложение')
    number = models.FloatField(default=0, db_index=True, verbose_name='Номер версии')
    published = models.DateField(null=True, default=None, blank=True, verbose_name='Дата релиза')
    description = models.TextField(null=True, blank=True, verbose_name='Описание изменений')

    def __str__(self):
        return f"{self.application.name} ver: {self.number}"

    def main_screen(self):
        self.main_screen = self.screen_set.get(main=True)
        return self.main_screen

    def screens(self):
        self.screens = self.screen_set.filter(main=False)
        return self.screens

    def last_5_screens(self):
        self.screens = self.screen_set.filter(main=False)[:5]
        return self.screens

    def delete(self, *args, **kwargs):
        for screen in self.screen_set.all():
            screen.delete()
        super().delete(*args, **kwargs)

    screens.short_description = 'Экраны'
    main_screen.short_description = 'Основной экран'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
        ordering = ['-number']


class Pattern(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название паттерна')


class Element(models.Model):
    name = models.CharField(max_length=30, db_index=True, unique=True, verbose_name='Название элемента')
    order = models.SmallIntegerField(default=0, db_index=True, verbose_name='Порядок')
    super_element = models.ForeignKey('SuperElement', on_delete=models.PROTECT, null=True, blank=True,
                                      verbose_name='Группа элементов')


class SuperElementManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(super_element__isnull=True)


class SuperElement(Element):
    objects = SuperElementManager()

    def __str__(self):
        return self.name

    class Meta:
        proxy = True
        ordering = ('order', 'name')
        verbose_name = 'Группа элементов'
        verbose_name_plural = 'Группы элементов'


class SubElementManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(super_element__isnull=False)


class SubElement(Element):
    objects = SubElementManager()

    def __str__(self):
        return f'{self.super_element.name} - {self.name}'

    class Meta:
        proxy = True
        ordering = ('order', 'name')
        verbose_name = 'Элемент'
        verbose_name_plural = 'Элементы'


class Screen(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название экрана')
    application = models.ForeignKey(Version, on_delete=models.CASCADE, verbose_name='Приложение')
    # Скрины связан с приложением через объект версии
    main = models.BooleanField(default=False, db_index=True, verbose_name='Главный экран')
    pattern = models.ManyToManyField(Pattern, null=True, blank=True, verbose_name='Паттерн')
    elements = models.ManyToManyField(Element, null=True, blank=True, verbose_name='Элементы')
    screen = models.ImageField(null=True, blank=True, upload_to=get_timestamp_path,
                               verbose_name='Снимок экрана')  # Добавить в имя файла название приложения

    class Meta:
        verbose_name = 'Экран приложения'
        verbose_name_plural = 'Экраны приложений'
