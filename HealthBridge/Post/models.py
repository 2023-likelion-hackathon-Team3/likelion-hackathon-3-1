from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/post/tag/{self.slug}"


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    head_image = models.ImageField(upload_to="post/images/%Y/%m/%d/", blank=True)

    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return f"[{self.pk}]{self.title}"
