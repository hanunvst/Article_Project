
from django.urls import path
from blog import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='blog_home'),

    path('post/<int:pk>/detail/', views.PostDetailView.as_view(),
         name='post_detail'),

    path('post/create/', views.PostCreateView.as_view(),
         name='post_create'),

    path('post/<int:pk>/update/', views.PostUpdateView.as_view(),
         name='post_update'),

    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(),
         name='post_delete'),

    path('user/<str:username>/', views.UserPostListView.as_view(),
         name='user_posts'),

    path('latest_posts/', views.latest_posts_view, name='latest_posts'),

    path('interview_questions/', views.interview_questions_view, name='interview_questions'),

    path('responsive/', views.responsive_view, name='responsive'),

    # path('', views.home_view, name='blog_home'),
    path('about/', views.about_view, name='blog_about'),
]