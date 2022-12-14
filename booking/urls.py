from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('find/', include('findpage.urls')),
    path('addcard/', include('addcard.urls')),
    path('user_profile/', include('user_profile.urls')),
    path('check_card/', include('checking.urls')),
    path('rent_room/', include('rent.urls'), name = 'rent'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)