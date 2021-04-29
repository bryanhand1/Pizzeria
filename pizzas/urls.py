from django.urls import path
from django.conf import settings # new
from django.urls import path, include # new
from django.conf.urls.static import static # new

from . import views

app_name = 'pizzas'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('pizzas', views.pizzas, name='pizzas'),
    path('pizzas/<int:pizza_id>/', views.pizza, name='pizza'),
    path('new_comment/<int:pizza_id>/', views.new_comment, name = 'new_comment'),


]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)