from django.shortcuts import render
from .forms import PizzaForm, PizzaModelForm, MultiplePizzaForm
from django.forms import formset_factory
from .models import Pizza


def home(request):
    context = {}
    return render(request, 'pizza/home.html', context)


def order(request):
    multiple_form = MultiplePizzaForm()
    if request.method == 'POST':
        # filled_form = PizzaModelForm(request.POST, request.FILES)   # for image input
        filled_form = PizzaModelForm(request.POST)
        if filled_form.is_valid():
            created_pizza = filled_form.save()
            created_pizza_pk = created_pizza.id
            note = 'Thanks for Ordering! Your %s %s and %s Pizza is on its way :) ' %(
                filled_form.cleaned_data.get('size'),
                filled_form.cleaned_data.get('topping1'),
                filled_form.cleaned_data.get('topping2')
            )
            pizza_form = PizzaModelForm()
            context = {
                'pizza_form': pizza_form,
                'multiple_form': multiple_form,
                'note': note,
                'created_pizza_pk': created_pizza_pk
            }
            return render(request, 'pizza/order.html', context)

    else:
        pizza_form = PizzaModelForm()
        context = {
            'pizza_form': pizza_form,
            'multiple_form': multiple_form,
        }
    return render(request, 'pizza/order.html', context)


def pizzas(request):
    number_of_pizzas = 2
    filled_multiple_pizza_form = MultiplePizzaForm(request.GET)
    if filled_multiple_pizza_form.is_valid():
        number_of_pizzas = filled_multiple_pizza_form.cleaned_data['number']
    
    PizzaFormSet = formset_factory(PizzaModelForm, extra=number_of_pizzas)
    formset = PizzaFormSet()
    if request.method == 'POST':
        filled_formset = PizzaFormSet(request.POST)
        if filled_formset.is_valid():
            for form in filled_formset:
                print(form.cleaned_data['topping1'])
            note = 'Pazzas have been Ordered!'
        else:
            note = 'Order was not created, try again!'
        context = {
            'note': note,
            'formset': formset
        }
        return render(request, 'pizza/pizzas.html', context)

    else:
        context = {
            'formset': formset
        }
        return render(request, 'pizza/pizzas.html', context)


def edit_order(request, pk):
    pizza = Pizza.objects.get(pk=pk)
    form = PizzaModelForm(instance=pizza)
    if request.method == 'POST':
        filled_form = PizzaModelForm(request.POST, instance=pizza)
        if filled_form.is_valid():
            filled_form.save()
            form = filled_form
            context = {
                'form': form,
                'pizza': pizza,
                'note': 'Order has been Updated!'
            }
            return render(request, 'pizza/edit_order.html', context)

    context = {
        'form': form,
        'pizza': pizza
    }
    return render(request, 'pizza/edit_order.html', context)
