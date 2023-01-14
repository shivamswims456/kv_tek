from django.urls import path, include
from authenticate import views
urlpatterns = [

    path('login', views.login_web.as_view(), name='web_login'),
    path('registered_user/', include('dj_rest_auth.urls')),
    path('register/', include('dj_rest_auth.registration.urls'))
]