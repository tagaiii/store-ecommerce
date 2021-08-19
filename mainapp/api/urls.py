from django.urls import path

from .api_views import (
    CategoryAPIView,
    CategoryDetailAPIView,
    CustomerListAPIView, 
    SmartphoneListAPIView, 
    SmartphoneDetailAPIView,
    NotebookListAPIView,
    NotebookDetailView
)

urlpatterns = [
    path('categories/', CategoryAPIView.as_view(), name='categories'),
    path('categories/<str:id>', CategoryDetailAPIView.as_view(), name='categories_detail'),
    path('smartphones/', SmartphoneListAPIView.as_view(), name='smartphones'),
    path('notebooks/', NotebookListAPIView.as_view(), name='notebooks'),
    path('smartphones/<str:id>', SmartphoneDetailAPIView.as_view(), name='smartphone_detail'),
    path('notebooks/<str:id>', NotebookDetailView.as_view(), name='notebook_detail'),
    path('customers/', CustomerListAPIView.as_view(), name='customers')
]