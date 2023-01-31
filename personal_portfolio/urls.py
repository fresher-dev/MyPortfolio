from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	path("", views.HomeView.as_view(), name="home"),
	path("<int:pk>/", views.ProjectDetailView.as_view(), name="detail"),
	path("explorer/", views.work_explorer, name="explorer"),
	path("send-mail/", views.sendMail, name="send"),
	path("add/project/", views.CreateProjectView.as_view(), name="add-project"),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)