from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from myapp.models import Patient

class PatientForm(forms.ModelForm):
    
    class Meta:
        model = Patient
        fields = ['name', 'phone', 'email', 'date', 'time', 'address']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'forms-control'}),
            'date': forms.DateInput(attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CreateUserForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class':'input100 has-val'}),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={'class':'input100 has-val'}),
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'input100 has-val'}),
            'email': forms.EmailInput(attrs={'class': 'input100 has-val'}),  
        }