from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406350394',
        'name': 'Hannan Afif Darmawan',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)