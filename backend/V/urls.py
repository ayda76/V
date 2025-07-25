"""
URL configuration for V project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path , include ,re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls.static import static
import os
from rest_framework.authtoken import views
from rest_framework import permissions
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
   # path("auth/", include("rest_framework.urls")),
    path("api/profile/", include("profile_app.api.urls")),
    path("api/post/", include("post_app.api.urls")),
    path("api/request/", include("request_app.api.urls")),
    
    path('auth/', include('djoser.urls')),
    path("auth/", include('djoser.urls.jwt')),
    path('', include('django_prometheus.urls')),

]
schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API For V System",
      default_version='v1',
      description="This snippet was created for frontend developers to know what APIs are provided and how to use them.",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="reza.sajadee@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns += [
   
    
   path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
 
]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)