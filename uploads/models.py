from django.db import models


class FileUpload(models.Model):
    file = models.FileField(upload_to='uploads/')
    word_count = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
