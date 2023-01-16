from django.shortcuts import render
from .models import Project
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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