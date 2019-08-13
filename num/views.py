from django.shortcuts import render

# Create your views here.
def push(request):
    return render(request, 'num/push.html')

def pull(request):
    numbers=request.GET.get('numbers')
    context = {
        'numbers': numbers,
    }
    return render(request, 'num/pull.html', context)

