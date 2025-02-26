from debug_toolbar.toolbar import debug_toolbar_urls

from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('members/', include('members.urls', namespace='members')),
    path('chats/', include('chats.urls', namespace='chats')),
    path('recommendations/', include('recommendations.urls', 
                                     namespace='recommendations')),
]

if settings.DEBUG:
    urlpatterns.extend(
        static(settings.MEDIA_URL,
               document_root=settings.MEDIA_ROOT))

if settings.DEBUG:
    urlpatterns.extend(
        debug_toolbar_urls())
