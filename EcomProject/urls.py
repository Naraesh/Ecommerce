from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from .import settings
import EcomApp.urls
import accounts.urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('EcomApp.urls')),
    path('accounts/',include('accounts.urls'))
]


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
