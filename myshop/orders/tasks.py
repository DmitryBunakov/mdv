from .models import Order


# @shared_task
def order_created(order_id):

    order = Order.objects.get(id=order_id)
    pass
