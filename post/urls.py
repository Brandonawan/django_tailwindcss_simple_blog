from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name='index'),
    path('<slug:slug>/',views.post_detail, name='post_detail'),
    path('category/<int:pk>/',views.category_detail, name='category_detail'),
]