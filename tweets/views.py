from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from .models import Tweet
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SearchForm
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404



class TweetListView(ListView):
    model = Tweet
    template_name = 'tweets/tweet_list.html'
    context_object_name = 'tweets'


class TweetCreateView(LoginRequiredMixin, CreateView):
    model = Tweet
    fields = ['content', 'image']
    template_name = 'tweets/tweet_form.html'
    success_url = reverse_lazy('tweet_list')

    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)


class TweetUpdateView(LoginRequiredMixin, UpdateView):
    model = Tweet
    fields = ['content']
    template_name = 'tweets/tweet_form.html'
    
    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

    def get_success_url(self):
        return reverse_lazy('tweet_list')

class TweetDeleteView(LoginRequiredMixin, DeleteView):
    model = Tweet
    template_name = 'tweets/tweet_confirm_delete.html'
    success_url = reverse_lazy('tweet_list')

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)
    
    

class TweetSearchView(FormView):
    form_class = SearchForm
    template_name = 'tweets/search_results.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'query' in self.request.GET:
            query = self.request.GET['query']
            context['tweets'] = Tweet.objects.filter(content__icontains=query)
        else:
            context['tweets'] = []
        return context

@login_required
@require_POST
def like_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)
    if request.user not in tweet.likers.all():
        tweet.likers.add(request.user)
    return JsonResponse({'likes_count': tweet.likers.count()})



@login_required
@require_POST
def unlike_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)
    if request.user in tweet.likers.all():
        tweet.likers.remove(request.user)
    return JsonResponse({'likes_count': tweet.likers.count()})
