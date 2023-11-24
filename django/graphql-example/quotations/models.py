from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Quotation(models.Model):
    text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='quotations')


class BibleQuotation(Quotation):
    bible_book = models.CharField(max_length=200)
    chapter = models.IntegerField(default=0)
    verse = models.IntegerField(default=0)
