from ast import Try
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Medicament
from .forms import MedicamentForm

# Create your views here.


class MedicamentView(LoginRequiredMixin, View):
    template_name = 'medicament/create.html'
    
    def get(self, request, *args, **kwargs):
        action = request.GET.get('action', False)
        pk = request.GET.get('pk', False)
        
        try:
            medicine = Medicament.objects.get(id=pk)
            if action == 'update':
                form = MedicamentForm(instance=medicine)
            
                ctx = {
                        'form' : form,
                        'med' : medicine
                    }
                
                return render(request, self.template_name, ctx)

            if action == 'delete':
                medicine.delete()
                return redirect('medicaments')
            
        except Medicament.DoesNotExist:
            if action == 'create':
                form = MedicamentForm()  
                ctx = {
                        'form' : form,
                        'med' : False
                    }
                return render(request, self.template_name, ctx)
            else:
                queryset = Medicament.objects.all()
                ctx = { 'queryset' : queryset }
                self.template_name = 'medicament/list.html'
                return render(request, self.template_name, ctx)

        
    

    def post(self, request, *args, **kwargs):
        pk = request.POST.get('pk', False)
        action = request.POST.get('action', False)
        
        try:
            medicine = Medicament.objects.get(id=pk)
            if action == 'delete':
                medicine.delete()
                return redirect('medicaments')
            else:
                form = MedicamentForm(request.POST, request.FILES, instance=medicine)
        except Medicament.DoesNotExist:
            form = MedicamentForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
        else:
            ctx = {
                'form' : form,
                'med': False
            }

            return render(request, self.template_name, ctx)
        
        return redirect('medicaments')
        
        
