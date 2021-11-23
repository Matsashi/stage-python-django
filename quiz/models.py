from django.db import models


class Category(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=20)


class Quiz(models.Model):
    def __str__(self):
        return self.title
    title = models.CharField(max_length=255)
    categorie_set = models.ManyToManyField('Category', related_name='quiz')
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)


class Question(models.Model):
    def __str__(self):
        return self.question
    question = models.CharField(max_length=200, null=True)
    op1 = models.CharField(max_length=200, null=True)
    op2 = models.CharField(max_length=200, null=True)
    op3 = models.CharField(max_length=200, null=True)
    op4 = models.CharField(max_length=200, null=True)
    ans = models.CharField(max_length=200, null=True)
    quiz_set = models.ForeignKey(Quiz, on_delete=models.CASCADE)
