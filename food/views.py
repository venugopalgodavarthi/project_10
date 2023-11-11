from django.shortcuts import render, redirect
from food.forms import menu_items_form, food_items_form, order_food_items_form
from food.models import menu_items, food_items, cart_items
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum, Count
# Create your views here.


@login_required(login_url='/authe/login')
def album_view(request):
    res = food_items.objects.all()
    return render(request=request, template_name='album.html', context={'res': res})


@login_required(login_url='/authe/login')
def create_item_view(request):
    res = menu_items.objects.all()
    form = menu_items_form()
    if request.method == 'POST':
        print(request.POST)
        form = menu_items_form(request.POST)
        if form.is_valid:
            form.save()
    if request.method == 'GET':
        res = menu_items.objects.all()
    return render(request=request, template_name='items_create.html', context={'form': form, 'res': res})


@login_required(login_url='/authe/login')
def update_item_view(request, pk):
    res = menu_items.objects.get(mid=pk)
    form = menu_items_form(instance=res)
    if request.method == 'POST':
        res = menu_items.objects.get(mid=pk)
        form = menu_items_form(request.POST, instance=res)
        if form.is_valid:
            form.save()
            return redirect('/food/item_create')
    return render(request=request, template_name='item_update.html', context={'form': form})


@login_required(login_url='/authe/login')
def delete_item_view(request, pk):
    res = menu_items.objects.get(mid=pk)
    if request.method == 'POST':
        res = menu_items.objects.get(mid=pk).delete()
        return redirect('/food/item_create')
    return render(request=request, template_name='item_delete.html', context={'res': res})


@login_required(login_url='/authe/login')
def create_food_view(request):
    form = food_items_form()
    if request.method == 'POST':
        print(request.POST, request.FILES)
        form = food_items_form(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return redirect('/food/food_list')
    return render(request=request, template_name='food_create.html', context={'form': form})


@login_required(login_url='/authe/login')
def list_food_view(request):
    res = food_items.objects.all()
    return render(request=request, template_name='food_list.html', context={'res': res})


@login_required(login_url='/authe/login')
def update_food_view(request, pk):
    res = food_items.objects.get(fid=pk)
    form = food_items_form(instance=res)
    if request.method == 'POST':
        res = food_items.objects.get(fid=pk)
        form = food_items_form(request.POST, request.FILES, instance=res)
        if form.is_valid:
            form.save()
            return redirect('/food/food_list')
    return render(request=request, template_name='food_update.html', context={'form': form})


@login_required(login_url='/authe/login')
def delete_food_view(request, pk):
    res = food_items.objects.get(fid=pk)
    if request.method == 'POST':
        res = food_items.objects.get(fid=pk).delete()
        return redirect('/food/food_list')
    return render(request=request, template_name='food_delete.html', context={'res': res})


@login_required(login_url='/authe/login')
def cart_add(request, cust, food):
    cart_items.objects.create(cust_id=cust, food_id=food)
    messages.success(request, "Item is added")
    return redirect('/food/album')


@login_required(login_url='/authe/login')
def cart_list(request):
    res = cart_items.objects.filter(cust_id=request.user.id)
    food_data = [j[0] for j in res.values_list('food_id', 'cart_id')]
    cart_data = [j[1] for j in res.values_list('food_id', 'cart_id')]
    data = food_items.objects.filter(fid__in=food_data)
    data = [(data[i], cart_data[i]) for i in range(0, len(data))]
    return render(request=request, template_name='cart_list.html', context={'data': data})


@login_required(login_url='/authe/login')
def remove_food(request, pk):
    cart_items.objects.get(cart_id=pk).delete()
    messages.success(request, "food item removed")
    return redirect('/food/cart_list')


@login_required(login_url='/authe/login')
def checkout_food(request):
    res = cart_items.objects.filter(
        cust_id=request.user.id).values_list('food_id')
    print()
    food_data = [food_items.objects.get(fid=i) for i in [i[0] for i in res]]
    print(food_data)
    food_count = [food_items.objects.get(fid=i).f_price for i in [
        i[0] for i in res]]
    print(food_count)
    form = order_food_items_form()
    total_price = sum(food_count)
    data = {'form': form, 'food_data': food_data,
            'f_price__sum': total_price, 'f_price__count': len(food_count)}
    if request.method == 'POST':
        print(request.POST)
        form = order_food_items_form(request.POST)
        if form.is_valid:
            user = form.save(commit=False)
            user.cust_id = request.user.id
            user.total_price = total_price
            if True:
                user.save()
                messages.success(request, "booking success")
                return redirect('/food/album')
    return render(request=request, template_name='checkout.html', context=data)
