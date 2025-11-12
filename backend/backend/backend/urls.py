"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from sitecontent import views as sc_views
from sitecontent.views import home, projects_page
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView


urlpatterns = [
    path('', home, name='home'),
    path('projects/', projects_page, name='projects'),

    path('admin/', admin.site.urls),

    # JSON API для фронтенда
    path('api/tariffs/', sc_views.tariffs_list, name='api-tariffs'),
    path('api/projects/', sc_views.projects_list, name='api-projects'),
]

# В режиме отладки отдавать медиа:
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

