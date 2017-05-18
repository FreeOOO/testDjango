#coding:utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response

def my_view(request):
    # View code here...
    name = 'hello'
    return render_to_response('index.html',locals())        #locals()相当与生成字典{'name':'hello'}
    #return render(request, 'index.html',{'name':'hello'})
