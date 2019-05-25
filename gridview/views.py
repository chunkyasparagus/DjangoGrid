from django.shortcuts import render
from django.http import HttpResponse
from .models import Person

from itertools import count


def viewgrid(request):
    datan = count(1)
    context = dict()
    context['rows'] = list()
    new_row = list()
    new_row.append({'class': 'tl', 'isdata': False, 'label': 'XO'})
    everyone = Person.objects.all()
    for bondee in everyone:
        new_row.append({'class': 'th', 'isdata': False, 'label': bondee.name})
    context['rows'].append(new_row)

    for bonder in everyone:
        new_row = list()
        new_row.append({'class': 'lh', 'isdata': False, 'label': bonder.name})
        for bondee in everyone:
            new_row.append({'class': 'c', 'isdata': True, 'datavalue': '0', 'dataname': f'griddata{next(datan)}'})
        context['rows'].append(new_row)

    return render(request, 'grid.html', context)


def updategrid(request):
    return HttpResponse('success')
