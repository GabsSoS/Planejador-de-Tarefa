from django.contrib.auth.models import User
from django.db import models

STATUS_CHOICES = (
    ('1', 'Não iniciado'),
    ('2', 'Em andamento'),
    ('3', 'Finalizado'))

class PersonalUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)
    
    status = models.CharField(
        max_length=100,
        choices=STATUS_CHOICES,
        blank=True,
        null=True,
    )
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.title