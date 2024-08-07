from django.shortcuts import render, redirect
from . import models
from . import forms
from django.urls import reverse, reverse_lazy

from django.contrib.auth.decorators import  login_required
from django.contrib.auth.forms import  UserCreationForm
from django.views.generic import  CreateView

# Create your views here.

def list_tweet(request):
    all_tweets = models.Tweet.objects.all()
    tweet_dict = {"tweets" : all_tweets}
    return render(request, 'tweetapp/listtweet.html', context= tweet_dict)

@login_required(login_url="/login")
def add_tweet(request):
    if request.POST:
        nickname = request.POST["nickname"]
        message = request.POST["message"]
        tweet = models.Tweet(nickname = nickname, message = message)
        tweet.save()
        return redirect(reverse("tweetapp:list_tweet"))
    return render(request, 'tweetapp/addtweet.html')


def add_tweet_byForm(request):
    if request.POST :
        form = forms.AddTweetForm(request.POST)
        if form.is_valid() :
            print(form.cleaned_data)
            nickname = form.cleaned_data["nickname_input"]
            message = form.cleaned_data["message_input"]
            tweet = models.Tweet(nickname = nickname, message = message)
            tweet.save()
            return(redirect(reverse('tweetapp:list_tweet')))
        
        else:
            print("Error in form")
            return render(request,"tweetapp/addtweetbyform.html", context={"form":form})



    else:
        form = forms.AddTweetForm()
        return render(request,"tweetapp/addtweetbyform.html", context={"form":form})
    

def add_tweet_by_ModelForm(request):
    if request.POST :
        form = forms.AddTweetModelForm(request.POST)
        if form.is_valid() :
            print(form.cleaned_data)
            nickname = form.cleaned_data["nickname"]
            message = form.cleaned_data["message"]
            tweet = models.Tweet(nickname = nickname, message = message)
            tweet.save()
            return(redirect(reverse('tweetapp:list_tweet')))
        
        else:
            print("Error in form")
            return render(request,"tweetapp/addtweetbymodelform.html", context={"form":form})



    else:
        form = forms.AddTweetModelForm()
        return render(request,"tweetapp/addtweetbymodelform.html", context={"form":form})




class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name =  "registration/signup.html"

