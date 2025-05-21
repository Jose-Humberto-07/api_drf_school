from django.shortcuts import render
from django.http import JsonResponse


def estudantes(request):
    if request.method == 'GET':
        estudante = {
            'id': '1',
            'nome': 'Humberto',
            'idade': 27,
            'profissao': 'Analista de Sistema'
        }
        return JsonResponse(estudante)
