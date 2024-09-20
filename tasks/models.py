from django.db import models
from django.contrib.auth.models import AbstractUser

class Utilizadores(AbstractUser):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='utilizadores_set',
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        related_query_name='utilizadores',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='utilizadores_set',
        blank=True,
        help_text=('Specific permissions for this user.'),
        related_query_name='utilizadores',
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
    

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pendente'),
        ('in_progress', 'Em andamento'),
        ('completed', 'Concluído'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='pending')
    due_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(Utilizadores, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
