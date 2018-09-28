from django.urls import path

from . import views

app_name = 'manager'
urlpatterns = [
    # ex: /manager/
    path('', views.index, name='index'),
    # ex: /manager/5/
    path('<int:investor_id>/', views.detail, name='detail'),
    # ex: /manager/5/results/
    path('<int:investor_id>/results/', views.results, name='results'),
    # ex: /manager/5/vote/
    path('<int:investor_id>/vote/', views.vote, name='vote'),
]