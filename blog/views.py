from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .models import Post, Comment, Contributor
from .forms import CommentForm, PostForm


# Lists view for posts
class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


# Selected post detail view
class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('-created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            'post_detail.html',
            {
                'post': post,
                'comments': comments,
                'liked': liked,
                'comment_form': CommentForm()

            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )


# Remove or add like on post detail page view
class PostLike(LoginRequiredMixin, View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


# Update a post on post detail page view with
# success message feedback
class UpdatePost(LoginRequiredMixin, SuccessMessageMixin,
                 UserPassesTestMixin, generic.UpdateView):
    model = Post
    template_name = 'post_add_edit.html'
    form_class = PostForm
    success_message = 'Post Edited'

    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


# Delete a post on post detail page view with
# success message feedback
class PostDelete(LoginRequiredMixin, SuccessMessageMixin,
                 UserPassesTestMixin, generic.DeleteView):
    model = Post
    template_name = 'post_detail.html'
    success_url = '/'
    success_message = 'Post Deleted'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(PostDelete, self).delete(request, *args, **kwargs)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


# Create a post with a post form view with
# success message feedback
class AddPost(LoginRequiredMixin, SuccessMessageMixin,
              UserPassesTestMixin, generic.CreateView):
    model = Post
    template_name = 'post_add_edit.html'
    form_class = PostForm
    success_message = 'Post Created'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_staff


# View for About Us page
class AboutUs(generic.ListView):
    model = Contributor
    context_object_name = 'contributor_list'
    queryset = Contributor.objects.all().order_by('name')
    template_name = 'aboutus.html'
