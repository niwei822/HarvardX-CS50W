from django.shortcuts import render

tasks = ["a", "b", "c"]
# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })