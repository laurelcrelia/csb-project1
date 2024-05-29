from django.shortcuts import render, redirect, get_object_or_404
from .models import Timer
from .forms import RegisterForm #TimerForm (FIX 3)
from django.utils import timezone
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt # FIX 1 (CSRF Flaw): remove this line.
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login')
def homePageView(request):
    userid=request.GET.get('userid', request.user.id)
    query = "SELECT * FROM countdown_app_timer WHERE creator_id = %s" % userid
    timers = Timer.objects.raw(query)
    for timer in timers:
        timer.remaining_time = calculate_remaining_time(timer.expiration_date)

    return render(request, 'index.html', {'timers': timers})

# FIX 2 (Injection Flaw): 
# def homePageView(request):
#     userid = request.user.id
#     timers = Timer.objects.filter(creator_id=userid)
#     for timer in timers:
#         timer.remaining_time = calculate_remaining_time(timer.expiration_date)

#     return render(request, 'index.html', {'timers': timers})


@csrf_exempt # FIX 1 (CSRF Flaw): remove this @csrf_exempt.
@login_required(login_url='/login')
def createView(request):
    if request.method == 'POST':
        title = request.POST.get('title', '')
        expiration_date = request.POST.get('expiration_date', '')

        timer = Timer.objects.create(
            creator=request.user,
            title=title, 
            # Quick fix to XSS vulnerability would be to add escape() function which sanitizes user input
            # title = escape(title)
            expiration_date=expiration_date
        )
        
        return redirect('/')
    else:
        return render(request, 'create.html')
    
#FIX 3 (XSS)
# @login_required(login_url='/login')
# def createView(request):
#     if request.method == 'POST':
#         form = TimerForm(request.POST)
#         if form.is_valid():
#             timer = form.save(commit=False)
#             timer.creator = request.user
#             timer.save() 
#             return redirect('/')
#     else:
#         form = TimerForm()

#     return render(request, 'create.html', {'form': form})


def registerView(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required
def deleteEvent(request, event_id):
    timer = get_object_or_404(Timer, pk=event_id)
    
    if request.method == 'POST':
        timer.delete()
        return redirect('/')
    
    return render(request, 'delete.html', {'timer': timer})

def calculate_remaining_time(expiration_date):
    now = timezone.now()
    delta = expiration_date - now

    years = delta.days // 365
    months = (delta.days % 365) // 30
    days = delta.days % 30

    return {'years': years, 'months': months, 'days': days}