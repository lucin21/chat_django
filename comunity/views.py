from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from comunity.models import Community
from .forms import CommunityForm

# Create your views here.


class CommunityList(ListView):
    model = Community
    template_name = 'core/index.html'
    context_object_name = 'community_list'


class CommunityDetail(DetailView):
    model = Community
    template_name = 'core/community_detail.html'
    context_object_name = 'community'


class CommunityCreateView(CreateView):
    template_name = "community/create_community.html"
    model = Community
    form_class = CommunityForm
    success_url = reverse_lazy('community:index')

    def form_valid(self, form):
        print(self.request.user)
        #logica del proceso
        comunidad = form.save(commit=False)
        # empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        comunidad.slug = comunidad.name.replace(" ", "-")
        comunidad.user = self.request.user
        comunidad.save()
        return super(CommunityCreateView, self).form_valid(form)
