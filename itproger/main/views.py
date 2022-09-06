from django.shortcuts import render


def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['hello', 'tort'],
        'obj': {
            'car': 'BMW',
            'age': 28,
            'hobby': 'test'
        }
    }
    return render(request, 'main/main.html', data)


def about(request):
    return render(request, 'main/about.html')
