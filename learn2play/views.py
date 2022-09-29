from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'index.html', {})


def lesson(request, lesson_id: int):
    return render(request, 'lesson.html', {'id': lesson_id, })


def test(request):
    return render(request, 'test.html', {})


def certificate(request):
    if request.GET.get('22exampleRadios', '') is '' or request.GET.get('22exampleRadios', '') is '' or request.GET.get(
            '22exampleRadios', '') is '' or request.GET.get('text', '') is '':
        return render(request, 'fail.html', {})
    return render(request, 'certificate.html', {})


def fail(request):
    return render(request, 'fail.html', {})


def song(request, song_name: str, artist_name: str):
    return render(request, 'song.html', {'song_name': song_name, 'artist_name': artist_name})


def results(request):
    return render(request, 'search-results.html', {
        'query': 'Some Song' if request.GET.get('query', 'Some Song') == '' else request.GET.get('query', 'Some Song'),
        'songs': [{
            'song_name': 'I go',
            'artist_name': 'Peggy Gou'
        }, {
            'song_name': 'empire ants',
            'artist_name': 'gorillaz'
        }, {
            'song_name': 'carnival of rust',
            'artist_name': 'poets of the fall'
        }, {
            'song_name': 'du hast',
            'artist_name': 'rammstein'
        }, {
            'song_name': 'as it was',
            'artist_name': 'harry styles'
        },
        ]
    })
