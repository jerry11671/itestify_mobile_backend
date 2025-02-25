from django.contrib import admin
from django.urls import path, include
from common.views import HealthCheckAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls')),
    path('', HealthCheckAPIView.as_view()),
]

