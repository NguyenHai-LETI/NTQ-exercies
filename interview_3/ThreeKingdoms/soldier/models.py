from django.db import models

class Soldier(models.Model):
    name = models.CharField(max_length=100)
    longevity = models.PositiveIntegerField()
    description = models.TextField()
    skills = models.TextField()

    def __str__(self):
        return f"Name: {self.name}, Longevity: {self.longevity}"
