from django.shortcuts import render
import json
from main.views.testimonial.testimonial_list import testimonial_list

def testimonial_admin(request):
    response = testimonial_list(request)
    
    payload = json.loads(response.content)
    data = payload.get("data", [])

    for item in data:
        item['id'] = item.pop('_id')

    return render(request, "testimonial-admin.html", {"testimonials": data})