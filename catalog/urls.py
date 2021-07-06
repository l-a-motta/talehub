# Django imports
from django.urls import path

# Internal imports
from . import views

app_name = 'catalog'
urlpatterns = [
    # ex: /catalog/
    path('', views.index, name='index'),
    # ex: /catalog/5/
    path('<int:book_id>/', views.details, name='details'),
    # ex: /catalog/5/chapter/2
    path('<int:book_id>/chapter/<int:chapter_id>', views.chapter, name='chapter'),
    # ex: /catalog/5/chapter/2/vote
    path('<int:book_id>/chapter/<int:chapter_id>/vote', views.vote, name='vote'),
    # ex: /add-book/
    path('add-book/', views.add_book, name='add-book'),
]