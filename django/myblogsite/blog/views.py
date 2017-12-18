from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
class PostListView(View):

    def get(self, request):
        object_lists = Post.published.all()
        paginator = Paginator(object_lists, 3)
        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        return render(request, 'blog/post/list.html', {'posts': posts,
                                                       'page': page})


class PostDetailiew(View):
    def get(self, request, year, month, day, post):
        post = get_object_or_404(
            Post,
            slug=post,
            status='published',
            publish__year=year,
            publish__month=month,
            publish__day=day
        )
        return render(request, 'blog/post/detail.html', {'post': post})
        
