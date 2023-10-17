from django.urls import path
from . import views
from .views import TweetListView, TweetCreateView, TweetDeleteView, TweetUpdateView, TweetSearchView

urlpatterns = [
    path('tweets/', TweetListView.as_view(), name='tweet_list'),
    path('tweet/new/', TweetCreateView.as_view(), name='tweet_create'),
    path('tweets/edit/<int:pk>/', TweetUpdateView.as_view(), name='tweet_update'),
    path('tweets/delete/<int:pk>/', TweetDeleteView.as_view(), name='tweet_delete'),
    path('tweet/<int:tweet_id>/like/', views.like_tweet, name='like_tweet'),
    path('tweet/<int:tweet_id>/unlike/', views.unlike_tweet, name='unlike_tweet'),
    path('search/', TweetSearchView.as_view(), name='tweet_search'), 

]
