from django.contrib import admin
from django.urls import path
from . import views
from homepage.views import DetailLaptopView, DeleteLaptopView, UpdateLaptopOView, UpdateLaptopDView
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name = 'laptops'),
    path('register/', views.register, name = 'register'),
    path('login/', auth_views.LoginView.as_view(template_name = 'homepage/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL},  name = 'logout'),
    path('explore/', views.explore, name = 'explore'),
    path('laptop/<int:pk>/', DetailLaptopView.as_view(), name = 'laptop-details'),
    path('laptop/<int:pk>/delete/', DeleteLaptopView.as_view(), name = 'delete-laptop'),
    path('laptop/<int:pk>/update1/', UpdateLaptopOView.as_view(), name = 'update1-laptop'),
    path('laptop/<int:pk>/update2/', UpdateLaptopDView.as_view(), name = 'update2-laptop'),
    path('laptop/new1', views.add_laptopo_data, name = 'new1-laptop'),
    path('laptop/new2', views.add_laptopd_data, name = 'new2-laptop'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
