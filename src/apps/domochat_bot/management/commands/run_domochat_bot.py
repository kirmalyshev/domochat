from django.core.management.base import BaseCommand

from apps.domochat_bot.main import domochat_updater


class Command(BaseCommand):
    """
    Запускаем ДомоЧатец бота
    """

    def handle(self, *args, **options):
        domochat_updater.start_polling()
