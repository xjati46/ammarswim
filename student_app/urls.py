from django.urls import path
from . import views

app_name = 'student-app'

urlpatterns = [
    path('', views.StudentIndexView.as_view(), name='student-index'),
    path(
        'profile/',
        views.StudentProfileView.as_view(),
        name='student-profile'),
    path(
        'order/',
        views.StudentOrderListView.as_view(),
        name='student-order-list'),
    path(
        'order/<int:pk>/',
        views.StudentOrderDetailView.as_view(),
        name='student-order-detail'),
    path(
        'order/update/<int:pk>/',
        views.StudentOrderUpdateView.as_view(),
        name='student-order-update'),
    path(
        'rapor/',
        views.RaporListView.as_view(),
        name='rapor-list'),
    path(
        'arsip/',
        views.StudentArsipListView.as_view(),
        name='student-arsip-list'),
]
