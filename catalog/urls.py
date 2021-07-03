# Django imports
from django.urls import path

# Internal imports
from . import views

urlpatterns = [
    # ex: /catalog/
    path('', views.index, name='index'),
    # ex: /catalog/5/
    path('<int:book_id>/', views.detail, name='detail'),
    # ex: /catalog/5/chapters/
    path('<int:book_id>/chapters/', views.chapters, name='chapters'),
]