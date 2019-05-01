from django.apps import AppConfig


class FundraiserConfig(AppConfig):
    name = 'fundraiser'

    def ready(self):
        # import signal handlers
        import fundraiser.signals

