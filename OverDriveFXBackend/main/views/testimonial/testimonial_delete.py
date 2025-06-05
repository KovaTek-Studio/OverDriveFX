from django.shortcuts import redirect
from django.views.decorators.http import require_POST
from bson import ObjectId
from main.utils.dbconnect import connect_db

@require_POST
def testimonial_delete(request, pk):
    colec = connect_db("testimonial")
    colec.delete_one({"_id": ObjectId(pk)})
    return redirect('testimonial-admin')