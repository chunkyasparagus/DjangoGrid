from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import Person, Bond

from itertools import count
from collections import OrderedDict


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
            try:
                v = Bond.objects.get(bonder__id=bonder.id, bondee__id=bondee.id).bond_level
            except ObjectDoesNotExist:
                new_object = Bond(bonder=bonder, bondee=bondee)
                new_object.save()
                v = new_object.bond_level
            new_row.append({'class': 'c', 'isdata': True, 'datavalue': f'{v}', 'dataname': f'griddata_{next(datan)}'})
        context['rows'].append(new_row)

    return render(request, 'grid.html', context)


def updategrid(request):
    raw_grid_data = {int(key.split('_')[1]): data for key, data in request.POST.items() if key.startswith('griddata_')}
    grid_data = list(OrderedDict(sorted(raw_grid_data.items())).values())
    everyone = Person.objects.all()
    for bonder in everyone:
        for bondee in everyone:
            v = grid_data.pop(0)
            bond_obj = Bond.objects.get(bonder__id=bonder.id, bondee__id=bondee.id)
            if v != bond_obj.bond_level:
                bond_obj.bond_level = v
                bond_obj.save()

    return redirect('viewgrid')
