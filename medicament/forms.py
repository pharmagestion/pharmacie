from dataclasses import field
from django import forms
from .models import Medicament


class MedicamentForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(MedicamentForm, self).__init__(*args, **kwargs)
        

        for field in self.fields:

            if field == 'manu_date':
                self.fields[field].widget = forms.DateInput(attrs={'type': 'date'})
            
            if field == 'expr_date':
                self.fields[field].widget = forms.DateInput(attrs={'type': 'date'})

            if field == 'description':
                self.fields[field].widget = forms.Textarea(attrs={'type': 'textarea', 'rows': 8, 'col': 10})

            self.fields[field].widget.attrs.update({'class': 'form-control'})
    

    class Meta:
       model = Medicament
       fields = '__all__'
       exclude = ('create', )
    

    def clean_manu_date(self):
        pass
    
    def clean_expr_date(self):
        pass
    