from django.shortcuts import render
import requests


def exchange(request):
    response = requests.get(url="https://v6.exchangerate-api.com/v6/8bf336b17b6a4ca5e1e1cd1b/latest/USD").json()
    currencies = response.get('conversion_rates')
    if request.method == 'GET':
        context = {
            'current': currencies
        }
        return render(request, 'exchange_app/index.html', context)
    if request.method == 'POST':
        from_amount = float(request.POST.get('from-amount'))
        from_curr = request.POST.get('from-curr')
        to_curr = request.POST.get('to-curr')
        converted_amount = round((currencies[to_curr] / currencies[from_curr]) * float(from_amount), 2)
        context = {
            'current': currencies,
            'from_curr': from_curr,
            'to_curr': to_curr,

            'converted_amount': converted_amount
        }
        return render(request, 'exchange_app/index.html', context)