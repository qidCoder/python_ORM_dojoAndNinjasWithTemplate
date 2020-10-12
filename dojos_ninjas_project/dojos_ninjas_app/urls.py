from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('process_add', views.process_add),
    path('delete/<int:dojo_id>', views.delete)
]