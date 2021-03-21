from django import forms
from student_app.models import Student
from admin_app.models import Order, Product
from tempus_dominus.widgets import DatePicker


class AdminStudentDnursForm(forms.ModelForm):
    tanggal_lahir = forms.DateField(widget=DatePicker())

    class Meta:
        model = Student
        exclude = ['user']


class AdminOrderDnursForm(forms.ModelForm):
    tanggal_transaksi = forms.DateField(widget=DatePicker())
    tanggal_expired = forms.DateField(widget=DatePicker())

    def __init__(self, *args, **kwargs):
        super(AdminOrderDnursForm, self).__init__(*args, **kwargs)
        self.fields['student'].queryset = Student.objects.filter(
            afiliasi='Dnurs')
        self.fields['product'].queryset = Product.objects.filter(
            nama_produk__startswith='dn')

    class Meta:
        model = Order
        fields = [
            'student', 'coach', 'product', 'diskon',
            'tanggal_transaksi', 'tanggal_expired',
            ]
