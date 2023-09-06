from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Leticia Kalila Darlene',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)
