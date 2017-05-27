import logging

from django.conf import settings
from telegram.ext import Updater

from apps.domochat_bot.functions import (
    start_handler,
    hello_handler,
    order_handler,
    inline_caps_handler)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG)

domochat_updater = Updater(token=settings.TELEGRAM_BOT_TOKEN)
dp = domochat_updater.dispatcher

# dp.add_handler(start_handler)
# dp.add_handler(hello_handler)
# dp.add_handler(order_handler)
dp.add_handler(inline_caps_handler)
