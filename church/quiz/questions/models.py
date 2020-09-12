from django.db import models


class Hymn (models.Model):
    id = models.IntegerField(primary_key=True)
    Ename = models.CharField(max_length=200)
    Elyrics = models.TextField(max_length=2083)
    id2 = models.IntegerField()
    Yname = models.CharField(max_length=200)
    time = models.CharField(max_length=20)
    meter = models.CharField(max_length=10)
    Ylyrics = models.TextField (max_length=2083)
    created = models.DateTimeField(auto_now_add=True)






