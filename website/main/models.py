from django.db import models

class News(models.Model):
    title = models.CharField('Название', max_length = 30)
    content = models.CharField('Содержание', max_length=300)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    date = models.DateTimeField('Дата публикации', auto_now=True)


    def __str__(self):
        return f'Новость: {self.title}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-date', ]




class Review(models.Model):
    author = models.CharField('Автор', max_length = 50)
    review = models.TextField('Содержание отзыва', max_length = 500)
    date = models.DateTimeField('Дата публикации', auto_now=True)

    def __str__(self):
        return f'Автор: {self.author}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-date', ]



