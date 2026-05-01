from django.db import models

# Create your models here.

class MoodLog(models.Model):
    MOOD_CHOICES = [
        ('happy', '😊'),
        ('normal', '😐'),
        ('sad', '😢'),
    ]

    mood = models.CharField(max_length=10, choices=MOOD_CHOICES)
    action = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.mood} - {self.created_at}"