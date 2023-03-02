from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm

# Create your views here.


class PostByCommunity(ListView):
    template_name = "core/post_detail.html"
    model = Post
    context_object_name = "posts"

    def get_queryset(self):
        # el codigo que yo queira
        area = self.kwargs['shorname']
        lista = Post.objects.filter(
            community__slug=area
        )
        return lista


class PostCreateView(CreateView):
    template_name = "post/create_post.html"
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('community:index')

    def form_valid(self, form):
        print(self.request.user)
        #logica del proceso
        comunidad = form.save(commit=False)
        # empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        comunidad.slug = comunidad.title.replace(" ", "-")
        comunidad.user = self.request.user
        comunidad.save()
        return super(PostCreateView, self).form_valid(form)
