from django.contrib.auth import login, authenticate
from rest_framework.views import APIView
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.utils.decorators import method_decorator
from database.models import Tweet, CommentsAndStatus
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count


class UserLoginView(View):

    def get(self, request, format=None):
        if request.user.is_authenticated:
            print(f'request.user ==> {request.user}')
            return redirect('UserTweets') 
        form = LoginForm()
        return render(request, 'user/login_form.html', {'form': form})
    
    def post(self, request, format=None):
        # print(f'request.POST ==> {request.POST}')
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect('UserTweets') 
        return redirect('login') 


@method_decorator(login_required(login_url='login'), name='dispatch')
class UserTweets(View):
    def get(self, request, format=None):
        # print(f'request.user ==> {request.user}')
        user_data = request.user
        tweets = Tweet.objects.values("id", "tweet","created_datetime").filter(user_id=user_data.id).order_by("id")
        # always use order_by while using paginator
        paginator = Paginator(tweets, 10)  # Show 10 items per page
        page = request.GET.get('page')
        try:
            tweet_10 = paginator.page(page)
        except PageNotAnInteger:
            # If the page is not an integer, deliver the first page.
            tweet_10 = paginator.page(1)
        except EmptyPage:
            # If the page is out of range (e.g., 9999), deliver the last page.
            tweet_10 = paginator.page(paginator.num_pages)

        # print(len(tweets))
        # return HttpResponse(f"<h1>{user_data.id}</h1>")
        # print(f'tweet_10 ==> {tweet_10}')
        return render(request, 'user/user_tweets.html', context={'tweets': tweet_10, "user_email": user_data.email, "add_tweet":AddTweetForm(), "search_tweet":SearchTweetForm()})
    
    def post(self,request):
        print(f'data ==> {request.POST}')
        form = AddTweetForm(request.POST)
        search_form = SearchTweetForm(request.POST)
        if form.is_valid():
            tweet = form.cleaned_data.get("tweet")
            Tweet.objects.create(tweet=tweet, user_id = request.user)
            return redirect("UserTweets")

        elif search_form.is_valid():
            return HttpResponse("search_form")
        return HttpResponse("failed to create <Tweet>")


@method_decorator(login_required(login_url='login'), name='dispatch')
class CustomLogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        # Redirect to the desired page after logout
        return redirect('login')


@method_decorator(login_required(login_url='login'), name='dispatch')
class MyDetail(View):

    def get(self, request, *args, **kwargs):
        user_data = request.user
        tweet_counts = Tweet.objects.filter(user_id=user_data).count()
        '''
        select count(*), status  from comments_n_status where user_id = 1 group by status
        '''
        comments_on_tweet_count = CommentsAndStatus.objects.filter(user_id=user_data).values('status').annotate(count=Count('id'))
        print(f'comments_on_tweet_count ==> {comments_on_tweet_count}')

        return HttpResponse("ok")



@method_decorator(login_required(login_url='login'), name='dispatch')
class UserEditTweet(View):

    def post(self, request, tweet_id):
        form = EditTweetForm(request.POST)
        obj = get_object_or_404(Tweet, id=tweet_id)
        if form.is_valid() and obj.user_id.id is request.user.id:
            # Save the updated data to the database
            return HttpResponse("edit form is valid")
        return HttpResponse("this is not your tweet")

    def get(self, request, tweet_id):
        obj = get_object_or_404(Tweet, id=tweet_id)
        if obj.user_id.id is request.user.id:
            form = EditTweetForm(initial={'edit_tweet': obj.tweet})
            return render(request, 'user/edit_tweet.html', {'form': form, 'object_id': tweet_id})
        return HttpResponse("this is not your tweet")



# @method_decorator(login_required(login_url='login'), name='dispatch')
class HashTags(View):
    def get(self, request, *args, **kwargs):
        search_term = request.GET.get('search_term', '')
        print(f'search_term ==> {search_term}')
        return HttpResponse("ok")
    



class TestTweet(View):
    def get(self, request, format=None):
        tweets = Tweet.objects.values("id", "tweet","created_datetime").filter().order_by("id")
        paginator = Paginator(tweets, 10)  # Show 10 items per page
        page = request.GET.get('page')
        try:
            tweet_10 = paginator.page(page)
        except PageNotAnInteger:
            tweet_10 = paginator.page(1)
        except EmptyPage:
            tweet_10 = paginator.page(paginator.num_pages)
        return render(request, 'test/test_search.html', context={'tweets': tweet_10})
    
    def post(self,request):
        print(f'data ==> {request.POST}')
        search_query = request.POST.get("search_query")
        tweets = Tweet.objects.values("id", "tweet","created_datetime").filter(tweet__icontains=search_query).order_by("id")
        paginator = Paginator(tweets, 10)  # Show 10 items per page
        page = request.GET.get('page')
        # page = 10
        try:
            tweet_10 = paginator.page(page)
        except PageNotAnInteger:
            tweet_10 = paginator.page(1)
        except EmptyPage:
            tweet_10 = paginator.page(paginator.num_pages)
        return render(request, 'test/test_search.html', context={'tweets': tweet_10, "search_query":search_query})
    
