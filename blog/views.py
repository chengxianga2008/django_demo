from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from .models import Post

# Create your views here.


class PostListView(ListView):
    model = Post
    template_name = 'blog/list.html'
    # paginate_by = 10  # if pagination is desired


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    pk_url_kwarg = 'post_id'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name_suffix = '_create_form'
    fields = ['title', 'description', ]

    def form_valid(self, form):
        form.instance.is_published = True
        form.instance.author = self.request.user.author
        form.instance.created_at = datetime.now()
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name_suffix = '_update_form'
    fields = ['title', 'description', 'is_published', ]
    pk_url_kwarg = 'post_id'

    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user.author == post.author


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    pk_url_kwarg = 'post_id'
    success_url = reverse_lazy('post_list')

    def test_func(self):
        post = self.get_object()
        return self.request.user.author == post.author
