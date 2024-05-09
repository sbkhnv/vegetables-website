from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

scheme_view = get_schema_view(
    openapi.Info(
        title="Music",
        description="created by subkhanov",
        default_version="v1",
        terms_of_service="https://t.me/subkhanov77",
        contact=openapi.Contact(email='subkhanov77@gmail.com'),
        license=openapi.License(name='test web')
    ),
    public=True,
    permission_classes=(permissions.AllowAny, )
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("user/",include("users.urls")),
    path("",include("shop.urls")),
    path('api/v1/',include("music.urls")),
    path('api-auth/',include('rest_framework.urls')),
    path('docs/',scheme_view.with_ui("swagger",cache_timeout=0),name='swagger'),
    path('docs-redoc/',scheme_view.with_ui("redoc",cache_timeout=0),name='redoc'),
]

urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
