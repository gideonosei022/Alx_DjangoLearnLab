

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from .models import Comment, Post
from .forms import CommentForm, PostForm

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Post, Tag
from .forms import PostForm
from django.db.models import Q

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log user in after register
            return redirect('post_list')  # or homepage
    else:
        form = UserRegisterForm()

    return render(request, 'blog/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        request.user.email = request.POST.get('email')
        request.user.save()
        return redirect('profile')

    return render(request, 'blog/profile.html')



# List all posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'  # templates/blog/post_list.html
    context_object_name = 'posts'
    ordering = ['-published_date']  # newest first

# View single post
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'  # templates/blog/post_detail.html
    context_object_name = 'post'

# Create new post



class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        # Set author before saving
        form.instance.author = self.request.user
        response = super().form_valid(form)

        # Handle tags
        tags_input = form.cleaned_data.get('tags')
        if tags_input:
            tag_names = [tag.strip() for tag in tags_input.split(',') if tag.strip()]

            for tag_name in tag_names:
                tag, created = Tag.objects.get_or_create(name=tag_name)
                self.object.tags.add(tag)

        return response


# Update existing post (author only)
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def get_initial(self):
        initial = super().get_initial()
        initial['tags'] = ', '.join(tag.name for tag in self.object.tags.all())
        return initial

    def form_valid(self, form):
        form.instance.author = self.request.user
        response = super().form_valid(form)

        self.object.tags.clear()

        tags_input = form.cleaned_data.get('tags')
        if tags_input:
            tag_names = [tag.strip() for tag in tags_input.split(',') if tag.strip()]

            for tag_name in tag_names:
                tag, created = Tag.objects.get_or_create(name=tag_name)
                self.object.tags.add(tag)

        return response

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


# Delete post (author only)
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'  # templates/blog/post_confirm_delete.html
    success_url = reverse_lazy('post-list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
from django.contrib.auth.decorators import login_required

@login_required
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()

    return redirect('post-detail', pk=pk)

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.object.post.pk})

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def form_valid(self, form):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        form.instance.post = post
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.kwargs['pk']})

class TagPostListView(ListView):
    model = Post
    template_name = 'blog/tag_posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        tag_name = self.kwargs['tag_name']
        return Post.objects.filter(tags__name=tag_name)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag_name'] = self.kwargs['tag_name']
        return context
class SearchResultsView(ListView):
    model = Post
    template_name = 'blog/search_results.html'
    context_object_name = 'posts'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Post.objects.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(tags__name__icontains=query)
            ).distinct()
        return Post.objects.none()
