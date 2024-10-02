from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from . import views

app_name = 'tienda'

urlpatterns = [
    path('', views.index, name='index'),
    path('producto/<int:id>', views.producto, name='producto'),
    path('categoria/<int:id>', views.categoria, name='categoria')
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
