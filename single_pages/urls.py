from single_pages import views
from django.urls import path
urlpatterns = [
    path('about_me/', views.aboutme),
    path('',views.landing)
]