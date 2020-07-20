"""Nativ_Plus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from Trips import views as trip_views
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name="register"),
    path('', user_views.LogUserIn, name="login"),
    path('index/', user_views.LogUserIn, name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
    path('Home/', trip_views.homepage, name="home"),
    path('NewTrip/', trip_views.createTrip, name="newtrip"),
    path('DriverList/', trip_views.driverlist, name="driverlist"),
    path('TripInfo/', trip_views.tripinfo, name="tripinfo"),
    path('TripInfo/<str:pk>', trip_views.tripinfo, name="tripinfo_with_PK"),
    path('Update/<str:pk>', trip_views.updateTrip, name="updatetrip"),
    path('Delete/<str:pk>', trip_views.deleteTrip, name="deletetrip"),
]
