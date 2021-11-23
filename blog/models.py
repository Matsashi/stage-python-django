from django.db import models


class Category(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=20)


class Post(models.Model):
    def __str__(self):
        return self.title
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categorie_set = models.ManyToManyField('Category', related_name='posts')


class Comment(models.Model):
    def __str__(self):
        return self.body
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post_set = models.ForeignKey('Post', on_delete=models.CASCADE)
