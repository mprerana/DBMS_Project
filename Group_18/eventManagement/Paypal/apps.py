from django.apps import AppConfig


class PaypalConfig(AppConfig):
    name = 'Paypal'

    def ready(self):
        pass
