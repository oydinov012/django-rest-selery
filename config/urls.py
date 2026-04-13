
from django.contrib import admin
from django.urls import path
from myapp.views import tets_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/',tets_view, name='test_view'),
]
