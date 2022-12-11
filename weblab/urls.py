from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lab/', include('instruments.urls')),
    path('userprofile/', include('user.urls')),#, namespace = "user" )),
    path('transport/', include('transport.urls')),
    path('technician/', include('technician.urls')),
    
]
