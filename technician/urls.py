from django.urls import path
from . import views

app_name = 'technician'

urlpatterns = [
   path('', views.main_page_tech, name="mainpage"),
   path('<data>/', views.change, name="change"),

]   