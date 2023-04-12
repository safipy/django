from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='')
    description = models.TextField()
    created_data = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

