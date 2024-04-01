from django import forms
from .models import MovieTicket

class MovieTicketForm(forms.ModelForm):
    class Meta:
        model = MovieTicket
        fields ='__all__'

        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'movie' : forms.TextInput(attrs={'class':'form-control'}),
            'multiplex' : forms.TextInput(attrs={'class':'form-control'}),
            'date' : forms.DateTimeInput(attrs={'type':'date','class':'form-control'}),
            'no_seat' : forms.NumberInput(attrs={'class':'form-control'}),
            'seat_type' : forms.Select(attrs={'class':'form-control'}),
            'mobile' : forms.NumberInput(attrs={'class':'form-control'})
        }