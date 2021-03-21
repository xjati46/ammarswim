from django import forms
from admin_app.models import Order
from tempus_dominus.widgets import DatePicker
from student_app.models import Rapor


class CoachOrderForm(forms.ModelForm):
    p1 = forms.DateField(
        label='Pertemuan 1', required=False, widget=DatePicker())
    p2 = forms.DateField(
        label='Pertemuan 2', required=False, widget=DatePicker())
    p3 = forms.DateField(
        label='Pertemuan 3', required=False, widget=DatePicker())
    p4 = forms.DateField(
        label='Pertemuan 4', required=False, widget=DatePicker())
    p5 = forms.DateField(
        label='Pertemuan 5', required=False, widget=DatePicker())
    p6 = forms.DateField(
        label='Pertemuan 6', required=False, widget=DatePicker())
    p7 = forms.DateField(
        label='Pertemuan 7', required=False, widget=DatePicker())
    p8 = forms.DateField(
        label='Pertemuan 8', required=False, widget=DatePicker())

    class Meta:
        model = Order
        fields = ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8']


class RaporForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        coach_id = kwargs.pop('coach_id')
        super(RaporForm, self).__init__(*args, **kwargs)
        self.fields['order'].queryset = Order.objects.filter(
            coach=coach_id).filter(arsip='False')

    class Meta:
        model = Rapor
        fields = '__all__'
