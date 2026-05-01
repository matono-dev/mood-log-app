from django.shortcuts import render, redirect
from .models import MoodLog

# Create your views here.
def pages(request):
    
    #データ入力についての処理
    if request.method == "POST":
        mood = request.POST.get("mood")
        action = request.POST.get("action")
        MoodLog.objects.create(
            mood = mood,
            action = action,
        )

        return redirect("/")
    
    #一覧表示
    data = MoodLog.objects.all()
    return render(request,"logs/log_list.html",{"logs":data})
