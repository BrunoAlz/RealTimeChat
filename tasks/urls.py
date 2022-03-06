from django.urls import path
from tasks import views

app_name = 'task'

urlpatterns = [
    path('', views.tasks_index, name='tasks_index'),
]

htmx_urlpatterns = [
    path('add_task', views.add_task, name='add_task'),
    path('search/', views.search_task, name='search_task'),
    path('like/<int:id>/', views.like, name='like'),
    path('del_task/<int:id>/', views.del_task, name='del_task'),
]

urlpatterns += htmx_urlpatterns

