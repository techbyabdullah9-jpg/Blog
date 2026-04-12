from django.shortcuts import get_object_or_404, render

from blog.models import Post

# Create your views here.

def post_detail(request, pk):
    p_detail = get_object_or_404(Post, pk=pk)
    context = {
        'p_detail': p_detail,
    }
    return render(request, 'post_detail.html', context)