from django.db import models

# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=200, blank=False, default='')
    text = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date =models.DateTimeField(auto_now=True)
