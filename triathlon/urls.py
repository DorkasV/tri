from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('athletes/', views.AthleteListView.as_view(), name='athletes'),
    path('athlete/<int:pk>', views.AthleteDetailView.as_view(), name='athlete-detail'),
    path('events/', views.EventListView.as_view(), name='events'),
    path('event/<int:pk>', views.EventDetailView.as_view(), name='event-detail'),
    path('results/', views.ResultListView.as_view(), name='results'),
    path('result/<int:pk>', views.ResultDetailView.as_view(), name='result-detail'),
]
