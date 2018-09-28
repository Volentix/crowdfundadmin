from django.urls import path

from . import views

app_name = 'manager'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:investor_id>/vote/', views.vote, name='vote'),
]