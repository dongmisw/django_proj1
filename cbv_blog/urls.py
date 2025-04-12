from django.urls import path

from cbv_blog.views import PostList

from cbv_blog.views import PostDetail

urlpatterns =[
    path('',PostList.as_view()),
    path('<int:pk>/',PostDetail.as_view()),
]