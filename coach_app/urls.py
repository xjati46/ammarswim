from django.urls import path
from . import views

app_name = 'coach-app'

urlpatterns = [
    path('', views.CoachIndexView.as_view(), name='coach-index'),
    path('profile/', views.CoachProfileView.as_view(), name='coach-profile'),
    path(
        'order/',
        views.CoachOrderListView.as_view(),
        name='coach-order-list'),
    path(
        'order/<int:pk>/',
        views.CoachOrderDetailView.as_view(),
        name='coach-order-detail'),
    path(
        'order/update/<int:pk>',
        views.CoachOrderUpdateView.as_view(),
        name='coach-order-update'),
    path(
        'arsip/',
        views.CoachArsipListView.as_view(),
        name='coach-arsip-list'),
    path('rapor/', views.RaporListView.as_view(), name='rapor-list'),
    path('rapor/new/', views.RaporCreateView.as_view(), name='rapor-create'),
    path(
        'pencairan/',
        views.CoachPencairanListView.as_view(),
        name='pencairan-list'),
    path('order-kelas/', views.CoachOrderKelasListView.as_view(), name='coach-order-kelas-list'),
]
