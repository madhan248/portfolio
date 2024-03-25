"""
URL configuration for portfolio project.

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
from django.urls import path
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_401_UNAUTHORIZED
from rest_framework.views import APIView

class HealthCheck(APIView):
    def get(self, request, *args, **kwargs):
        return Response({
                    "status": HTTP_200_OK,
                    "message": "Success"
                },HTTP_200_OK)

class NewApi(APIView):
    def get(self, request, *args, **kwargs):
        return Response({
                    "status": HTTP_200_OK,
                    "message": "Success"
                },HTTP_200_OK)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HealthCheck.as_view(), name='HealthCheck'),
    path('new-api/', NewApi.as_view(), name='NewApi')
]
