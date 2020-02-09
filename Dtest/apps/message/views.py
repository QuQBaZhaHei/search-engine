# _*_ coding: utf-8 _*_
from django.shortcuts import render
from . import search_indexes

# Create your views here.
def getform(request):
    '''
    if request.method=="POST":
        keyword=request.POST.get('keyword','')
        user_message=UserMessage()
        user_message.keyword=keyword
        user_message.save()
    '''
    return render(request, 'message_form.html')


def getsearch(request):
    request.encoding = 'utf-8'
    if 'keyword' in request.GET and request.GET['keyword']:
        message = request.GET['keyword']
        search_indexes.search(message)
        context = {}
        context['message'] = message
        con1 = []
        con2 = []
        for i in range(1, 5):
            con1.append('界面设计')
        context['hort'] = con1
        for i in range(1, 5):
            con2.append('历史网页')
        context['history'] = con2
        return render(request, 'search.html', context)
    else:
        message = '你提交的空表单'
        return render(request, 'message_form.html')
    return render(request,'search.html')