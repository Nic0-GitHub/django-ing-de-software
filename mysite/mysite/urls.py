from django.views.generic import RedirectView
from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('', RedirectView.as_view(url='polls/', permanent=True)),
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]