from django.shortcuts import render

# Create your views here.
def homepage(request):
    string_to_dispaly = "Welcome"
    title = "The Science Hub "
    context = {"string_to_dispaly": string_to_dispaly, "title": title}
    return render(request, "home_page/base.html", context)
