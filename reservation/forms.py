from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        exclude = ['customer','room']
        widgets = {
            'check_in_date': forms.DateInput(attrs={'format': 'yyyy-mm-dd', 'type': 'date', 'class': 'form-control'}),
            'check_out_date': forms.DateInput(attrs={'format': 'yyyy-mm-dd', 'type': 'date', 'class': 'form-control'}),
        }

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

        for name,field in self.fields.items():
            if name in ('number_of_guests','room'):
                field.widget.attrs.update({'class':'form-control', 'placeholder':'Choose...'})

