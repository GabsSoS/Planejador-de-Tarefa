from django.db import models

STATUS_CHOICES = (
    ('1','Não iniciado'),
    ('2', 'Em andamento'),
    ('3', 'Finalizado')
)

class Task(models.Model):
    owner = models.ForeignKey(
    "auth.User",
    related_name="snippets",
    on_delete=models.CASCADE
    )
    title = models.TextField(max_length=100, blank=True, null=True)
    create_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField(max_length=255)
    task_status = models.CharField(choices=STATUS_CHOICES)

    def __str__(self):
        return self.title