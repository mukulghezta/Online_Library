from django.db import models

class Book(models.Model):
    book_id = models.IntegerField(primary_key=True)
    book_name = models.CharField(max_length=100)
    book_author = models.CharField(max_length=100)
    book_language = models.CharField(max_length=30)
    book_quantity = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.book_name

class CD(models.Model):
    cd_id = models.IntegerField(primary_key=True)
    cd_name = models.CharField(max_length=100)
    cd_artist = models.CharField(max_length=100)
    cd_language = models.CharField(max_length=30)
    cd_quantity = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.cd_name