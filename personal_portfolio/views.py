from django.shortcuts import render, redirect
from .models import Project
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from django.conf import settings


class HomeView(ListView):
	template_name = "personal_portfolio/home.html"

	queryset = Project.objects.all()[:3]


class ProjectDetailView(DetailView):
	template_name = "personal_portfolio/detail.html"
	queryset = Project.objects.all()


def work_explorer(request):
	projects = Project.objects.all()

	paginator = Paginator(projects, 6)
	page = request.GET.get('page', 1)

	try:
		page_obj = paginator.page(page)

	except PageNotAnInteger:
		page_obj = paginator.page(1)

	except EmptyPage:
		page_obj = paginator.page(paginator.num_pages)

	context = {
		"projects": projects,
		"page_obj": page_obj,
		"page": page,
	}

	return render(request, "personal_portfolio/work_explorer.html", context)


def sendMail(request):
	if request.method == "POST":
		name = request.POST.get('name')
		email = request.POST.get('email')
		messages = request.POST.get('messages')

		subject = "Welcome to Django Web Mail Services"
		message = f"\nYour messages\n--------------------------\n{messages}\n--------------------------\n\nHi {name}, thank you for your attention."
		email_form = settings.EMAIL_HOST_USER
		receipient_list = [email]
		send_mail(subject, message, email_form, receipient_list)
	return redirect("home")

class CreateProjectView(CreateView):
	model = Project
	fields = ['title', 'description', 'technology', 'image', 'link']
	template_name = "personal_portfolio/add_project.html"