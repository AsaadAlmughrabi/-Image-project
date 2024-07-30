from django.urls import path
from .views import home_view, image_detail_view

urlpatterns = [
    path("", home_view, name="home"),
    path("<int:pk>", image_detail_view, name="detail"),
]
