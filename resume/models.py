from django.db import models


class Experience(models.Model):
    title = models.CharField(max_length=30)
    organization = models.CharField(max_length=30)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return f'{self.title} - {self.organization}'


class Education(models.Model):
    institution = models.CharField(max_length=50)
    degree = models.CharField(max_length=120)
    gpa = models.FloatField()
    start_date = models.DateField()
    end_date = models.DateField()
    courses = models.TextField()

    def __str__(self):
        return f'{self.institution}'
