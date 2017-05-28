import re

from telegram.ext import CommandHandler, InlineQueryHandler, MessageHandler, \
    Filters

from apps.domochat.models import Chat, Order


def start(bot, update):
    update.reply_message(
        _("Привет, я ваш ДомоЧатец, и я заставлю ТСЖ работать быстрее.\n"))


def hello(bot, update):
    update.message.reply_text(
        'Привет, {}! Расскажите, что вас беспокоит'.format(
            update.message.from_user.first_name))


def order(bot, update, args):
    order_text = ' '.join(args)
    update.message.reply_text(
        'Текст заявки: {}'.format(order_text))


order_re = re.compile('^Заявка:.+', re.IGNORECASE)
problem_re = re.compile('^Проблема:.+', re.IGNORECASE)
should_do_re = re.compile('^(Нужно|Надо) (сделать|починить|отремонтировать)',
                          re.IGNORECASE)


def create_order(bot, update):
    msg_text = update.message.text
    regexps_to_check = (order_re, problem_re, should_do_re)
    for regexp in regexps_to_check:
        if regexp.match(msg_text):
            chat, created = Chat.objects.get_or_create(
                telegram_chat_id=update.message.chat.id,
            )
            chat.title = update.message.chat.title
            chat.save()
            new_order = Order.objects.create(
                chat=chat,
                text=update.message
            )
            update.message.reply_text(
                "Спасибо за уведомление! Оформили заявочку "
                "по вашему запросу, скоро решим проблемку.", quote=True
            )
            return


start_handler = CommandHandler('start', start)  # TODO ConversationHandler
hello_handler = CommandHandler('hello', hello)  # TODO ConversationHandler
order_handler = MessageHandler(Filters.text, create_order, )

inline_caps_handler = InlineQueryHandler(create_order, )
