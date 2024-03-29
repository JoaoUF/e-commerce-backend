from django.urls import path
from core import views

urlpatterns = [
    path('product/',views.ProductList.as_view()),
    path('product/<uuid:pk>/',views.ProductDetail.as_view()),
]