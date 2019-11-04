"""middlerware para actualizar"""

from django.shortcuts import redirect
from django.urls import reverse

class perfilCompletoMiddleware:

    """perfil"""

    def __init__(self,get_response):
        self.get_reponse = get_response

    def __call__(self, request):
        if not request.user.is_anonymous:
            perfil = request.user.perfil
            print(request.user)
            if perfil.tipo_usuario=='':
                if request.path not in [reverse('signup1'),reverse('logout')]:
                    return redirect('signup1')
            else:
                if perfil.tipo_usuario.upper()=='ALUMNO':
                    
                    if perfil.numero=='' :
                        if request.path not in [reverse('signup2'), reverse('logout')]:
                            return redirect('signup2')
                if perfil.tipo_usuario.upper() == 'PROFESOR':
                    
                    if perfil.numero=='' :
                        if request.path not in [reverse('signup2'), reverse('logout')]:
                            return redirect('signup2')
        response = self.get_reponse(request)
        return response



