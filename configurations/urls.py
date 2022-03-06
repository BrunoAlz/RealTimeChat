from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Toda vez que formos para a RAIZ do SITE Chamaremos o CORE.URLS
    path('', include('core.urls')), 
    path('accounts/', include('accounts.urls')), 
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
