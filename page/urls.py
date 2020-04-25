from django.urls import path
from .views import (
    # manage
    manage_list,
    
    # page
    page_show,
    page_list,
    page_create,
    page_update,
    page_delete,
    
    # carousel
    carousel_create,
    carousel_list,
    carousel_update,
)
urlpatterns = [
    path('', manage_list, name="manage_list"),
    
    # carousel
    path('carousel/list/', carousel_list, name="carousel_list"),
    path('carousel/create/',carousel_create, name='carousel_create'), 
    path('carousel/update/<int:pk>/',carousel_update, name='carousel_update'), 
    
    # page
    path('page/<slug:slug>/', page_show, name='page_show'), 
    path('page/page_list/',page_list, name='page_list'), 
    path('page/page_create/',page_create, name='page_create'), 
    path('page/page_update/<int:pk>/',page_update, name='page_update'), 
    path('page/page_delete/<int:pk>/',page_delete, name='page_delete'), 
]