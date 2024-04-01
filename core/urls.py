from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path

from .schema import swagger_urlpatterns

urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),
    re_path(r"^rosetta/", include("rosetta.urls")),
    path("api/v1/", include("apps.mfy.urls")),
    path("api/v1/", include("apps.users.urls")),
]
urlpatterns += i18n_patterns(path("admin/", admin.site.urls))

urlpatterns += swagger_urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
