from django.views import View
from django.template.response import TemplateResponse
# Create your views here.


class login_web(View):

    def get(self, request):

        template_name = 'base/pages/auth/login.html'

        return TemplateResponse(request, template_name)

        





