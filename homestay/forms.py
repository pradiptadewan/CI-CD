from django import forms
from .models import Booking

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Nama Anda'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email Anda'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Pesan Anda'}))

    def save(self):
        pass


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['room', 'customer_name', 'email', 'check_in_date', 'check_out_date', 'guests']
        widgets = {
            'check_in_date': forms.DateInput(attrs={'type': 'date'}),
            'check_out_date': forms.DateInput(attrs={'type': 'date'}),
        }
