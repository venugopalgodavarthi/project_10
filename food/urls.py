from django.urls import path
from food.views import *
app_name = "food"
urlpatterns = [
    path(route='album/', view=album_view, name="album"),
    path(route='item_create/', view=create_item_view, name="items_create"),
    path(route='item_update/<int:pk>/',
         view=update_item_view, name="item_update"),
    path(route='item_delete/<int:pk>/',
         view=delete_item_view, name="item_delete"),

    path(route='food_create/', view=create_food_view, name="food_create"),
    path(route='food_list/', view=list_food_view, name="food_list"),
    path(route='food_update/<int:pk>/',
         view=update_food_view, name="food_update"),
    path(route='food_delete/<int:pk>/',
         view=delete_food_view, name="food_delete"),

    path(route='cart_add/<int:cust>/<int:food>/',
         view=cart_add, name="cart_add"),
    path(route='cart_list/',
         view=cart_list, name="cart_list"),
    path(route='remove_food/<int:pk>/',
         view=remove_food, name="remove_food"),

    path(route='checkout_food/',
         view=checkout_food, name="checkout_food"),


]
