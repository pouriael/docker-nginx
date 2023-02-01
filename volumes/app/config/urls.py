
from django.contrib import admin
from django.urls import path,include
from web.views import home
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',home),
    path('admin/', admin.site.urls),

] 

urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)