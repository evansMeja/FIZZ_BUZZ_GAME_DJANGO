from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect,reverse
from django.contrib.auth import login,authenticate,logout
from .models import *
from django.contrib.auth.models import User
from django.http import JsonResponse

restricted_page_error = 'please login to continue'

def bestplayers(request):
    template_name="bestplayers.html"
    scores_list=Scores.objects.all()
    context={'scores_list':scores_list}
    return render(request,template_name,context)


def validatemylogin(request):
	data = {
		'is_logged_out': not request.user.is_authenticated,
		'is_logged_in_client': request.user.is_authenticated and not request.user.is_staff,
		'is_logged_in_admin': request.user.is_authenticated and request.user.is_staff
	}	
	if data['is_logged_out']:
		username = request.POST.get('username', None)
		password = request.POST.get('password', None)
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request,user)
			if request.user.is_staff:
				data['is_logged_in_admin'] = True
			else:
				data['is_logged_in_client'] = True
		else:		
			data['error_message'] = 'Incorect Login Details'
	return JsonResponse(data)
    
def validateregister(request):    
    email = request.POST.get('email', None) 
    data = {
        'email_exists': User.objects.filter(email=email).exists()
    } 
    if not data['email_exists']:
        name = request.POST.get('name', None)
        password = request.POST.get('pass1', None)
        mynewuser = User.objects.create_user(username=email,password=password,email=email)
        user = authenticate(request, username=email, password=password)
        login(request,user)
        ScoresObj = Scores()
        ScoresObj.Owner=user
        ScoresObj.save()
    return JsonResponse(data)

def resetscores(request):
    data = {} 
    scoreObj = Scores.objects.get(Owner=request.user)
    scoreObj.score = 0
    scoreObj.save()
    scoreObj1 = Scores.objects.get(Owner=request.user)
    if scoreObj1.score == 0:
        data['score_reset_sucessfully']=True
    return JsonResponse(data)
    

def savenewscore(request):
    data = {} 
    score1 = request.POST.get('score_fin', None)
    score=int(score1)
    scoreObj = Scores.objects.get(Owner=request.user)
    if scoreObj.score < score:
        scoreObj.score = score
        scoreObj.save()
        data['new_target_achieved']=True
    return JsonResponse(data)

def Logout(request):
	if request.user.is_authenticated:
		logout(request)
		return HttpResponseRedirect('/')
	else:
		return HttpResponseRedirect("/")
    

def index(request):
    if request.user.is_authenticated:
        template_name="index.html"
        context={}
        return render(request,template_name,context)
    else:
        template_name="login.html"
        context={'restricted_page_error':restricted_page_error}
        return render(request,template_name,context)
       
def play(request):
    if request.user.is_authenticated:
        template_name="play.html"
        high_score = Scores.objects.get(Owner=request.user).score
        context={'restricted_page_error':restricted_page_error,'high_score':high_score}
        return render(request,template_name,context)
    else:
        template_name="login.html"
        context={'restricted_page_error':restricted_page_error}
        return render(request,template_name,context)
    
def Login(request):		
	if request.method == 'POST':
		username=request.POST['username']
		password=request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request,user)
			if not request.user.is_staff:
				return HttpResponseRedirect(reverse("play"))
	context={}	
	template_name="login.html"
	return render(request,template_name,context)
    
def register(request):
    template_name="register.html"
    context={}
    return render(request,template_name,context)
    
def rules(request):
    if request.user.is_authenticated:
        template_name="rules.html"
        context={'restricted_page_error':restricted_page_error}
        return render(request,template_name,context)
    else:
        template_name="login.html"
        context={}
        return render(request,template_name,context)