from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length= 500)
    content = models.CharField(max_length=1000)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs = {'pk': self.pk})

# class Comment(models.Model):
#     post = models.ForeignKey(to= Post, on_delete= models.CASCADE)
#     body = models.CharField(max_length=200)
#     user = models.ForeignKey(to = User, on_delete=models.CASCADE)
#
#     def get_absolute_url(self):
#         return reverse('comment-detail', kwargs={'pk': self.pk})