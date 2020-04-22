from django.urls import path, re_path
from blog import views


app_name = 'blog'
urlpatterns = [
    path('', views.PostLV.as_view(), name='index'), #/blog/
    path('post/', views.PostLV.as_view(), name='post_list'), #/blog/post/
    re_path(r'^post/(?P<slug>[-\w]+)/$', views.PostDV.as_view(), name='post_detail'), #/blog/post/django-example/
    path('archive/', views.PostAV.as_view(), name='post_archive'), #/blog/archive/
    path('archive/<int:year>/', views.PostYAV.as_view(), name='post_year_archive'), #/blog/archive/2020/
    path('archive/<int:year>/<str:month>/', views.PostMAV.as_view(), name='post_month_archive'), #/blog/archive/2020/nov/
    path('archive/<int:year>/<str:month>/<int:day>/', views.PostDAV.as_view(), name='post_day_archive'), #/blog/archive/2020/nov/10/
    path('archive/today/', views.PostTAV.as_view(), name='post_today_archive'), #/blog/archive/today/
    path('tag/', views.TagCloudTV.as_view(), name='tag_cloud'),
    path('tag/<str:tag>/', views.TaggedObjectLV.as_view(), name='tagged_object_list'),
    path('search/', views.SearchFormView.as_view(), name='search'),
]
