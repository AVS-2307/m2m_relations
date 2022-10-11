from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение', )
    categories = models.ManyToManyField('Category', related_name='articles', through='Relations',
                                        through_fields=('article', 'category'))

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=256, db_index=True, verbose_name='Наименование категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']

    def __str__(self):
        return self.title


class Relations(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scope')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='scope')
    main = models.BooleanField(verbose_name='Главная категория')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return str(self.category) if self.category else ''
