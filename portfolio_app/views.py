from django.shortcuts import render, redirect
from .models import * 
from django.conf import settings 
from django.core.mail import send_mail 
from .forms import ContactForm
from django.http import JsonResponse


def blog(request,pk):
      blog = Blog.objects.get(id=pk)
      Categories = Category.objects.all()
      Blogs = Blog.objects.order_by('-date')
      blog.viewed()
      context = {
            'blog':blog,
            'Categories' : Categories,
            'Blogs':Blogs,
      }
      return render(request,"blog.html",context)

def blogs(request):
      Blogs = Blog.objects.order_by('-date')
      context = {
            'Blogs' : Blogs,     
      }
      return render(request,"blogs.html",context)
      
def privacypolicy(request):
      return render(request,"privacy_policy.html")
      
def termofservices(request):
      return render(request,"termofservices.html")


def project(request,pk):
      project = Project.objects.get(id=pk)
      project.viewed()
      context = {
            'project':project
      }
      return render(request,"project.html",context)

def projects(request):
      Projects = Project.objects.order_by('-date')
      context = {
            'Projects' : Projects,
      }
      return render(request,"projects.html",context)

def home(request):
      Projects = Project.objects.order_by('-date')
      Categories = Category.objects.all()
      Blogs = Blog.objects.order_by('-date')
      Educations = Education.objects.order_by('-date')
      Experiences = Experience.objects.order_by('-end')
      Certificates = Certificate.objects.all()
      form = ContactForm()

      context = {
          'Projects' : Projects,
          'Categories' : Categories,  
          'Blogs' : Blogs,     
          'Educations' : Educations,  
          'Experiences' : Experiences,  
          'Certificates' : Certificates,
          'form':form,  
      }
      return render(request,"index.html",context)
      
#sending emails
def sendmail(request):
      form = ContactForm()
      if request.method == 'POST':
            form = ContactForm(request.POST or None)
            if form.is_valid():
                  name = request.POST.get('name')
                  subject = request.POST.get('subject')
                  message = request.POST.get('message')
                  from_email = request.POST.get('email')
                  recipient_list = [settings.EMAIL_HOST_USER]
                  send_mail(subject, message, from_email, recipient_list) 
                  form.save()
                  response = {
                        'name': name,
                        }
                  return JsonResponse(response,safe=False)
            else:
                  form = ContactForm()
      context = {
            'form':form
      }
      return render(request,"index.html",context)
      
      
      
#Errors Page handling      
def custom_page_not_found_view(request, exception):
    return render(request, "errors/error404.html", {})

def custom_error_view(request, exception=None):
    return render(request, "errors/error500.html", {})

def custom_permission_denied_view(request, exception=None):
    return render(request, "errors/error403.html", {})

def custom_bad_request_view(request, exception=None):
    return render(request, "errors/error400.html", {})
