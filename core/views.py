from django.shortcuts import render, HttpResponse
# Create your views here.
"""
Inicio-home
Historia-about
Sevicios-services
Visitanos- store
Contacto-contact
Blog-blog
Sample-sample
"""
def home(request):
    return render(request,"core/home.html")

def about(request):
    return render(request,"core/about.html")



def store(request):
    return render(request,"core/store.html")



