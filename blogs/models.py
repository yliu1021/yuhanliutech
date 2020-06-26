from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=30)
    published_date = models.DateField(auto_now_add=True)
    blog = models.TextField()

    def __str__(self):
        return f'{self.title} - {self.published_date}'
