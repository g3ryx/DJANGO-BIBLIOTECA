from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255, null=True)
    image = models.ImageField(upload_to='media/', null=True)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ImagesPost(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="media/", null=True)
    title = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.title
