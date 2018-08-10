from .models import Order
from celery import task
from django.core.mail import send_mail


@task
def order_created(order_id):
    """
    Task to send an e-mail notification when an order is
    successfully created.
    """
    order = Order.objects.get(id=order_id)
    subject = 'Order nr. {}'.format(order.id)
    message = 'Dear {},\n\nYou have successfully placed an order.Your order id is {}.'.format(order.first_name,
                                                                                              order.id)
    mail_send = send_mail(subject, message, 'admin@myshop.com', [order.email])
    return mail_send
