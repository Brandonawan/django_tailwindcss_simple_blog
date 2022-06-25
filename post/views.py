from django.shortcuts import get_object_or_404, redirect, render
from .models import Post, Comment, Category

# Create your views here.
def index(request):
    posts = Post.objects.all

    return render(request, 'index.html', {'posts': posts} )

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == 'POST':
        name = request.POST.get('name', '')
        comment = request.POST.get('comment', '')

        if name and comment:
            comment = Comment.objects.create(
                post = post,
                name = name,
                comment = comment
            )

            return redirect('post_detail', slug=post.slug)

    return render(request, 'detail.html', {'post': post})

def category_detail(request, pk):
    post = get_object_or_404(Category, pk=pk)

    return render(request, 'category.html', {'category': category})