from django.contrib import admin
from django.urls import path, include
from employeeapp import views as employeeapp_views

urlpatterns = [
    path('', employeeapp_views.index, name='index'),
    path('admin/', admin.site.urls),
    
]
