
from django.db import models
from django.shortcuts import reverse

# Create your models here.


class World(models.Model):
    title = models.CharField('Название мира', max_length=150, unique=True)
    description = models.TextField('Описание мира')
    image = models.ImageField('Изображение', upload_to='worlds_images/')
    creation_date = models.DateTimeField('Датта создания', auto_now_add=True)
    slug = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('world_detail_url', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Мир'
        verbose_name_plural = 'Миры'


class Category(models.Model):
    world = models.ForeignKey(World, verbose_name='Мир', related_name='categories', on_delete=models.CASCADE)
    title = models.CharField('Название категории', max_length=150, unique=True)
    description = models.TextField('Описание категории')
    image = models.ImageField('Изображение', upload_to='categories_images/')
    creation_date = models.DateTimeField('Датта создания', auto_now_add=True)
    slug = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category_detail_url', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class CategoryRooms(models.Model):
    category = models.ForeignKey(Category, verbose_name='Категория', related_name='rooms', on_delete=models.CASCADE)
    title = models.CharField('Название комнаты', max_length=150, unique=True)
    type_of_room = models.BooleanField(default=False, help_text='По дефолту открыта')
    description = models.TextField('Описание комнаты')
    image = models.ImageField('Изображение', upload_to='category_rooms_images/')
    creation_date = models.DateTimeField('Датта создания', auto_now_add=True)
    slug = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category_room_detail_url', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Комната категории'
        verbose_name_plural = 'Комнаты категорий'


class Topic(models.Model):
    room = models.ForeignKey(CategoryRooms, verbose_name='Комната', related_name='topic', on_delete=models.CASCADE)
    title = models.CharField('Название статьи', max_length=150, unique=True)
    body = models.TextField('Текст статьи')
    topic_image = models.ImageField(
        'Изображение', upload_to='topic_title_image/', default='categories_images/SmartCheap.png'
    )
    creation_date = models.DateTimeField('Датта создания', auto_now_add=True)
    update_date = models.DateTimeField('Датта редактирования', auto_now=True)
    slug = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('topic_details_url', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class TopicRooms(models.Model):
    topic = models.ForeignKey(Topic, verbose_name='Статья', related_name='rooms', on_delete=models.CASCADE)
    title = models.CharField('Название комнаты', max_length=150, unique=True)
    type_of_room = models.BooleanField(default=False, help_text='По дефолту открыта')
    description = models.TextField('Описание комнаты')
    image = models.ImageField('Изображение', upload_to='topic_rooms_images/')
    creation_date = models.DateTimeField('Датта создания', auto_now_add=True)
    slug = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('topic_room_detail_url', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Комната статьи'
        verbose_name_plural = 'Комнаты статей'


class RoomsProjects(models.Model):
    room = models.ForeignKey(TopicRooms, verbose_name='Комната', related_name='projects', on_delete=models.CASCADE)
    title = models.CharField('Название проэкта', max_length=150, unique=True)
    type_of_project = models.BooleanField(default=False, help_text='По дефолту открыт')
    description = models.TextField('Краткое описание проэкта')
    body = models.TextField('Полное описание проэкта', blank=True)
    image = models.ImageField('Изображение', upload_to='rooms_projects_images/')
    creation_date = models.DateTimeField('Датта создания', auto_now_add=True)
    slug = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project_url', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Проэкт комнаты'
        verbose_name_plural = 'Проэкты комнат'


class TopicImage(models.Model):
    topic = models.ForeignKey(Topic, verbose_name='Статья', related_name='topic_images', on_delete=models.CASCADE)
    title = models.CharField('Название изображения', max_length=150)
    description = models.TextField('Описание изображения', max_length=500)
    image = models.ImageField('Изображение', upload_to='topics_images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Изобрежение'
        verbose_name_plural = 'Изображения'


class ProjectsImages(models.Model):
    project = models.ForeignKey(
        RoomsProjects, verbose_name='Проэкт', related_name='project_images', on_delete=models.CASCADE
    )
    title = models.CharField('Название изображения', max_length=150)
    description = models.TextField('Описание изображения')
    image = models.ImageField('Изображение', upload_to='projects_images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
