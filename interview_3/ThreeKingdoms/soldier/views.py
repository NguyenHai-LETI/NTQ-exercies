from django.shortcuts import render
from django.views.generic import ListView
from .models import Soldier

# Function-based view (FBV)
def soldier_view(request):
    soldiers = Soldier.objects.all()
    context = {
        'soldiers': soldiers,
        'method' : 'Function based view'
    }
    return render(request,'soldier_list.html',context)

class SoldierListView(ListView):
    model = Soldier
    template_name = 'soldier_list.html'
    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['soldiers'] = Soldier.objects.all()
        context['method'] = 'Class based view'

        return context