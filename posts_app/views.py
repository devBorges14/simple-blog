from django.shortcuts import render
from posts_app.models import Post

def post_list(request):
    template_name = 'post_list.html'  # Nome do template
    posts = Post.objects.all().order_by('-data_publicacao')  # Agora o mais recente vem primeiro
    context = {'posts': posts}  # Passa os posts para o template
    return render(request, template_name, context)
