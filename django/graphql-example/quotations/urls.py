from django.urls import path
from strawberry.django.views import AsyncGraphQLView, GraphQLView

from . import views
from .schema import schema

urlpatterns = [
    path("", views.index, name="index"),
    path("graphql/sync", GraphQLView.as_view(schema=schema)),
    path("graphql", AsyncGraphQLView.as_view(schema=schema)),
]
