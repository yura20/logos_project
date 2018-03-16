from django.urls import path

from main.views import article_view
from main.views import main_view

app_name = "main"
urlpatterns = [
    
    path('article/<int:art_id>/', article_view, name="single_art"),
    path('', main_view, name="home")
]
