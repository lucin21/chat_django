from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Comment
from .forms import CommentForm
from django.urls import reverse_lazy
import datetime

# Create your views here.


class CommentsByPost(ListView):
    template_name = "core/comments.html"
    model = Comment
    context_object_name = "comments"

    def get_queryset(self):
        # el codigo que yo queira
        area = self.kwargs['shorname']
        lista = Comment.objects.filter(
            post__slug=area
        ).order_by('-created_at')
        print(lista)
        return lista

class CommentCreateView(CreateView):
    template_name = "comment/create_comment.html"
    model = Comment
    form_class = CommentForm
    success_url = reverse_lazy('community:index')

    def form_valid(self, form):
        print(self.request.user)
        #logica del proceso
        comunidad = form.save(commit=False)
        # empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        # comunidad.slug = comunidad.title.replace(" ", "-")
        comunidad.user = self.request.user
        comunidad.save()
        return super(CommentCreateView, self).form_valid(form)

