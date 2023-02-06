
from .views import ItemList, ItemDetail
from django.urls import path, include
urlpatterns = [
    path('items/', ItemList.as_view(), name='item-list'),
    path('items/<int:pk>/', ItemDetail.as_view(), name='item-detail'),
path('api/', include('myapp.urls')),
]