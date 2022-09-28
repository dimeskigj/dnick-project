from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'index.html', {})


def lesson(request, lesson_id: int):
    return render(request, 'lesson.html', {'id': lesson_id, })


def test(request):
    return render(request, 'test.html', {})


def certificate(request):
    return render(request, 'certificate.html', {})
