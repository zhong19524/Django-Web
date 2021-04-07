from django.urls import path
from . import views
from .views import PostListView , PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

urlpatterns = [
#path looking for postlistview:  <app>/<model>_<viewtype>.html. ex. /post_list.html
#path("", views.home, name="mysite_home"),
path("", PostListView.as_view(), name="mysite_home"),
path("post/<int:pk>", PostDetailView.as_view(), name="post_detail"),
path("post/<str:username>", UserPostListView.as_view(), name="user_posts"),
path("post/new/", PostCreateView.as_view(), name="post-create"),
path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
path("about/", views.about, name="mysite_about")
]
