from django import template

register = template.Library()

@register.simple_tag(name='subtotal')
def subtotal(cart):
    total = 0
    if cart and cart.added_items.exists():  # Check if cart and cart items exist
        for item in cart.added_items.all():
            if item.product and item.product.price:  # Ensure item.product is not None and has a price
                total += item.quantity * item.product.price
            else:
                # Handle the case where product or product.price is None
                # This could be logging an error or continuing silently
                pass
    return total
