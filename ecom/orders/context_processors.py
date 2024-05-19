# orders/context_processors.py

from django.db.models import Sum
from .models import Order

def cart_count(request):
    if request.user.is_authenticated:
        customer = request.user.customer_profile
        cart = Order.objects.filter(owner=customer, order_status=Order.CART_STAGE).first()
        if cart:
            count = cart.added_items.aggregate(total_quantity=Sum('quantity'))['total_quantity'] or 0
        else:
            count = 0
    else:
        count = 0
    return {
        'cart_count': count
    }
