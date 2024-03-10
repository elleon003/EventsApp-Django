from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('', views.events_list, name='events_list'),
    path('<slug:category_slug>/', views.events_list, name='events_list_by_category' ),
    path('<int:id>/<slug:slug>/', views.event_detail, name='event_detail'),
]