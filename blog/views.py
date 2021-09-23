'''Arquivo de views do projeto.
Serve para acessar os templates de acordo com o
requisitado.'''

from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from blog.forms import PostForm
from blog.models import Post

# pylint: disable=invalid-name

# Create your views here.


def post_list(request):
    '''Fornece a lista de Posts registrados de acordo com a data especificada'''

    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by(
        'published_date'
    )
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    '''Fornece detalhes do Post em questão'''

    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    '''Usado para a criação de um novo Post'''

    if request.method != 'POST':
        form = PostForm()
    else:
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    '''Usado para a edição de um Post já existente'''

    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def about(request):
    '''Acesso a página About'''
    return render(request, 'blog/about.html', {})


def admin(request):
    '''Acesso a página Admin'''
    return render(request, 'admin/', {})
