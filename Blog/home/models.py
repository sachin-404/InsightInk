from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BlogModel(models.Model):
    title = models.CharField(max_length=1000)
    content = models.TextField()
    slug = models.SlugField(max_length=1000)
    image = models.ImageField(upload_to="blog_images")
    created_at = models.DateTimeField(auto_now_add=True)
