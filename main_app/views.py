from django.views.generic import TemplateView, CreateView
from main_app.forms import UserCreateForm, CoachProfileForm, StudentProfileForm
from coach_app.models import Coach
from student_app.models import Student
from django.urls import reverse_lazy
from admin_app.models import Order
from main_app.filters import OrderFilter
from django.shortcuts import render


# Create your views here.


class IndexView(TemplateView):
    template_name = 'main_app/index.html'


class RegistrationView(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('index')
    template_name = 'registration/registration.html'


class DeniedAccessView(TemplateView):
    template_name = 'main_app/403.html'


class CoachProfileCreateView(CreateView):
    template_name = 'main_app/coach_profile_create.html'
    model = Coach
    form_class = CoachProfileForm
    success_url = '/main/'


class StudentProfileCreateView(CreateView):
    template_name = 'main_app/student_profile_create.html'
    model = Student
    form_class = StudentProfileForm
    success_url = '/main/'


class TestTemplateView(TemplateView):
    template_name = 'main_app/test.html'

    def get_context_data(self, **kwargs):
        context = super(TestTemplateView, self).get_context_data(**kwargs)
        # p = Books.objects.values(
        #     'author'
        #     ).order_by(
        #     'author'
        #     ).annotate(
        #     total_price=Sum('price'))
        p = 'test boss...'
        context = {
            'p': p,
        }
        return context


def search(request):
    order_list = Order.objects.all()
    order_filter = OrderFilter(request.GET, queryset=order_list)
    return render(
        request, 'main_app/order_filter.html', {'filter': order_filter}
        )
