
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class BlogPost(models.Model):

    title =models.CharField(max_length=255)
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    desc = models.CharField(max_length=130)
    content =models.TextField()
    image = models.ImageField(upload_to="picture", blank=True, null=True)
    dateTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.author) +  " Blog Title: " + self.title

    def get_absolute_url(self):
        return reverse('home')


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    dateTime = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')

class MyBlog(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    blogs = models.ManyToManyField(BlogPost)

    def __str__(self):
        return f"My Blogs for {self.user.username}"