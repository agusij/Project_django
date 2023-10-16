from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Tweet
from django.contrib.auth.mixins import LoginRequiredMixin


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