from django.urls import path
from app.views import (
    PostListCreateAPIView,
    PostDetailAPIView
)


urlpatterns = [
    path('post', PostListCreateAPIView.as_view()),
    path('post/<int:pk>', PostDetailAPIView.as_view()),
]