from django.urls import path
from .import views

urlpatterns=[
    path('',views.home,name='home'),
    path('crud_page/',views.show_laptop,name='crud_page'),
    path('detail_laptop/<str:id>',views.show_all_data,name='detail_laptop'),
    path('create_laptop/',views.create_laptop,name='create_laptop'),
    path('update_laptop/<str:id>/',views.update_laptop,name='update_laptop'),
    path('delete_laptop/<str:id>/',views.delete_laptop,name='delete_laptop'),
     path('show_all/<str:id>/',views.show_all_data,name='show_all')
]