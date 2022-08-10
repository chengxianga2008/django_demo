from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from .models import Post
from user.models import Author

# Create your views here.


class PostListView(ListView):
    model = Post
    template_name = 'blog/list.html'
    ordering = ['-created_at']
    paginate_by = 5


class PostUserListView(ListView):
    model = Post
    template_name = 'blog/post_user_list.html'
    ordering = ['-created_at']
    paginate_by = 5

    def get_queryset(self):
        self.author = get_object_or_404(
            Author, Q(id__exact=self.kwargs['author_id']))
        queryset = Post.objects.filter(author=self.author)
        ordering = self.get_ordering()
        if ordering:
            if isinstance(ordering, str):
                ordering = (ordering,)
            queryset = queryset.order_by(*ordering)
        return queryset

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['author'] = self.author
        return context


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
