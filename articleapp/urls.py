from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.homepage_f, name='homepage_f'),
    path('login',views.login_f, name='login_f'),
    path('signup',views.signup_f, name='signup_f'),
    path('articles',views.articles_f, name='articles_f'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)