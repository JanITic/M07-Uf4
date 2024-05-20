from django.shortcuts import render


def students(request):
    students_data = [
        {"nom": "Ana", "cognom1": "Rodríguez", "cognom2": "Méndez", "correu": "ana@example.com", "curs": "DAM", "mòduls_matriculats": ["M01", "M02"]},
        {"nom": "Luis", "cognom1": "Pérez", "cognom2": "González", "correu": "luis@example.com", "curs": "DAW", "mòduls_matriculats": ["M03", "M04"]},
        {"nom": "Carla", "cognom1": "Fernández", "cognom2": "Martínez", "correu": "carla@example.com", "curs": "DAM", "mòduls_matriculats": ["M02", "M03"]},
        {"nom": "Jorge", "cognom1": "Sánchez", "cognom2": "López", "correu": "jorge@example.com", "curs": "DAW", "mòduls_matriculats": ["M01", "M04"]},
        {"nom": "Marta", "cognom1": "García", "cognom2": "Ruiz", "correu": "marta@example.com", "curs": "DAM", "mòduls_matriculats": ["M01", "M03"]}
    ]
    return render(request, 'student.html', {"data": students_data})

def teachers(request):
    teachers_data = [
        {"nom": "Pablo", "cognom1": "Gómez", "cognom2": "Sanz", "correu": "pablo@example.com", "curs": "DAM", "tutor": "M01", "mòduls_impartits": ["M01", "M02"]},
        {"nom": "Elena", "cognom1": "Martínez", "cognom2": "Gómez", "correu": "elena@example.com", "curs": "DAW", "tutor": "M02", "mòduls_impartits": ["M03", "M04"]},
        {"nom": "Alberto", "cognom1": "López", "cognom2": "García", "correu": "alberto@example.com", "curs": "DAM", "tutor": "M03", "mòduls_impartits": ["M02", "M03"]},
        {"nom": "Sonia", "cognom1": "Fernández", "cognom2": "Pérez", "correu": "sonia@example.com", "curs": "DAW", "tutor": "M04", "mòduls_impartits": ["M01", "M04"]},
        {"nom": "Raúl", "cognom1": "Serrano", "cognom2": "Vázquez", "correu": "raul@example.com", "curs": "DAM", "tutor": "M01", "mòduls_impartits": ["M01", "M03"]}
    ]
    return render(request, 'teacher.html', {"data": teachers_data})


def index(request):
    return render(request, 'index.html')
