from django.urls import path
from . import views

urlpatterns = [
    path('<int:post_id>/', views.single_post_page),
    path('', views.index),

]