from django.shortcuts import render
import decapp
from django.shortcuts import HttpResponse
from django.db.models import Sum
# Create your views here.


def showMain(request):
    allcat=decapp.models.Company.objects.all().values()

    return render(request,'index.html',{'data':allcat})

def loaddetails(request):
    param=request.GET['param']
    data=decapp.models.Category.objects.filter(topic=param).values('area').distinct()
    print data
    print param
    return render(request,'details.html',{'data':data})

def calculateWeight(request):
    paramset=request.GET.getlist('selection')
    print paramset
    i=0
    listset=[]
    for i in range(0,len(paramset)-1):
        print paramset[i]
        listset.append(paramset[i])
        i=i+1
    print listset
    datasubject = decapp.models.Category.objects.filter(area__in=paramset).values('subject').annotate(sumweight=Sum('weight')).order_by('-sumweight')
    return render(request,'results.html',{'data':datasubject})