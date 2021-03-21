from django.views.generic import (
                                TemplateView,
                                ListView,
                                DetailView,
                                UpdateView,
                                )
from student_app.models import Rapor
from admin_app.models import Order
from main_app.models import Newsfeed
from student_app.forms import StudentOrderForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect

# Create your views here.


class StudentIndexView(PermissionRequiredMixin, TemplateView):
    permission_required = (
                            'student_app.view_rapor',
                            'student_app.view_student'
                            )
    template_name = 'student_app/index.html'

    def handle_no_permission(self):
        return redirect('denied-access')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_list'] = Newsfeed.objects.all()
        return context


class StudentProfileView(PermissionRequiredMixin, TemplateView):
    permission_required = (
                            'student_app.view_rapor',
                            'student_app.view_student'
                            )
    template_name = 'student_app/profile.html'

    def handle_no_permission(self):
        return redirect('denied-access')


class StudentOrderListView(PermissionRequiredMixin, ListView):
    permission_required = (
                            'student_app.view_rapor',
                            'student_app.view_student'
                            )
    context_object_name = 'student_order_list'
    template_name = 'student_app/order_list.html'

    def get_queryset(self):
        return Order.objects.filter(
            student=self.request.user.student.id
            ).filter(
            arsip='False')

    def handle_no_permission(self):
        return redirect('denied-access')


class StudentOrderDetailView(PermissionRequiredMixin, DetailView):
    permission_required = (
                            'student_app.view_rapor',
                            'student_app.view_student'
                            )
    model = Order
    template_name = 'student_app/order_detail.html'

    def handle_no_permission(self):
        return redirect('denied-access')


class StudentOrderUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = (
                            'student_app.view_rapor',
                            'student_app.view_student'
                            )
    template_name = 'student_app/order_form.html'
    model = Order
    form_class = StudentOrderForm
    success_url = '/student/order/'

    def handle_no_permission(self):
        return redirect('denied-access')


class RaporListView(PermissionRequiredMixin, ListView):
    permission_required = (
                            'student_app.view_rapor',
                            'student_app.view_student'
                            )
    template_name = 'student_app/rapor_list.html'
    context_object_name = 'rapor_list'

    def get_queryset(self):
        return Rapor.objects.filter(
            order__student=self.request.user.student.id
            )

    def handle_no_permission(self):
        return redirect('denied-access')


class StudentArsipListView(PermissionRequiredMixin, ListView):
    permission_required = (
                            'student_app.view_rapor',
                            'student_app.view_student'
                            )
    context_object_name = 'student_arsip_list'
    template_name = 'student_app/arsip_list.html'

    def get_queryset(self):
        return Order.objects.filter(
            student=self.request.user.student.id
            ).filter(
            arsip='True')

    def handle_no_permission(self):
        return redirect('denied-access')
