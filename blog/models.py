from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'
    def __str__(self):
        return f'[{self.pk : >4}] {self.title : >20}   {self.created_at : >40}       {self.updated_at}'
    class Meta:
        ordering = ['-created_at']

