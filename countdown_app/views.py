from django.shortcuts import render, redirect
from .models import Timer
from .forms import TimerForm
from django.utils import timezone

def homePageView(request):
    timers = Timer.objects.all()
    for timer in timers:
        timer.remaining_time = calculate_remaining_time(timer.expiration_date)

    return render(request, 'index.html', {'timers': timers})

def createView(request):
    if request.method == 'POST':
        form = TimerForm(request.POST)
        if form.is_valid():
            timer = form.save(commit=False)
            timer.save()
        return redirect('/')
    return render(request, 'create.html')

def calculate_remaining_time(expiration_date):
    now = timezone.now()
    delta = expiration_date - now

    years = delta.days // 365
    months = (delta.days % 365) // 30
    days = delta.days % 30

    return {'years': years, 'months': months, 'days': days}