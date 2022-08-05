from django.db import models
from user.models import Author

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    is_published = models.BooleanField()
    created_at = models.DateTimeField()