from django.urls import path,include
from .import views

urlpatterns = [
    path('home/', views.landing_page, name='home'),
    path('contact/', views.contact_page, name='contact_page'),
    path('Card/', views.card_page, name='card_page'),
    path('post/<int:card_id>/', views.post_detail, name='post_detail'),
    path('Card_detail/<int:card_id>', views.detail_page,name = 'detail_page'),
   
    
]