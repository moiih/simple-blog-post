from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .forms import BlogForm
from .models import BlogModel

# Create your views here.

def register(request):

    if not request.user.is_authenticated:

        if request.method == 'POST':

            username = request.POST['username']
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']

            if password1 == password2:

                if User.objects.filter(username=username).exists():
                    messages.info(request, 'This Username Already Exists!')
                    return redirect('/register/')
                
                elif User.objects.filter(email=email).exists():
                    messages.info(request, 'This Username Already Exists!')
                    return redirect('/register/')

                else:
                    user = User.objects.create_user(username=username, password=password1, email=email)
                    user.save()
                    print('\n\tUser Created \n\n')
                    return redirect('/login/')

            else:
                messages.info(request, 'Two Passwords Do Not Match!!')
                return redirect('/register/')

            return rediect('/')

        else:
            return render(request, 'register.html')
    
    else:
        return render(request, 'home.html')




def login(request):

    if not request.user.is_authenticated:

        if request.method == 'POST':

            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'Invalid Credentials!!')
                return redirect('/login/')

        else:
            return render(request, 'login.html')

    else:
        return render(request, 'home.html')



def logout(request):
    auth.logout(request)
    return redirect('/login/')



def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return redirect('/login/')



def write_blog(request):

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()            
            messages.success(request, 'Post Successful..!!')
    else:
        form = BlogForm()

    context = { 'form' : form }
    return render(request, 'write_blog.html', context)



# def user_post(request):

#     if request.method == 'GET':
#         if request.GET.get('toogle') is None:
#             snippets = BlogModel.objects.all()
#         else:
#             snippets = BlogModel.objects.all().filter(user_id__exact=request.user.id)    
            
#     else:
#         snippets = BlogModel.objects.all().filter(user_id__exact=request.user.id)    

#     context = { 'snipps' : snippets, 'uid' : request.user.id}
#     return render(request, 'user_post.html', context)



def user_posts(request):

    snippets = BlogModel.objects.all().filter(user_id__exact=request.user.id)    

    context = { 'snipps' : snippets }
    return render(request, 'user_posts.html', context)



def all_posts(request):

    all_snippets = BlogModel.objects.all()        

    context = { 'all_snipps' : all_snippets }
    return render(request, 'all_posts.html', context)