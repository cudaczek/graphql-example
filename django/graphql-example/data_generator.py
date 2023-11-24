import datetime
import os
import random
import re
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'graphql-example.settings')
django.setup()
from quotations.models import Book, BibleQuotation, Quotation
import pytz
bible = open('bib.txt', 'r')
count = 0

bib = Book(name="Biblia Tysiąclecia", author="praca zbiorowa", pub_date=datetime.datetime(year=datetime.MINYEAR, month=1, day=2, tzinfo=pytz.UTC))
bib.save()
# bib = Book.objects.get(name="Biblia Tysiąclecia")
while True:
    count += 1

    line = bible.readline()
    match = re.match(r"(\w+)\s+(\d+)\s+(\d+)\s+(.*)", line)
    if match:
        bq = BibleQuotation(
            book_id=bib.id,
            text=match.group(4),
            pub_date=datetime.datetime(year=datetime.MINYEAR + len(match.group(1)), month=8, day=random.randint(1, 25), tzinfo=pytz.UTC),
            bible_book=match.group(1),
            chapter=match.group(2),
            verse=match.group(3),
        )
        bq.save()
    if not line:
        break

bible.close()

epopeja = open('Epopeja.txt', 'r')
count = 0

ep = Book(name="Pan Tadeusz czyli ostatni zajazd na Litwie", author="Adam Mickiewicz", pub_date=datetime.datetime(year=1834, month=5, day=28, tzinfo=pytz.UTC))
ep.save()
# ep = Book.objects.get(name="Pan Tadeusz czyli ostatni zajazd na Litwie")
while True:
    count += 1

    line = epopeja.readline()
    match = re.match(r"(.*)", line)
    if match:
        bq = Quotation(
            book_id=ep.id,
            text=match.group(1),
            pub_date=datetime.datetime(year=1834, month=5, day=28, tzinfo=pytz.UTC)
        )
        bq.save()

    if not line:
        break

epopeja.close()
