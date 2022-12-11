from django.urls import path
from . import views,user_func

app_name = 'lab'

urlpatterns = [
   path('', views.mainlab, name="mainlab"),
   path('search/', views.search, name="search"),
   path('login/', user_func.elogin, name="login"),
   path('logout/', user_func.elogout, name="logout"),
   path('register/', user_func.eregister, name="register"),
   path('<br>/', views.type, name="type"),
   path('<br>/hitch', views.useraction, name="data"),
   path('<br>/<mu>/<ui>', views.add_data, name="add_data"),



]