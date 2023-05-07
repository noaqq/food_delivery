from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path("", views.start, name="start"),
    path("menu", views.menu, name="menu"),
    path("faq", views.faq, name="faq"),
    path("order", views.basket, name="order"),
    path("payment", views.payment, name="payment"),
    path("delivery", views.delivery, name="delivery"),
    path("menu/<str:category>", views.menu_category, name="menu_category"),
    path("create", views.create, name="create"),
    path("update", views.update, name="update"),
    path("delete", views.delete, name="delete"),
    path("clear_basket", views.clear_basket, name="clear_basket"),
    path("sort_food", views.sort_food, name="sort_food"),
    path("login", views.login_user, name="login_user"),
    path("regist", views.regist, name="regist"),
    path("logout", views.logout_user, name="logout"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
