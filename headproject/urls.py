from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("user/",include("users.urls")),
    path("",include("shop.urls")),
    path('api/v1/',include("music.urls")),
    path('auth/',views.obtain_auth_token),

]

urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
