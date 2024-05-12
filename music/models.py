from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=10)
    image = models.URLField(null=True)
    create_date = models.DateField(auto_now_add=True,null=True)
    Last_update = models.DateField(auto_now=True)


class Albom(models.Model):
    title = models.CharField(max_length=10)
    artist = models.ForeignKey(Artist,on_delete=models.CASCADE,null=True)
    cover = models.URLField(null=True)
    popular = models.PositiveIntegerField(default=0)
    create_date = models.DateField(auto_now_add=True,null=True)
    Last_update = models.DateField(auto_now=True)
    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['id'])
        ]

class Songs(models.Model):
    title = models.CharField(max_length=10)
    cover = models.URLField(null=True)
    albom = models.ForeignKey(Albom,on_delete=models.CASCADE,null=True)
    listened = models.PositiveIntegerField(default=0)
    create_date = models.DateField(auto_now_add=True,null=True)
    Last_update = models.DateField(auto_now=True)

    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['id'])
        ]

