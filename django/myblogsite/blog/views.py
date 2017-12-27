from django.core.mail import send_mail
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Count
from django.shortcuts import get_object_or_404, render
from django.views.generic.base import View
from taggit.models import Tag

from myblogsite.settings import EMAIL_FROM

from .forms import CommentForm, EmailPostForm
from .models import Comment, Post


# Create your views here.
class PostListView(View):

    def get(self, request, tag_slug=None):
        object_lists = Post.published.all()
        tag = None
        if tag_slug:
            tag = get_object_or_404(Tag, slug=tag_slug)
            object_lists = object_lists.filter(tags__in=[tag])
        paginator = Paginator(object_lists, 3)
        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        return render(request, 'blog/post/list.html', {'posts': posts,
                                                       'page': page,
                                                       'tag': tag})


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
        comment_form = CommentForm()
        comments = post.comments.filter(active=True)

        post_tags_ids = post.tags.values_list('id', flat=True)
        similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
        similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:4]
        return render(request, 'blog/post/detail.html', {'post': post,
                                                         'comments': comments,
                                                         'comment_form': comment_form,
                                                         'similar_posts': similar_posts})

    def post(self, request, year, month, day, post):
        post = get_object_or_404(
            Post,
            slug=post,
            status='published',
            publish__year=year,
            publish__month=month,
            publish__day=day
        )
        comments = post.comments.filter(active=True)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        else:
            comment_form = CommentForm()

        return render(request, 'blog/post/detail.html', {'post': post,
                                                         'comments': comments,
                                                         'comment_form': comment_form,
                                                         'msg': '成功添加评论'})


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
