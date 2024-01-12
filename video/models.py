from django.db import models


class Video(models.Model):
    video = models.TextField(blank=False)
    subtitles = models.TextField(blank=False)
    image=models.TextField(blank=False)
    
    def __str__(self):
        return f"Video {self.id}"