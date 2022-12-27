from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import git
from django.views.decorators.csrf import csrf_exempt
from .forms import PostForm
from django.views.generic.edit import FormView

@csrf_exempt
def update(request):
    if request.method == "POST":
        repo = git.repo("porosh10.pythonanywhere.com/")
        origin = repo.remotes.origin

        origin.pull()

        return HttpResponse("Updated code on Pythonanywhere!")
    else:
        return HttpResponse("Couldn't update!")



class PostListView(ListView):
    model = Post
    template_name = 'Blogger/home.html'
    posts = Post.objects.all()
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name = 'Blogger/user_posts.html'
    posts = Post.objects.all()
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get('username'))
        return Post.objects.filter(author = user).order_by('-date_posted')



class PostDetailView(DetailView):
    model = Post


# @login_required
# def post_create(request):
#     if request.method == 'POST':
#         p_form = PostForm(request.POST, instance=request.user)
#         if p_form.is_valid():
#             p_form.save()
#             messages.success(request, f'Your Post has been posted!!!!!')
#             return redirect('/')
#     else:
#         p_form = PostForm(instance=request.user)
#     context = {
#         'p_form' : p_form
#     }
#     return render(request,'User/profile.html',context)
#
# @login_required
# def post_update(request, pk):
#     post = Post.objects.get(pk=pk)
#     if request.method == 'POST' and post.author==request.user:
#         p_form = PostForm(request.POST, instance=request.user)
#
#         if p_form.is_valid():
#             p_form.save()
#             messages.success(request, f'Your Post has been Updated!!!!!')
#             return redirect('/')
#     else:
#         p_form = PostForm(instance=request.user)
#     context = {
#         'p_form' : p_form
#     }
#     return render(request,'User/profile.html',context)
class PostCreateView(LoginRequiredMixin, CreateView, FormView):
    # title = forms.CharField()
    # content = forms.CharField(widget=forms.Textarea(attrs={"rows": "5"}))
    form_class = PostForm
    model = Post
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView, FormView):
    model = Post
    # fields = ['title','content']
    form_class = PostForm
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'Blogger/about.html', )


