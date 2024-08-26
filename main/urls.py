from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from main import views  

urlpatterns = [
    path('home/', views.landingPage.as_view(), name='home'),
    # path('contact/', views.contact_page, name='contact_page'),
    path('Card/', views.card_page, name='card_page'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('addpost/', views.addpost.as_view(), name='addpost'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
