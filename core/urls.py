from django.urls import path
from core import views

urlpatterns = [
    path('product/',views.product_list.as_view()),
    path('product/<int:pk>/',views.product_detail.as_view()),
]