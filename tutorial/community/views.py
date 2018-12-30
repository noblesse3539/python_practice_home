from django.shortcuts import render
from community.forms import *
# Create your views here.

def write(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save() # 데이터베이스에 저장함
    else :
        form = Form()
    return render(request, 'write.html', {'form':form})

def lists(request):
    articleList = Article.objects.all()
    return render(request, 'list.html', {'articleList':articleList} )

def view(request, num="1"):
    article = Article.objects.get(id=num)
    return render(request, 'view.html', {'article':article})