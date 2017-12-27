from django.conf.urls import url
from . import views


urlpatterns = [
    # post views
    url(r'^$', views.PostListView.as_view(), name='post_list'),
    url(r'^tag/(?P<tag_slug>[-\w]+)/$', views.PostListView.as_view(), name='post_list_by_tag'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',
        views.PostDetailView.as_view(), name='post_detail'),
    url(r'^(?P<post_id>\d+)/share/$', views.PostShareView.as_view(),
        name='post_share'),
]