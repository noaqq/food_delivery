from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path("", views.start, name="start"),
    path("menu", views.menu, name="menu"),
    path("faq", views.faq, name="faq"),
    path("delivery", views.delivery, name="delivery"),
    path("about", views.about, name="about"),
    path("login", views.login, name="login_user"),
    path("regist", views.regist, name = "regist"),
    path("logout", views.logout_user, name="logout"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)