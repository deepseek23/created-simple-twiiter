from django.shortcuts import render, get_object_or_404, redirect
from .models import Tweet, Twiit
from .forms import tweetForm, UserRegistrationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from rest_framework import generics
from .serializers import TweetSerializer
from django.http import JsonResponse
from django.views.decorators.http import require_POST

# Create your views here.
def index(request):
    return render(request, 'index.html')

def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')  # Changed to descending order
    return render(request, 'tweet_list.html', {'tweets': tweets})

@login_required
def tweet_create(request):
    if request.method == 'POST':
       form = tweetForm(request.POST, request.FILES)
       if form.is_valid():
           tweet = form.save(commit=False)
           tweet.user = request.user
           tweet.save()
           return redirect('tweet_list')
    else:
        form = tweetForm()
    return render(request, 'tweet_form.html', {'form': form})

@login_required
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == 'POST':
       form = tweetForm(request.POST, request.FILES, instance=tweet)
       if form.is_valid():
           tweet = form.save(commit=False)
           tweet.user = request.user
           tweet.save()
           return redirect('tweet_list')
    else:
        form = tweetForm(instance=tweet)
    return render(request, 'tweet_form.html', {'form': form})
    
@login_required
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweet_list')
    else:
        return render(request, 'tweet_confirm_delete.html', {'tweet': tweet})

@login_required
@require_POST
def toggle_like(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id)
    user = request.user
    
    if user in tweet.likes.all():
        tweet.likes.remove(user)
        liked = False
    else:
        tweet.likes.add(user)
        liked = True
    
    return JsonResponse({
        'liked': liked,
        'total_likes': tweet.total_likes()
    })

def register(request):
    if request.method == 'POST':
         form = UserRegistrationForm(request.POST)
         if form.is_valid():
             user = form.save(commit=False)
             user.set_password(form.cleaned_data['password1'])
             user.save()
             login(request, user)
             return redirect('tweet_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

class TweetListCreate(generics.ListCreateAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer