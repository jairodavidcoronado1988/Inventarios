from rest_framework import serializers
from inventarioslist_app.models import Comercial, Empresa, Ot, Producto, Actualizacion, Ciudad

#Serializer Productos
class ProductonomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['nombre']

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = "__all__"

#Serializer Empresas
class EmpresanomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = ['nombre']

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        #fields = "__all__"
        exclude = ['productos','comercial']
        
class EmpresaComProdSerializer(serializers.ModelSerializer):
    comercial= serializers.StringRelatedField(source='comercial.nombre')
    productos = ProductoSerializer(many=True, read_only=True)
    class Meta:
        model = Empresa
        #fields = "__all__"
        exclude = ['nit']

class CrearEmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = "__all__"

class EmpresaComercialSerializer(serializers.ModelSerializer):
    comercial= serializers.StringRelatedField(source='comercial.nombre')
    class Meta:
        model = Empresa
        #fields = "__all__"
        exclude = ['productos']

#Serializer Comercial
class ComercialSerializer(serializers.ModelSerializer):
    empresaslist = EmpresaSerializer(many=True, read_only=True)
    class Meta:
        model = Comercial
        fields = "__all__"

#Serializer Actualizaciones
class ActSerializer(serializers.ModelSerializer):
    producto = ProductonomSerializer(many=True, read_only=True)
    empresa = EmpresanomSerializer(read_only=True)
    class Meta:
        model = Actualizacion
        fields = "__all__"
        
class CrearActSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actualizacion
        fields = "__all__"

#Serializer OT
class OtSerializer(serializers.ModelSerializer):
    empresas = EmpresanomSerializer(read_only=True)
    class Meta:
        model = Ot
        fields = "__all__"

class CrearOtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ot
        fields = "__all__"

#Serializer Ciudades
class CiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = "__all__"





