from django.urls import path
from core.views import PostAPIView

urlpatterns = [
    path('post', PostAPIView.as_view()),
]
