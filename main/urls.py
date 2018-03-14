from django.urls import path

from main.views import article_view


urlpatterns = [
    path('article/<int:art_id>/', article_view),
]
