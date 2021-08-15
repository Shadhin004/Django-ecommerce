from . models import *

def add_variable_to_context(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()     
        
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_item':0}
    
    
    context = {'items': items, 'order': order, }

    return (context)



