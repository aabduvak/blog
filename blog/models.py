from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse
from django.utils import timezone

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField(max_length=120)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Tag(models.Model):
    caption = models.CharField(max_length=40, default='')

    def __str__(self):
        return f'{self.caption}'


class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.TextField(default='')
    image = models.ImageField(upload_to='posts', null=True)
    date = models.DateField(default=timezone.now())
    slug = models.SlugField(default='', blank=True, null=False, unique=True)

    content = models.TextField(default='')

    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, related_name='posts')

    tags = models.ManyToManyField(Tag)

    def get_absolute_url(self):
        return reverse('post-detail-page', args=[self.slug])

    def __str__(self):
        return f'{self.title}'
