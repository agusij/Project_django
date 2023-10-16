from django.urls import path
from .views import TweetListView, TweetCreateView, TweetDeleteView, TweetUpdateView

urlpatterns = [
    path('tweets/', TweetListView.as_view(), name='tweet_list'),
    path('tweet/new/', TweetCreateView.as_view(), name='tweet_create'),
    path('tweets/edit/<int:pk>/', TweetUpdateView.as_view(), name='tweet_update'),
    path('tweets/delete/<int:pk>/', TweetDeleteView.as_view(), name='tweet_delete'),


]
