from django.views import View
from django.template.response import TemplateResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django_sso.sso_gateway.models import Service, AuthenticationRequest

# Create your views here.


class login_web(View):

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):

        if not request.user.is_anonymous:

            return redirect(self.get_success_url())


        return super().dispatch(request, *args, **kwargs)
        

    def get_success_url(self):

        sso_request_token = self.request.GET.get('sso', '').strip()

        auth_request = None

        if sso_request_token:
            auth_request = AuthenticationRequest.objects.filter(
                token=sso_request_token,
                used = False
            ).first()

        
        if not auth_request or auth_request.next_url:

            return reverse_lazy('welcome')

        try:

            auth_request.activate(self.request.user)

        except Exception as e:

            return reverse_lazy('welcome') + '?fallback=true'


        return f'{auth_request.service.base_url}/sso/accept/'






    def get(self, request):

        template_name = 'base/pages/auth/login.html'

        return TemplateResponse(request, template_name)

        





