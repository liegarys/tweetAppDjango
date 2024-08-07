from django.contrib import admin
from django.urls import path
from . import views


app_name = "tweetapp"

urlpatterns = [
    path('', views.list_tweet, name= "list_tweet"),
    path('addtweet/',  views.add_tweet, name= "add_tweet"),
    path('addtweetbyform/', view= views.add_tweet_byForm, name='add_tweet_by_form'),
    path('addtweetbymodelform/', view= views.add_tweet_byForm, name='add_tweet_by_model_form'),
    path('signup/', view=views.SignUpView.as_view(), name="signup"),

]
