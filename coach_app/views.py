from django.views.generic import (
                                TemplateView,
                                ListView,
                                DetailView,
                                UpdateView,
                                CreateView,
                                )
from admin_app.models import Order
from coach_app.forms import CoachOrderForm, RaporForm
from student_app.models import Rapor
from coach_app.models import Coach
from main_app.models import Newsfeed
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect

# Create your views here.


class CoachIndexView(PermissionRequiredMixin, TemplateView):
    permission_required = 'coach_app.view_coach'
    template_name = 'coach_app/index.html'

    def handle_no_permission(self):
        return redirect('denied-access')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_list'] = Newsfeed.objects.all()
        return context


class CoachProfileView(PermissionRequiredMixin, TemplateView):
    permission_required = 'coach_app.view_coach'
    template_name = 'coach_app/profile.html'

    def handle_no_permission(self):
        return redirect('denied-access')


class CoachOrderListView(PermissionRequiredMixin, ListView):
    permission_required = 'coach_app.view_coach'
    context_object_name = 'coach_order_list'
    template_name = 'coach_app/order_list.html'

    def get_queryset(self):
        return Order.objects.filter(
            coach=self.request.user.coach.id
            ).filter(
            arsip='False'
            ).filter(
            jenis_order='p')

    def handle_no_permission(self):
        return redirect('denied-access')


class CoachOrderDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'coach_app.view_coach'
    model = Order
    template_name = 'coach_app/order_detail.html'

    def handle_no_permission(self):
        return redirect('denied-access')


class CoachOrderUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'coach_app.view_coach'
    template_name = 'coach_app/order_form.html'
    model = Order
    form_class = CoachOrderForm
    success_url = '/coach/order/'

    def handle_no_permission(self):
        return redirect('denied-access')


class CoachArsipListView(PermissionRequiredMixin, ListView):
    permission_required = 'coach_app.view_coach'
    context_object_name = 'coach_arsip_list'
    template_name = 'coach_app/arsip_list.html'

    def get_queryset(self):
        return Order.objects.filter(
            coach=self.request.user.coach.id
            ).filter(
            arsip='True')

    def handle_no_permission(self):
        return redirect('denied-access')


class RaporListView(PermissionRequiredMixin, ListView):
    permission_required = 'coach_app.view_coach'
    context_object_name = 'rapor_list'
    template_name = 'coach_app/rapor_list.html'

    def get_queryset(self):
        return Rapor.objects.filter(
            order__coach=self.request.user.coach.id
            )

    def handle_no_permission(self):
        return redirect('denied-access')


class RaporCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'coach_app.view_coach'
    template_name = 'coach_app/rapor_form.html'
    form_class = RaporForm
    success_url = '/coach/rapor/'

    def get_form_kwargs(self):
        kwargs = super(RaporCreateView, self).get_form_kwargs()
        kwargs.update({'coach_id': self.request.user.coach.id})
        return kwargs

    def handle_no_permission(self):
        return redirect('denied-access')


class CoachPencairanListView(PermissionRequiredMixin, ListView):
    permission_required = 'coach_app.view_coach'
    context_object_name = 'coach_pencairan_list'
    template_name = 'coach_app/pencairan_list.html'

    def get_queryset(self):
        return Order.objects.filter(
            coach=self.request.user.coach.id
            ).filter(
            arsip='False').filter(
            jenis_order='p')

    def handle_no_permission(self):
        return redirect('denied-access')

class CoachOrderKelasListView(PermissionRequiredMixin, ListView):
    permission_required = 'coach_app.view_coach'
    context_object_name = 'coach_order_kelas_list'
    template_name = 'coach_app/order_kelas_list.html'

    def get_queryset(self):
        return Order.objects.filter(
            coach=self.request.user.coach.id
            ).filter(
            arsip='False'
            ).filter(
            jenis_order='k')

    def handle_no_permission(self):
        return redirect('denied-access')