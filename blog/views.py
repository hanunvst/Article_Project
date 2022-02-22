from django.contrib.auth.models import User
from django.contrib.auth.views import redirect_to_login
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.contrib.auth.decorators import login_required

from django.views.generic import (
    ListView,DetailView,CreateView,UpdateView,DeleteView
)

from django.contrib.auth.mixins import (
    LoginRequiredMixin,UserPassesTestMixin
)

class  PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/home.html'
    ordering = ['-date_posted']
    paginate_by = 2


class  PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post_detail.html'

class  PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content', ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    context_object_name = 'form'
    template_name = 'blog/post_form.html'

class  PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', ]
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()

        if self.request.user == post.author:
            return True
        return False

    def handle_no_permission(self):
        if self.raise_exception:
            raise PermissionDenied(self.get_permission_denied_message())
        return redirect_to_login(
            self.request.get_full_path(),
            self.get_login_url(),
            self.get_redirect_field_name()
        )

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    login_url = 'login'

    '''
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    '''

    def test_func(self):
        post = self.get_object()

        if self.request.user == post.author:
            return True
        return False

    def handle_no_permission(self):
        if self.raise_exception:
            raise PermissionDenied(self.get_permission_denied_message())
        return redirect_to_login(
            self.request.get_full_path(),
            self.get_login_url(),
            self.get_redirect_field_name()
        )

    context_object_name = 'post'
    template_name = 'blog/post_confirm_delete.html'


class  UserPostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/user_posts.html'
    # ordering = ['-date_posted']
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(
            User,  username=self.kwargs.get('username')
        )

        return Post.objects.filter(author=user).order_by('-date_posted')



def  latest_posts_view(request):
    latest_posts = Post.objects.all().order_by('-date_posted')[0:3]
    context = {
        "latest_posts" : latest_posts
    }
    return render(request,'blog/latest_posts.html', context)


def interview_questions_view(request):
    return render(request,'blog/interview_questions.html')

def responsive_view(request):
    return render(request, 'blog/responsive.html')


'''
def home_view(request):
    posts = Post.objects.all()
    context = {
        "posts" : posts
    }
    return render(request,'blog/home.html', context)
'''

# @login_required(login_url='/login/')
@login_required
def about_view(request):
    return render(request,'blog/about.html')