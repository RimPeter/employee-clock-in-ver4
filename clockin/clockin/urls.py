from django.contrib import admin
from django.urls import path, include
from employeeapp import views as index_views

urlpatterns = [
    path('', index_views.index, name='index'),
    path('admin/', admin.site.urls),
    
]
