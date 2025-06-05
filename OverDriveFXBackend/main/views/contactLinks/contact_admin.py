from django.shortcuts import render
import json
from main.views.contactLinks.contact_list import contact_list

def contact_admin(request):
    response = contact_list(request)
    
    payload = json.loads(response.content)
    data = payload.get("data", [])

    for item in data:
        item['id'] = item.pop('_id')

    return render(request, "contact-admin.html", {"contacts": data})