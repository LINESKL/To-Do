from django.db import models

class Task(models.Model):
     # Поля модели
    title = models.CharField(max_length=200) 
    description = models.TextField(blank=True, null=True)  
    created_at = models.DateTimeField(auto_now_add=True) 
    due_date = models.DateTimeField()  
    completed = models.BooleanField(default=False)  
    priority = models.CharField(max_length=10, choices=[('low', 'Низкий'), ('medium', 'Средний'), ('high', 'Высокий')], default='medium',)  # Приоритет задачи

    # Метод для отображения названия задачи при выводе объекта
    def __str__(self):
        return self.title
