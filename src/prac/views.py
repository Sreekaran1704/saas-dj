import pathlib
from django.shortcuts import render
from django.http import HttpResponse

from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent
def home_page_view(request, *args, **kwargs):
    my_title = "My page"
    page_queryset = PageVisit.objects.filter(path=request.path)
    queryset = PageVisit.objects.all()
    my_context = {
        "page_title" : my_title,
        "page_visits_count" : page_queryset.count(),
        "all_visits_count" : queryset.count(),
    }
    html_template = "home.html"
    path = request.path
    print(f"Path: {path}")
    PageVisit.objects.create(path=request.path)
    return render(request, html_template, my_context)