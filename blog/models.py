from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = ('DR','Draft')
        PUBLISHED = ('PB','Published')
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='author_posts')
    status = models.CharField(
        choices=Status.choices, default=Status.DRAFT, max_length=2)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
