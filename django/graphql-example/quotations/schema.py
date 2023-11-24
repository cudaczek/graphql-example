import strawberry
import strawberry_django
from strawberry_django.optimizer import DjangoOptimizerExtension

from .types import BibleQuotation, Quotation, QuotationWithOrder, QuotationOrder, Book, BookWithQuotations


@strawberry.type
class Query:
    bible_quotations: list[BibleQuotation] = strawberry.django.field()
    quotations: list[Quotation] = strawberry.django.field()
    quotations_with_order: list[QuotationWithOrder] = strawberry.django.field(order=QuotationOrder)
    books: list[Book] = strawberry.django.field()
    booksAndQuotas: list[BookWithQuotations] = strawberry.django.field()


schema = strawberry.Schema(
    query=Query,
    extensions=[
        DjangoOptimizerExtension,  # not required, but highly recommended
    ],
)