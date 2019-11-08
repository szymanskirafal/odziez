from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "odziez.users"
    verbose_name = _("Użytkownicy")

    def ready(self):
        try:
            import odziez.users.signals  # noqa F401
        except ImportError:
            pass
