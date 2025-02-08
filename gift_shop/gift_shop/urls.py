
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/token/login/', obtain_auth_token, name='login'),
    path('api/v1/', include ('gift.urls')),
    path('api/v1/', include ('order.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
