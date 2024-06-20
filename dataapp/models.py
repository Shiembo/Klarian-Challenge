from django.db import models

class DataFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class DataEntry(models.Model):
    data_file = models.ForeignKey(DataFile, on_delete=models.CASCADE)
    data = models.JSONField()
    entry_type = models.CharField(max_length=100)
