from django.db import models
from django.contrib.auth.models import User


STATUS_CHOICES = (
    ('1', 'Não iniciada'),
    ('2', 'Em andamente'),
    ('3', 'Finalizado')
)

class Task(models.Model):
    name = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='usuarios',
        )
    title = models.CharField(max_length=180)
    create_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(
        max_length=100,
        choices=STATUS_CHOICES,
        blank=True,
        null=True
    )
    
    def __str__(self):
        return self.name