from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    data={
        'title':'Home Page',
        'clist':['PHP' , 'Java' , 'Django'],
        'numbers':[10,20,30,40,50],
        'student_details':[
            {'name':'Arshoo', 'phone': 3091981734},
            {'name':'Asharib', 'phone': 3114480425}
            
        ]
    }
    return render(request,"index.html", data)

def aboutUS(request):
    return HttpResponse("<b>Welcome To MyProject</b>")

def course(request, courseid):
    return HttpResponse(courseid)

