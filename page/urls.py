from django.urls import path
from .views import (
    about_us,
    contact_us,
    home,
    oylesine_view,
    vision_us,
    page_view
)


urlpatterns = [
    path("",home,name="home"),
    path("oylesine.html",oylesine_view),
    path("iletisim/",contact_us,name="contact_us"),
    path("vizyonumuz/",vision_us,name="vision_us"),
    path("hakkimizda/",about_us,name="about_us"),
    path("<slug:slug>/",page_view),
]