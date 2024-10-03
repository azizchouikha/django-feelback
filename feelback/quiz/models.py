from django.db import models

class Forms(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Form {self.id} created on {self.created_at}"

class Questions(models.Model):
    title = models.CharField(max_length=150)
    form = models.ForeignKey(Forms, related_name='questions', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

class Answers(models.Model):
    value = models.IntegerField()  
    question = models.ForeignKey(Questions, related_name='answers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Answer {self.id} for question {self.question.id}"
    
from django.db import models

class Title(models.Model):
    title_name = models.CharField(max_length=255)

    def __str__(self):
        return self.title_name

class Orders(models.Model):
    order_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    form = models.ForeignKey(Forms, related_name='orders', on_delete=models.CASCADE)
