# main/views/testimonial/testimonial_edit.py
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from bson import ObjectId
from datetime import datetime
from main.utils.dbconnect import connect_db

@require_http_methods(["GET", "POST"])
def testimonial_edit(request, pk):
    colec = connect_db("testimonial")
    doc = colec.find_one({"_id": ObjectId(pk)})
    if not doc:
        return redirect("main:testimonial_admin")  # o mostrar 404

    # Prepara datos para el formulario
    doc["id"]    = str(doc["_id"])
    doc["fecha"] = doc["fecha"].isoformat()
    doc.setdefault("imagenes", [])  # Si no tiene, inicializa lista

    if request.method == "POST":
        # Lee datos, usando valor actual si no viene
        nombre  = request.POST.get("nombre",  doc.get("nombre"))
        email   = request.POST.get("email",   doc.get("email"))
        texto   = request.POST.get("texto",   doc.get("texto"))
        rating  = int(request.POST.get("rating", doc.get("rating")))
        aprobado = request.POST.get("aprobado") == "on"

        
        # Empieza con las imágenes actuales
        imagenes = list(doc["imagenes"])

        # Procesa nuevas imágenes y las añade
        for fichero in request.FILES.getlist("imagenes"):
            timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
            filename  = f"testimonials/{timestamp}_{fichero.name}"
            path      = default_storage.save(filename, ContentFile(fichero.read()))
            imagenes.append(default_storage.url(path))

        colec.update_one(
            {"_id": ObjectId(pk)},
            {"$set": {
                "nombre":   nombre,
                "email":    email,
                "texto":    texto,
                "rating":   rating,
                "aprobado": aprobado,
                "fecha":    datetime.fromisoformat(request.POST.get("fecha", doc["fecha"])),
                "imagenes": imagenes
            }}
        )
        return redirect('testimonial-admin')

    return render(request, "testimonial-edit.html", {"testimonial": doc})