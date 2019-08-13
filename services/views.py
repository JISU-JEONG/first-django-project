import requests
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'services/index.html')

def artii(request):
    return render(request, 'services/artii.html')

def artii_result(request):
    font = request.GET.get('font')
    text = request.GET.get('text')
    print(font, text)
    result = requests.get(f'http://artii.herokuapp.com/make?text={text}&font={font}')
    print(result)
    context = {
        'result' : result.text
    }
    return render(request, 'services/artii_result.html', context)