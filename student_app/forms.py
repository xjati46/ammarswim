from django import forms
from admin_app.models import Order


class StudentOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'p1_a', 'p2_a', 'p3_a', 'p4_a', 'p5_a', 'p6_a', 'p7_a', 'p8_a'
            ]
