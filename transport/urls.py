from django.urls import path
from . import views

app_name = 'transport'

urlpatterns = [
   path('', views.main_page_tran, name="mainpage"),
   path('return', views.second_page_tran, name="secondpage"),
   path('<data>/', views.first_change, name="firstchange"),
   


]   