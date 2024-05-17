from celery import shared_task
from .models import FileUpload


@shared_task
def count_words_in_file(file_id):
    file_upload = FileUpload.objects.get(id=file_id)
    with open(file_upload.file.path, 'r') as f:
        text = f.read()
    word_count = len(text.split())
    file_upload.word_count = word_count
    file_upload.save()
