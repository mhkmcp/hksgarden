from django.shortcuts import render
from .forms import PizzaForm, PizzaModelForm


def home(request):
    context = {}
    return render(request, 'pizza/home.html', context)


def order(request):
    if request.method == 'POST':
        # filled_form = PizzaModelForm(request.POST, request.FILES)   # for image input
        filled_form = PizzaModelForm(request.POST)
        if filled_form.is_valid():
            note = 'Thanks for Ordering! Your %s %s and %s Pizza is on its way :) ' %(
                filled_form.cleaned_data.get('size'),
                filled_form.cleaned_data.get('topping1'),
                filled_form.cleaned_data.get('topping2')
            )
            pizza_form = PizzaModelForm()
            context = {
                'pizza_form': pizza_form,
                'note': note
            }
            # return render(request, 'pizza/order.html', context)

    else:
        pizza_form = PizzaModelForm()
        context = {
            'pizza_form': pizza_form
        }
    return render(request, 'pizza/order.html', context)

