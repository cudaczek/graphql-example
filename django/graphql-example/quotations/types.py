from typing import Optional, List

import strawberry.django
from strawberry import auto

from . import models


@strawberry.django.type(models.Book)
class Book:
    id: auto
    name: auto
    author: auto
    pub_date: auto
    quotations: 'Quotation'


@strawberry.django.type(models.Quotation, pagination=True)
class Quotation:
    id: auto
    text: auto
    pub_date: auto
    book: 'Book'


@strawberry.django.type(models.Book)
class BookWithQuotations:
    id: auto
    name: auto
    author: auto
    pub_date: auto
    quotations: List['Quotation'] = strawberry.django.field()

    @strawberry.django.field
    def quotas_count(self, info) -> int:
        return self.quotations.count()


@strawberry.django.ordering.order(models.Quotation)
class QuotationOrder:
    id: auto
    text: auto


@strawberry.django.type(models.Quotation, order=QuotationOrder, pagination=True)
class QuotationWithOrder:
    id: auto
    text: auto
    pub_date: auto
    book: 'Book'


@strawberry.django.filters.filter(models.BibleQuotation, lookups=True)
class FruitFilter:
    id: Optional[int]
    bible_book: str


@strawberry.django.type(models.BibleQuotation, pagination=True, filters=FruitFilter)
class BibleQuotation:
    id: auto
    text: auto
    pub_date: auto
    bible_book: auto
    chapter: auto
    verse: auto
    book: 'Book'
