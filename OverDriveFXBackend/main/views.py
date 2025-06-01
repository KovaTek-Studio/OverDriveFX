# from django.shortcuts import render,redirect, HttpResponse
# from django.http import JsonResponse, HttpResponseBadRequest
# from django.core.files.storage import FileSystemStorage
# from bson import ObjectId
# from datetime import datetime
# from .utils.dbconnect import connect_db
# # Create your views here.
# def home(request):
#     return HttpResponse("<h1>Welcome Home OverDriveFX</h1><br>Can you center this div? xd")

# def testimonial_list(request):
#     coleccion_testimonial = connect_db("testimonial")
#     cursor = coleccion_testimonial.find()

#     testimonials = []
#     for doc in cursor:
#         # convierte el ObjectId a string
#         doc['_id'] = str(doc['_id'])
#         # formatea la fecha a ISO (si viene como datetime)
#         if isinstance(doc.get('fecha'), datetime):
#             doc['fecha'] = doc['fecha'].isoformat()
#         testimonials.append(doc)
#     # safe=False permite serializar listas
#     return JsonResponse(testimonials, safe=False)

# def testimonial_create(request):
#     coleccion_testimonial = connect_db("testimonial")

#     if request.method == 'POST':
#         # 1) Recogemos datos (o valores por defecto)
#         nombre= request.POST.get('nombre', '').strip()
#         email= request.POST.get('email', '').strip()
#         texto= request.POST.get('texto', '').strip()
#         rating= request.POST.get('rating', '').strip()
#         fecha= request.POST.get('fecha')  # opcional, o usa datetime.utcnow()

#         # 2) Validación rápida
#         if not all([nombre, email, texto, rating]):
#             return HttpResponseBadRequest("Nombre, email, texto y rating son obligatorios.")

#         # 3) Manejo de imágenes (si aplica)
#         """ imagenes = []
#         nuevas   = request.FILES.getlist('imagenes')
#         if nuevas:
#             fs = FileSystemStorage()
#             for f in nuevas:
#                 filename = fs.save(f.name, f)
#                 imagenes.append(fs.url(filename)) """

#         # 4) Construimos el doc y lo insertamos
#         doc = {
#             "nombre":nombre,
#             "email":email,
#             "texto":texto,
#             "rating":int(rating),
#             "fecha":datetime.utcnow() if not fecha else datetime.fromisoformat(fecha),
#           #  "imagenes":  imagenes,
#             "aprobado":False,
#         }
#         result = coleccion_testimonial.insert_one(doc)

#         # 5) Redirige o devuelve JSON
#         return redirect('testimonial-create')  # o JsonResponse(..., status=201)

#     # GET: pinta el formulario vacío
#     return render(request, 'testimonial-create.html')