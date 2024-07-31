from django.urls import path

from recipes.views import home

urlpatterns = [
    path('', home),  # Home
    path('recipe/test1/<str:id>/', home),   # Any type /123/any/...
    path('recipe/test2/<int:id>/', home),   # Only accepts numbers .../123/...
    path('recipe/test3/<slug:id>/', home),  # Join letters with a dash (.../building-your-1st-django-site/...)
    path('recipe/test3/<uuid:id>/', home)   # Using hash: UsHash075194d3-6885-417e-a8a8-6c931e272f00
]
