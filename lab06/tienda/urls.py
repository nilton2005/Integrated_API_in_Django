from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from . import views

app_name = 'tienda'

urlpatterns = [
    path('', views.index, name='index'),
    path('producto/<int:id>', views.producto, name='producto'),
    path('categoria/<int:id>', views.categoria, name='categoria'),
    # Esta url es para consumir la api rest
    path('api/', views.IndexApi.as_view(), name='api'),
    # for product
    path('api/productos', views.ProductosApi.as_view(), name='api-productos'),
    path('api/producto/<int:id>', views.ProductoDetailView.as_view(), name='api-producto'),

    # for categories

    path('api/categorias', views.CategoriasApi.as_view(), name='api-categorias'),
    path('api/categoria/<int:id>', views.CategoriDetailView.as_view(), name="api-categoria"),

]
