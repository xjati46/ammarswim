from django.urls import path
from . import views
from django.views.generic import RedirectView

app_name = 'admin-app'

urlpatterns = [
    path('', views.AdminIndexView.as_view(), name='admin-index'),
    path('profile/', views.AdminProfileView.as_view(), name='admin-profile'),
    path(
        'student/',
        views.AdminStudentDnursListView.as_view(),
        name='student-dnurs-list'),
    path(
        'student/<int:pk>/',
        views.AdminStudentDnursDetailView.as_view(),
        name='student-dnurs-detail'),
    path(
        'student/new/',
        views.AdminStudentDnursCreateView.as_view(),
        name='student-dnurs-create'),
    path(
        'order/',
        views.AdminOrderDnursListView.as_view(),
        name='order-dnurs-list'),
    path(
        'order/<int:pk>/',
        views.AdminOrderDnursDetailView.as_view(),
        name='order-dnurs-detail'),
    path(
        'order/new/',
        views.AdminOrderDnursCreateView.as_view(),
        name='order-dnurs-create'),
    path(
        'earning/',
        views.EarningDnursListView.as_view(),
        name='earning-dnurs-list'),
    path('arsip/', views.AdminArsipDnursListView.as_view(), name='arsip'),
    path(
        'arsip/<int:pk>/',
        views.AdminArsipDnursDetailView.as_view(),
        name='arsip-dnurs-detail'),
]
