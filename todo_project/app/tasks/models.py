from django.db import models

class Task(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('in_progress', 'В процессе'),
        ('done', 'Выполнена'),
    ]

    title = models.CharField('Название', max_length=200)
    description = models.TextField('Описание', blank=True)
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    due_date = models.DateTimeField('Срок выполнения')
    status = models.CharField('Статус', max_length=20, choices=STATUS_CHOICES, default='new')

    def __str__(self):
        return self.title
