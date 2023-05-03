from django.urls import path
from . import views

urlpatterns = [
    path('', views.apis),
    path('works/', views.work_list),
    path('register/', views.register),

]
