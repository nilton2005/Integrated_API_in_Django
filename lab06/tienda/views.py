from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializer import ProductoSerializer, CategoriaSerializer
from django.shortcuts import get_object_or_404, render
from .models import Categoria, Producto

# Create your views here.
#add product wit bucle for, create a directory fron save data of the products

def index(request):
    productos = Producto.objects.order_by('nombre')[:10]
    categorias = Categoria.objects.all()
    context = {'productos': productos, 'categorias': categorias}
    for producto in productos:
        print(producto.image)
    return render(request, 'index.html', context)
    
def producto(request, id):
    categorias = Categoria.objects.all()
    producto = get_object_or_404(Producto, pk=id)
    context = {
        'producto': producto,
        'categorias': categorias
    }
    return render(request, 'producto.html', context)

def categoria(request, id):
    productos = Producto.objects.filter(categoria_id = id) 
    categorias = Categoria.objects.all()
    for producto in productos:
        print(producto.nombre)
    context = {
        'productos' : productos, 'categoria': categorias
    }
    return render(request, 'categories.html', context)

# creating view for to consume api rest full
class IndexApi(APIView):
    def get(self, request):
        context = {
            'message': 'servidor activo'
        }
        return Response(context)
# for products
class ProductosApi(ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProductoDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    lookup_field = 'id' # esto deve ser la misma variable que se pasa en la url

# for categories

class CategoriasApi(ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    lookup_field = 'id'

 
