from django.db import models

# # Create your models here.
# class Gamemanager(models.Model):
#     # id = models.IntegerField(primary_key=True)
#     Gamename = models.CharField(max_length=100)
#     Gameid = models.CharField(max_length=50)
#     Gamepassword = models.CharField(max_length=50)
#     created = models.DateTimeField(auto_now_add=True)

class Gamecredsmanagers(models.Model):
    # id = models.IntegerField(primary_key=True)
    Gamename = models.CharField(max_length=100)
    Gameid = models.CharField(max_length=50)
    Gamepassword = models.CharField(max_length=50)
    # created = models.DateTimeField(auto_now_add=True)