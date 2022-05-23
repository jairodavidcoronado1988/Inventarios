from django.urls import path
from inventarioslist_app.api.views import ProductoDetalleAV,CiudadAV, ComercialListAV, ComercialDetalleAV, EmpresaAV, EmpresaDetalleAV, OtAV, ProductoAV, ActualizacionAV, EmpresaComercial

urlpatterns = [
    
    path('productos/list/', ProductoAV.as_view(), name='producto-list'),
    path('producto/<str:id_producto>', ProductoDetalleAV.as_view(), name='producto-detail'),
    
    path('empresas/list/', EmpresaAV.as_view(), name='empresa-list'),
    path('empresas/<str:nit>', EmpresaDetalleAV.as_view(), name='empresa-detail'),            
    path('empresascomercial/', EmpresaComercial.as_view(), name='empresa-comercial-detail'),
                
    path('comerciales/list/', ComercialListAV.as_view(), name='comercial-list'), 
    path('comercial/<int:pk>', ComercialDetalleAV.as_view(), name='comercial-detail'),
    
    path('actualizacion/list/', ActualizacionAV.as_view(), name='actualizacion-list'), 
    
    path('ot/list/', OtAV.as_view(), name='ot-list'),
    
    path('ciudades/list/', CiudadAV.as_view(), name='ciudad-list'), 
    
    
]