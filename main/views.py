from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Syarna Savitri',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)