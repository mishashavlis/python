from django.conf.urls.static import static
from recipe_site import settings
from django.contrib import admin
from django.urls import path, include
from post.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('captcha/', include('captcha.urls')),
    path('', include('post.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = pageNotFound