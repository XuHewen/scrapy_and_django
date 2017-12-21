from django.core.mail import send_mail
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render
from django.views.generic.base import View

from myblogsite.settings import EMAIL_FROM

from .forms import EmailPostForm
from .models import Post


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


class PostDetailView(View):
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


class PostShareView(View):
    def get(self, request, post_id):
        post = get_object_or_404(Post, id=post_id, status='published')
        form = EmailPostForm()
        return render(request, 'blog/post/share.html',
                      {'post': post, 'form': form})
    
    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id, status='published')
        form = EmailPostForm(request.POST)
        sent = False
        if form.is_valid():
            
            cd = form.cleaned_data

            post_url = request.build_absolute_uri(
                post.get_absolute_url()
            )

            subject = '{} ({}) recommends you reading "{}"'.format(
                cd['name'], cd['email'], post.title
            )

            message = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(
                post.title, post_url, cd['name'], cd['comments']
            )

            send_mail(subject, message, EMAIL_FROM, [cd['to']])

            sent = True
        else:
            form = EmailPostForm()
        
        return render(request, 'blog/post/share.html',
                      {'post': post,
                       'form': cd,
                       'sent': sent})
