# coding=utf-8

from django import forms
from django.shortcuts import redirect, render_to_response

from primes.models import PrimeNumber

import PrimeNumbers.settings as settings


class PrimeNumberForm(forms.ModelForm):
    """
    Форма для ввода порядкового номера простого числа.
    """
    max_index = settings.MAX_INDEX
    index = forms.IntegerField(min_value=1, max_value=max_index, initial=1,
                               label=u"Порядковый номер")

    class Meta:
        model = PrimeNumber


def index(request):
    """
    Выводит главную страницу.
    """
    return render_to_response('index.html', {'form': PrimeNumberForm()})


def get_prime(request):
    """
    Выводит простое число по заданному порядковому номеру.

    При неверных входных данных отображает главную страницу + сообщение об ошибке.
    """
    if request.POST:
        form = PrimeNumberForm(request.POST)
        if form.is_valid():
            return render_to_response('prime.html', {'prime': form.save(commit=False)})
        else:
            return render_to_response('index.html', {'form': form})
    return redirect('/')


def get_prime_json(request, **kwargs):
    """
    Возвращает информацию о простом числе по заданному порядковому номеру в формате JSON.
    """
    import json
    from django.http import HttpResponse

    form = PrimeNumberForm(kwargs)
    response = {'was_error': False}

    if form.is_valid():
        prime = form.save(commit=False)
        response.update({'index': prime.index,
                         'value': prime.value})
    else:
        response['was_error'] = True
        response['errors'] = form.errors

    return HttpResponse(json.dumps(response, ensure_ascii=False), content_type='application/json')