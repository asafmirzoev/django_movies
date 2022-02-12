from django.urls import reverse
from django.db import models
from datetime import date

from django.db.models.deletion import CASCADE


class Category(models.Model):
    name = models.CharField('Категория', max_length=150)
    description = models.TextField('Описание')
    url = models.SlugField(max_length=160, unique=True)


    def __str__(self):
        return self.name

    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    



class Actor(models.Model):
    name = models.CharField('Имя', max_length=100)
    age = models.PositiveSmallIntegerField('Возраст', default=0)
    description = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to='actors/')
    slug = models.CharField("URL", max_length=160, unique=True, null=True)


    def __str__(self):
        return self.name
    

    def get_absolute_url(self):
        return reverse('actor_detail', kwargs={'slug': self.slug})

    
    class Meta:
        verbose_name = 'Актёры и Режиссёры'
        verbose_name_plural = 'Актёры и Режиссёры'




class Genre(models.Model):
    name = models.CharField('Жанр', max_length=100)
    description = models.TextField('Описание')
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    
    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Movie(models.Model):
    title = models.CharField('Назавние', max_length=100)
    tagline = models.CharField('Слоган', max_length=100, default='')
    description = models.TextField('Описание')
    poster = models.ImageField('Постер', upload_to='movies/')
    year = models.PositiveSmallIntegerField('Дата выхода', default=2022)
    country = models.CharField('Страна', max_length=50)
    directors = models.ManyToManyField(Actor, verbose_name='Режиссёр', related_name='film_director')
    actors = models.ManyToManyField(Actor, verbose_name='Актёры', related_name='film_actors')
    genre = models.ManyToManyField(Genre, verbose_name='Жанр')
    world_premire = models.DateField('Премьера в мире', default=date.today)
    budget = models.PositiveIntegerField('Бюджет', default=0, help_text='Указывать сумму в долларах')
    fees_in_usa = models.PositiveIntegerField('Сборы в США', default=0, help_text='Указывать сумму в долларах')
    fees_in_world = models.PositiveIntegerField('Сборы в Мире', default=0, help_text='Указывать сумму в долларах')
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.SET_NULL, null=True)
    trailer = models.CharField('Трейлер', max_length=50, null=True)
    url = models.SlugField(max_length=160, unique=True)
    draft = models.BooleanField('Черновик', default=False)



    def __str__(self):
        return self.title
    
    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True)


    def get_absolute_url(self):
        return reverse('movie_detail', kwargs={'slug': self.url})
    
    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
    

class MovieShots(models.Model):
    image = models.ImageField('Изображение', upload_to='movie_shots/')
    movie = models.ForeignKey(Movie, verbose_name='Фильм', on_delete=models.CASCADE)
    


    def __str__(self):
        return self.image.url

    
    class Meta:
        verbose_name = 'Кадр из фильма'
        verbose_name_plural = 'Кадры из фильма'



class RatingStar(models.Model):
    value = models.PositiveSmallIntegerField('Значение', default=0)


    def __str__(self):
        return self.title

    
    class Meta:
        verbose_name = 'Звёзда рейтинга'
        verbose_name_plural = 'Звёзды рейтинга'


class Rating(models.Model):
    ip = models.CharField('IP адрес', max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name='Звезда')
    movie = models.ForeignKey(Movie, on_delete=CASCADE, verbose_name='Фильм')


    def __str__(self):
        return f'{self.star} - {self.movie}'

    
    class Meta:
        verbose_name = 'Рейтиг'
        verbose_name_plural = 'Рейтиги'
    


class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField('Имя', max_length=100)
    text = models.TextField('Сообщение', max_length=5000)
    parent = models.ForeignKey('self', verbose_name='Ролитель', on_delete=models.SET_NULL, blank=True, null=True)
    movie = models.ForeignKey(Movie, verbose_name='Фильм', on_delete=models.CASCADE)



    def __str__(self):
        return f'{self.name} - {self.movie}'

    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'