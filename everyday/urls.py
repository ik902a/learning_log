from django.urls import path
from . import views

app_name = 'everyday'
urlpatterns = [
    path('', views.index, name='index'),
    path('expenses/', views.expenses, name='expenses'),
    # path('topics/<int:topic_id>/', views.topic, name='topic'),
]