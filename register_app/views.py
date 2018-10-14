from django.shortcuts import render


# Create your views here.
def index(request):
    name = 'phone number'
    value = '09384677005'
    context ={'title':name,
              'value':value}
    return render(request, 'index.html', context)