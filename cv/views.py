from django.shortcuts import render

def index(request):
    context = {
        "name": "Ali",
        "last_name": "Mohammadinezhad",
        "phone": "+98 935 213 3383",
        "email": "alimn1382@gmail.com",
        "address": "Tabriz, East Azarbaijan, Iran"
        }
    return render(request, 'cv/index.html', context)
