from django.db import models

class TalkModel(models.Model):
    inputWord = models.CharField(max_length=100)
    outputWord = models.CharField(max_length=200)
    
    def __str__(self):
        return self.inputWord

class UserModel(models.Model):
    name = models.CharField(max_length=100)
    birthday = models.DateField()
    old = models.IntegerField()
    friendry = models.IntegerField()

class UserLike(models.Model):
    food = models.CharField(max_length=100)
    music = models.CharField(max_length=100)