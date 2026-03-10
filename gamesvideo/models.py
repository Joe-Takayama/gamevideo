import os
from django.db import models
from django.contrib.auth.models import User

class Video(models.Model):
    title = models.CharField(max_length=255)
    video = models.FileField(upload_to='videos/')
    description = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        if self.video:
            if os.path.isfile(self.video.path):
                os.remove(self.video.path)  # 実ファイル削除
        super().delete(*args, **kwargs)