from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request,'testapp/index.html')

def movies_view(request):
    msg1='Movie Information 1'
    msg2='Movie Information 1'
    msg3='Movie Information 1'
    msg4='Movie Information 1'
    msg5='Movie Information 1'
    my_dict={'msg1':msg1,'msg2':msg2,'msg3':msg3,'msg4':msg4,'msg5':msg5}
    return render(request,'testapp/movies.html',context=my_dict)

def sports_view(request):
    return render(request,'testapp/sports.html')

def politics_view(request):
    return render(request,'testapp/politics.html')
