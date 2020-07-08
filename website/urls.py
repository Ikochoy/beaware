from django.urls import path

from . import views

app_name= 'website'
urlpatterns = [
    path('home', views.home, name='home'),
    path('politics', views.politics, name='politics'),
    path('environment', views.environment, name='environment'),
    path('culture', views.culture, name='culture'),
    path('technology', views.technology, name='technology'),
    path('economics', views.economics, name='economics'),
    path('topnews', views.topnews, name='topnews'),
    path('discussions', views.discussions, name='discussions'),
    path('signup', views.sign_up, name='sign_up'),
    path('login', views.login_view, name='login_view'),
    path('add_post', views.add_post, name='add_post'),
    path('render_comment_modal/', views.render_comment_modal,
         name='render_comment_modal'),
    path('add_comment/', views.add_comment, name='add_comment'),
    path('like_post/', views.like_post, name='like_post'),
    path('unlike_post/', views.unlike_post, name='unlike_post'),
    path('dislike_post/', views.dislike_post, name='dislike_post'),
    path('undislike_post/', views.undislike_post, name='undislike_post'),
    path('render_reply_comment_modal/', views.render_reply_comment_modal,
         name='render_reply_comment_modal'),
    path('add_reply_comment/', views.add_reply_comment, name='add_reply_comment'),
    path('like_comment/', views.like_comment, name='like_comment'),
    path('unlike_comment/', views.unlike_comment, name='unlike_comment'),
    path('dislike_comment/', views.dislike_comment, name='dislike_comment'),
    path('undislike_comment/', views.undislike_comment, name='undislike_comment'),
]
