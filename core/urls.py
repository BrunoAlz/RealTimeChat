from django.urls import path
from core import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
]

htmx_urlpatterns = [
    path('add_task', views.add_task, name='add_task'),
    path('search/', views.search_task, name='search_task'),
    path('like/<int:id>/', views.like, name='like'),
    path('del_task/<int:id>/', views.del_task, name='del_task'),
]

urlpatterns += htmx_urlpatterns