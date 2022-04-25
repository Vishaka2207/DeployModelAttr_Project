from django.http import HttpResponse
from django.shortcuts import render
import joblib

def index(request):
    return render(request,"index.html")

def home(request):
    return render(request,"home.html")

def Attrition(request):
    return render(request,"Attrition.html")

def Churnform(request):
    return render(request,"Churnform.html")

def result(request):

    cls = joblib.load('finalized_attr2.sav')
#    lis = []

#    lis.append(request.GET['RI'])
#    lis.append(request.GET['Na'])
#    lis.append(request.GET['Mg'])
#    lis.append(request.GET['Al'])
#    lis.append(request.GET['Si'])
#    lis.append(request.GET['K'])
#    lis.append(request.GET['Ca'])
#    lis.append(request.GET['Ba'])
#    lis.append(request.GET['Fe'])
#    lis.append(request.GET['Fe'])
#    lis.append(request.GET['Fe'])
#    lis.append(request.GET['Fe'])
#    lis.append(request.GET['Fe'])

    A1 = int(request.GET['A1'])
    A2 = int(request.GET['A2'])
    A3 = int(request.GET['A3'])
    A4 = int(request.GET['A4'])
    A5 = int(request.GET['A5'])
    A6 = int(request.GET['A6'])
    A7 = int(request.GET['A7'])
    A8 = int(request.GET['A8'])
    A9 = int(request.GET['A9'])
    A10= int(request.GET['A10'])

#    ans = cls.predict(RI,Na,Mg,Al,Si,K,Ca,Ba,Fe,Fe,Fe,Fe,Fe)
#    ans = cls.predict([[A1,A2,A3,A4,A5,A6,A7,A8,A9,A10]])

#    if ans == 0:
#        return "Will not leave the bank"
#    elif ans == 1:
#        return "Will leave the bank"
#    else:
#        return "error"
#    return HttpResponse(str(ans))

    ans = cls.predict([[A1,A2,A3,A4,A5,A6,A7,A8,A9,A10]])

    if ans == 0:
        ans=" will most probably not not leave the bank"
    elif ans == 1:
        ans=" has high chances of leaving the bank"
    else:
        ans="Error"

    return render(request,"result.html",{'ans':ans, 'A1':A1})


#    ans = cls.predict([lis])

#    return render(request,"result.html",{'ans':ans,'lis':lis})
