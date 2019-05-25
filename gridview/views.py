from django.shortcuts import render
from django.http import HttpResponse
from .models import Person


def viewgrid(request):
    context = dict()
    context['rows'] = list()
    new_row = list()
    value = {'value': 'XO'}
    new_row.append(value)
    everyone = Person.objects.all()
    for bondee in everyone:
        new_row.append({'class': 'topheader', 'isdata': False, 'value': bondee.name})
    context['rows'].append(new_row)

    for bonder in everyone:
        new_row = list()
        new_row.append({'class': 'leftheader', 'isdata': False, 'value': bonder.name})
        for bondee in everyone:
            new_row.append({'class': 'gridvalue', 'isdata': True, 'value': '0'})
        context['rows'].append(new_row)

    return render(request, 'grid.html', context)


def updategrid(request):
    return HttpResponse('success')
