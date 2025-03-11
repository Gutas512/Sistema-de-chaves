from django.contrib import admin
from django.urls import path
from website import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.index, name='index'),

    path('funcionarios/', views.funcionario_list, name='funcionario_list'),
    path('funcionario/<int:id_funcionario>/', views.funcionario_detail, name='funcionario_detail'),
    path('funcionario/edit/<int:id_funcionario>/', views.funcionario_edit, name='funcionario_edit'),
    path('funcionario/delete/<int:id_funcionario>/', views.funcionario_delete, name='funcionario_delete'),
    path('funcionario/create/', views.funcionario_create, name='funcionario_create'),

    path('salas/', views.sala_list, name='sala_list'),

    path('registros/', views.registro_list, name='registro_list'),

]
