from django.http import JsonResponse
from datetime import datetime
from main.utils.dbconnect import connect_db

def contact_list(request):
    try:
        colec = connect_db('contact')
        data = []
        for d in colec.find():
            d['_id'] = str(d['_id'])
            #d['fecha'] = d['fecha'].isoformat() if isinstance(d.get('fecha'), datetime) else d.get('fecha')
            data.append(d)
        return JsonResponse(
            {
                "status": "success",
                "data": data
             },
            status=200
        )
    except Exception:
        return JsonResponse(
            {
                "status": "error",
                "error": {"code": "SERVER_ERROR", "message": "Error interno."}
            },
            status=500
        )