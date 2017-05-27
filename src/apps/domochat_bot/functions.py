from uuid import uuid4

from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import CommandHandler, InlineQueryHandler


def start(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text="Привет, я ваш ДомоЧатец, и я заставлю ТСЖ работать быстрее.")


def hello(bot, update):
    update.message.reply_text(
        'Привет, {}'.format(update.message.from_user.first_name))


def order(bot, update, args):
    order_text = ' '.join(args)
    update.message.reply_text(
        'Текст заявки: {}'.format(order_text))


def inline_write_new_order(bot, update):
    query = update.inline_query.query
    if not query:
        return
    results = [
        InlineQueryResultArticle(
            id=uuid4(),
            title='Заявка',
            input_message_content=InputTextMessageContent(
                'Заявка: {}'.format(query))
        ),
        InlineQueryResultArticle(
            id=uuid4(),
            title='Жалоба',
            input_message_content=InputTextMessageContent(
                'Жалоба: {}'.format(query))
        ),
    ]
    bot.answer_inline_query(update.inline_query.id, results)


start_handler = CommandHandler('start', start)
hello_handler = CommandHandler('hello', hello)
order_handler = CommandHandler('order', order, pass_args=True)
inline_caps_handler = InlineQueryHandler(inline_write_new_order, )
