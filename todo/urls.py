
from django.contrib import admin
from django.urls import path, include
from todolist_app import views as todolist_app_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todolist_app_view.index,name='index'),
    path('todolist/', include('todolist_app.urls')),
    path('account/', include('users_app.urls')),
    path('analytics', todolist_app_view.analytics, name='analytics'),
    path('about', todolist_app_view.about, name='about'),
    
]
