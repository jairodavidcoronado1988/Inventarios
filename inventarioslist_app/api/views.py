from re import I
from django.http import JsonResponse
from inventarioslist_app.api.permissions import IsAdminOrReadOnly
from inventarioslist_app.api.serializers import ComercialSerializer, EmpresaSerializer, ProductoSerializer,ActSerializer, OtSerializer, CiudadSerializer,EmpresaComercialSerializer,CrearEmpresaSerializer,EmpresaComProdSerializer,CrearActSerializer,CrearOtSerializer
from inventarioslist_app.models import Comercial, Empresa, Ot, Producto, Actualizacion, Ciudad
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics

# Create your views here.

class ProductoAV(APIView):
    
    permission_classes = [IsAdminOrReadOnly]
    def get(self, request):
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class ProductoDetalleAV(APIView):
    permission_classes = [IsAdminOrReadOnly]
    def get(self, request,id_producto):
        try:
            producto =Producto.objects.get(id_producto=id_producto)
        except Producto.DoesNotExist:
            return Response({'Error': 'El producto buscado no existe'}, status = status.HTTP_400_BAD_REQUEST)
        serializer = ProductoSerializer(producto)
        return Response(serializer.data)
        
    def put (self, request,id_producto):
        try:
            producto =Producto.objects.get(id_producto=id_producto)
        except Producto.DoesNotExist:
            return Response({'Error': 'El producto buscado no existe'}, status = status.HTTP_400_BAD_REQUEST)
        serializer = ProductoSerializer(producto, data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request,id_producto):
        try:
            producto = Producto.objects.get(id_producto=id_producto)
            
        except Producto.DoesNotExist:
            return Response({'Error': 'El producto buscado no existe'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductoSerializer(producto)
        producto.estado = False
        producto.save()
        return  Response(serializer.data)
        
      
class EmpresaAV(APIView):
    permission_classes = [IsAdminOrReadOnly]
    def get(self, request):
        empresas = Empresa.objects.all()
        serializer = EmpresaSerializer(empresas, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CrearEmpresaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class EmpresaDetalleAV(APIView):
    permission_classes = [IsAdminOrReadOnly]
    def get(self, request, nit):
        try:
            empresa = Empresa.objects.get(nit=nit)          
        except Empresa.DoesNotExist:
            return Response({'Error':'La Empresa Buscada No Existe'}, status=status.HTTP_404_NOT_FOUND)
        serializer = EmpresaComProdSerializer(empresa)
        return Response(serializer.data)
    
    def put(self, request, nit):
        try:
            empresa = Empresa.objects.get(nit=nit)
        except Empresa.DoesNotExist:
            return Response({'Error':'La Empresa Buscada No Existe'}, status=status.HTTP_404_NOT_FOUND)
        serializer = EmpresaSerializer(empresa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request,nit):
        try:
            empresa = Empresa.objects.get(nit=nit)
        except Empresa.DoesNotExist:
            return Response({'Error': 'Empresa No Encontrada'}, status=status.HTTP_404_NOT_FOUND)
        empresa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class EmpresaComercial(generics.ListAPIView):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = EmpresaComercialSerializer
    def get_queryset(self):
        nombre = self.request.query_params.get('nombre',None)
        return Empresa.objects.filter(comercial__nombre=nombre)
        
        
class ComercialListAV(APIView):
    permission_classes = [IsAdminOrReadOnly]
    def get(self, request):
        comerciales = Comercial.objects.all()
        serializer = ComercialSerializer(comerciales, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ComercialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            #return Response({'Error':'El comercial ya existe'})
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class ComercialDetalleAV(APIView):
    permission_classes = [IsAdminOrReadOnly]
    def get(self, request,pk):
        try:
            comercial = Comercial.objects.get(pk=pk)
        except Comercial.DoesNotExist:
            return Response({'Error': 'Comercial No Encontrado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ComercialSerializer(comercial)
        return Response(serializer.data)
    
    def put(self, request,pk):
        try:
            comercial = Comercial.objects.get(pk=pk)
        except Comercial.DoesNotExist:
            return Response({'Error': 'Comercial No Encontrado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ComercialSerializer(comercial, data=request.data)         
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request,pk):
        
        try:
            comercial = Comercial.objects.get(pk=pk)
        except Comercial.DoesNotExist:
            return Response({'Error': 'Comercial No Encontrado'}, status=status.HTTP_404_NOT_FOUND)
        comercial.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ActualizacionAV(APIView):
    permission_classes = [IsAdminOrReadOnly]
    def get(self, request):
        productos = Actualizacion.objects.all()
        serializer = ActSerializer(productos, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CrearActSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

        
class OtAV(APIView):
    permission_classes = [IsAdminOrReadOnly]
    def get(self, request):
        ots = Ot.objects.all()
        serializer = OtSerializer(ots, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CrearOtSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

        
class CiudadAV(APIView):
    permission_classes = [IsAdminOrReadOnly]
    def get(self, request):
        ciudades = Ciudad.objects.all()
        serializer = CiudadSerializer(ciudades, many=True)
        return Response(serializer.data)
    
    def post(self, request): 
        serializer = CiudadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)