from wsgiref import validate
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django import forms
from django.utils.translation import gettext_lazy as _
from . import models



class SignInForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(SignInForm, self).__init__(*args, **kwargs)
        keys = self.fields.keys()
        for key in keys:
            if key == 'password':
                self.fields[key].widget = forms.PasswordInput(attrs={'placeholder': key, 'class': 'form-control'})      
            else:
                self.fields[key].widget.attrs.update({'class': 'form-control', 'placeholder': key})
       
    # password = forms.CharField(max_length=16, widget=forms.PasswordInput, validators=[validate_password])

    """Form definition for Account."""

    class Meta:
        """Meta definition for Accountform."""

        model = models.Account
        fields = ('username', 'password')

# .attrs.update({'class': 'form-control', 
#                 'placeholder': key, 'validators': [validate_password]})
class SignUpForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        
        self.fields['user_type'].widget.attrs.update({'style': 'width: 100%', 'class': 'form-control'})
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'username'})
    
    comfirm_password = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Comfirm password'}))
    password = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'password'}), validators=[validate_password])

    """Form definition for SignUp."""

    class Meta:
        """Meta definition for SignUpform."""

        model = models.Account
        fields = ('username', 'user_type', 'password', 'comfirm_password')
        


    def clean_comfirm_password(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('comfirm_password')
        print(password2, password1)

        if password1 != password2:
            raise ValidationError( _('Password mismatch !') )
        
        return password2
    
    
class ProfileForm(forms.ModelForm):
    """Form definition for Profile."""
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        user = kwargs.get('instance', None)
        
        if user != None and  user.user_type != 'ADMIN':
            self.fields.pop('user_type')
       

        for key in self.fields.keys():
            if key == 'birth_date':
                self.fields[key].widget = forms.DateInput(attrs={'type': 'date'})
            if key == 'username':
                self.fields[key].widget.attrs.update({'readonly': True,})
                
            
            self.fields[key].widget.attrs.update({'class': 'form-control'})


    class Meta:
        """Meta definition for Profileform."""

        model = models.Account
        exclude = ('date_joined', 'is_staff', 'is_superuser', 'is_active', 'password'
        )
