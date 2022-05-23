# from django.shortcuts import render
# from inventarioslist_app.models import Comercial
# from django.http import JsonResponse
# # Create your views here.


# def comercial_list(request):
#     comerciales = Comercial.objects.all()
#     data = {
#         'comerciales': list(comerciales.values())
#     }
#     return JsonResponse(data)

# def comercial_detalle (request, pk):
#     comercial = Comercial.objects.get(pk=pk)
#     data = {
#         'nombre': comercial.nombre,
#         'apellido': comercial.apellido,
#         'telefono': comercial.telefono,
#         'email': comercial.email,
#         'estado': comercial.estado,
#     }
#     return JsonResponse(data)



