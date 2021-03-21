from django.views.generic import (
                                TemplateView,
                                ListView,
                                DetailView,
                                CreateView
                                )
from student_app.models import Student
from admin_app.models import Order
from main_app.models import Newsfeed
from admin_app.forms import AdminStudentDnursForm, AdminOrderDnursForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect

# Create your views here.


class AdminIndexView(PermissionRequiredMixin, TemplateView):
    permission_required = ('admin_app.view_order', 'admin_app.view_product')
    template_name = 'admin_app/index.html'

    def handle_no_permission(self):
        return redirect('denied-access')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_list'] = Newsfeed.objects.all()
        return context


class AdminProfileView(PermissionRequiredMixin, TemplateView):
    permission_required = ('admin_app.view_order', 'admin_app.view_product')
    template_name = 'admin_app/profile.html'

    def handle_no_permission(self):
        return redirect('denied-access')


class AdminStudentDnursListView(PermissionRequiredMixin, ListView):
    permission_required = ('admin_app.view_order', 'admin_app.view_product')
    context_object_name = 'student_dnurs_list'
    queryset = Student.objects.filter(afiliasi='Dnurs')
    template_name = 'admin_app/student_list.html'

    def handle_no_permission(self):
        return redirect('denied-access')


class AdminStudentDnursDetailView(PermissionRequiredMixin, DetailView):
    permission_required = ('admin_app.view_order', 'admin_app.view_product')
    model = Student
    template_name = 'admin_app/student_detail.html'

    def handle_no_permission(self):
        return redirect('denied-access')


class AdminStudentDnursCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ('admin_app.view_order', 'admin_app.view_product')
    template_name = 'admin_app/student_form.html'
    model = Student
    form_class = AdminStudentDnursForm
    success_url = '/adm/student/'

    def handle_no_permission(self):
        return redirect('denied-access')


class AdminOrderDnursListView(PermissionRequiredMixin, ListView):
    permission_required = ('admin_app.view_order', 'admin_app.view_product')
    context_object_name = 'order_dnurs_list'
    queryset = Order.objects.filter(
        product__nama_produk__startswith='dn').filter(
        arsip='False')
    template_name = 'admin_app/order_list.html'

    def handle_no_permission(self):
        return redirect('denied-access')


class AdminOrderDnursDetailView(PermissionRequiredMixin, DetailView):
    permission_required = ('admin_app.view_order', 'admin_app.view_product')
    model = Order
    template_name = 'admin_app/order_detail.html'

    def handle_no_permission(self):
        return redirect('denied-access')


class AdminOrderDnursCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ('admin_app.view_order', 'admin_app.view_product')
    template_name = 'admin_app/order_form.html'
    model = Order
    form_class = AdminOrderDnursForm
    success_url = '/adm/order/'

    def handle_no_permission(self):
        return redirect('denied-access')


class EarningDnursListView(PermissionRequiredMixin, ListView):
    permission_required = ('admin_app.view_order', 'admin_app.view_product')
    context_object_name = 'earning_dnurs_list'
    queryset = Order.objects.filter(
        product__nama_produk__startswith='dn').filter(
        arsip="False")
    template_name = 'admin_app/earning_list.html'

    def handle_no_permission(self):
        return redirect('denied-access')


class AdminArsipDnursListView(PermissionRequiredMixin, ListView):
    permission_required = ('admin_app.view_order', 'admin_app.view_product')
    context_object_name = 'arsip_dnurs_list'
    queryset = Order.objects.filter(
        product__nama_produk__startswith='dn').filter(
        arsip='True')
    template_name = 'admin_app/arsip_list.html'

    def handle_no_permission(self):
        return redirect('denied-access')


class AdminArsipDnursDetailView(PermissionRequiredMixin, DetailView):
    permission_required = ('admin_app.view_order', 'admin_app.view_product')
    model = Order
    template_name = 'admin_app/arsip_detail.html'

    def handle_no_permission(self):
        return redirect('denied-access')
