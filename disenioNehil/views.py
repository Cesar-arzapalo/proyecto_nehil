"""proyecto nehil"""
#django
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
#date
from datetime import datetime
#json
import json

@login_required()
def hola_mundo(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('la hora es {}'.format(str(now)))

def hola(request):
    numero = [int(i) for i in request.GET['numero'].split(',')]

    data={
        'angel':'ok'
    }
    return HttpResponse(json.dumps(data),content_type='application/json')

