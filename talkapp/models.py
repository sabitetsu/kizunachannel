from django.db import models

class TalkModel(models.Model):
    inputWord = models.CharField(max_length=100)
    outputWord = models.CharField(max_length=200)
    
    def __str__(self):
        return self.inputWord