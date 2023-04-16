from django.http import HttpResponse
from django.shortcuts import render
from base.models import Item

def home(request):
    print("-------------------------------------------")
    menu_items = Item.objects.all()
    context = {"items":menu_items}
    return render(request, "index.html", context)

def menu(request):
    return render(request, "menu.html")

def services(request):
    return render(request, "services.html")
def blog(request):
    return render(request, "blog.html")
def about(request):
    return render(request, "about.html")
def contact(request):
    return render(request, "contact.html")


#   path("", views.home, name ="home"),
#     path("menu", views.menu, name ="menu")
#     path("services", views.services, name ="services")
#     path("blog", views.blog, name ="blog")
#     path("about", views.about, name ="about")
#     path("contact", views.contact, name ="contact")'