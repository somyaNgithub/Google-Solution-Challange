"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import include, path
from website import views



urlpatterns = [ path("admin/", admin.site.urls),
                path('', include('website.urls', namespace="website")),
                path('userform/', views.userform_view,name="userform"),
                path('afterlocation/', views.afterlocation_view, name="afterlocation"),
                path('about/', views.about_view, name="about"),
                path('login/', views.login_view, name="login"),
                path('map/', views.map_view, name="map"),
                path('index/', views.home_view, name="home"),
                path('fooddonate/', views.donate_view, name="fooddonate")]

