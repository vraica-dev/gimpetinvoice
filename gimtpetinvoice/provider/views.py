from django.shortcuts import render
from django.views import View
from provider.forms import ProviderForm
import copy

class ProviderView(View):
    form_class = ProviderForm
    templte_name = 'provider_template.html'
    
    def get(self, request):
        form = self.form_class()
        return render(request, self.templte_name, {"form": form})
    
    def post(self, request):
        data = copy.deepcopy(self.request.POST)
        data['user'] = self.request.user

        form = self.form_class(data)
        print(data)
        if form.is_valid():
            form.save()
            form = self.form_class()
        return render(request, self.templte_name, {"form": form})