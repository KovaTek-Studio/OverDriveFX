from django.shortcuts import render,redirect
from django.http import HttpResponseBadRequest
from django.core.files.storage import FileSystemStorage
from datetime import datetime
from main.utils.dbconnect import connect_db
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
def testimonial_create(request):
    coleccion_testimonial = connect_db("testimonial")

    if request.method == 'POST':
        # 1) Recogemos datos (o valores por defecto)
        nombre= request.POST.get('nombre', '').strip()
        email= request.POST.get('email', '').strip()
        texto= request.POST.get('texto', '').strip()
        rating= request.POST.get('rating', '').strip()
        fecha= request.POST.get('fecha')  # opcional, o usa datetime.utcnow()

        # 2) Validación rápida
        if not all([nombre, email, texto, rating]):
            return HttpResponseBadRequest("Nombre, email, texto y rating son obligatorios.")

        # 3) Manejo de imágenes (si aplica)
        imagenes_urls = []
        for fichero in request.FILES.getlist('imagenes'):
            # Genera ruta única: media/testimonials/YYYYMMDD_hhmmss_nombre.ext
            timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
            filename  = f"testimonials/{timestamp}_{fichero.name}"
            # Guarda en MEDIA_ROOT y recoge la URL
            path = default_storage.save(filename, ContentFile(fichero.read()))
            imagenes_urls.append(default_storage.url(path))

        # 4) Construimos el doc y lo insertamos
        doc = {
            "nombre":nombre,
            "email":email,
            "texto":texto,
            "rating":int(rating),
            "fecha":datetime.utcnow() if not fecha else datetime.fromisoformat(fecha),
            "imagenes": imagenes_urls,
            "aprobado":False,
        }
        result = coleccion_testimonial.insert_one(doc)

        # 5) Redirige o devuelve JSON
        return redirect('testimonial-create')  # o JsonResponse(..., status=201)

    # GET: pinta el formulario vacío
    return render(request, 'testimonial-create.html')