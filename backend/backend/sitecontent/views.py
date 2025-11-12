from django.http import JsonResponse
from .models import Tariff, Project
from django.views.decorators.http import require_GET
from django.shortcuts import render
from .models import Review, Tariff, Project

@require_GET
def tariffs_list(request):
    tariffs = Tariff.objects.all()
    data = [t.as_dict() for t in tariffs]
    return JsonResponse({"results": data})

@require_GET
def projects_list(request):
    projects = Project.objects.all()
    data = [p.as_dict() for p in projects]
    return JsonResponse({"results": data})


def home(request):
    reviews = Review.objects.all()
    return render(request, 'index.html', {
        'reviews': reviews,
    })


def projects_page(request):
    return render(request, 'project.html')