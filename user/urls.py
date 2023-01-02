from django.urls import path

from rest_framework.authtoken import views

from .views import RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', views.obtain_auth_token)
]

#! APPLICATION OLUŞTURMAK İÇİN;
#todo, 1- önce yeni bir app oluştur,
#todo, 2- bu app içinde models.py içinde model oluştur,
#todo, 3- serializer.py dosyasını ekle ve bu modele ait bir serializer yaz, 
#todo, 4- oluşturulan model ve serializer kullanarak view.py içinde view oluştur,
#todo, 5- urls.py dosyasını ekle ve bu view için bir url (endpoint) yaz.