from django import forms
from food.models import menu_items, food_items, order_food


class menu_items_form(forms.ModelForm):
    class Meta:
        model = menu_items
        fields = '__all__'


class food_items_form(forms.ModelForm):
    class Meta:
        model = food_items
        fields = '__all__'


class order_food_items_form(forms.ModelForm):
    class Meta:
        model = order_food
        exclude = ['cust_id', 'total_price']
