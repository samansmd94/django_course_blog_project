from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.views import generic
from django.urls import reverse_lazy

from .forms import PostForm
from .models import Post

# Create your views here.

class PostListView(generic.ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts_list"

    def get_queryset(self):
        return Post.objects.filter(status='pub').order_by('-datetime_modified')

class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

class PostCreateView(generic.CreateView):
    form_class = PostForm
    template_name = "blog/post_create.html"

class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_create.html"

class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = "blog/post_delete.html"
    success_url = reverse_lazy("posts_list")

# def post_list_view(request):
#     # posts_list = Post.objects.all() # ORM
#     posts_list = Post.objects.filter(status='pub').order_by('-datetime_modified')
#     return render(request, "blog/post_list.html", {"posts_list": posts_list})

# def post_detail_view(request, pk):
#     # post = Post.objects.get(pk=pk)
#     # try:
#     #     post = Post.objects.get(pk=pk)
#     # except Post.DoesNotExist:
#     # except ObjectDoesNotExist:
#     #     post = None
#     #     print("Excepted")
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, "blog/post_detail.html", {"post": post})

# def post_create_view(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("posts_list")
#     else: # Get request
#         form = PostForm()
#
#     return render(request, "blog/post_create.html", {"form": form})
#     # if request.method == "POST":
#     #     post_title = request.POST.get("title")
#     #     post_text = request.POST.get("text")
#     #
#     #     user = User.objects.all()[0] # Django ORM
#     #     Post.objects.create(title=post_title, text=post_text, author= user, status="pub")
#     # else:
#     #     print("GET request")
#     # return render(request, "blog/post_create.html")

# def post_update_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     form = PostForm(request.POST or None, instance=post)
#
#     if form.is_valid():
#         form.save()
#         return redirect("posts_list")
#
#     return render(request, "blog/post_create.html", {"form": form})

# def post_delete_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == "POST":
#         post.delete()
#         return redirect("posts_list")
#
#     return render(request, "blog/post_delete.html", {"post": post})