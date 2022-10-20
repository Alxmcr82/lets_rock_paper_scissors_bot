import os
import random

from dotenv import load_dotenv
from telegram import ReplyKeyboardMarkup
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

load_dotenv()
token = os.getenv('TOKEN')

r_p_s = ['Камень', 'Бумага', 'Ножницы']


def battle(update, context):

    global r_p_s
    bot_action = random.choice(r_p_s)

    chat = update.effective_chat
    user_action = update.message.text
    name = update.message.chat.first_name

    context.bot.send_message(
            chat_id=chat.id,
            text=f'Бот выбрал {bot_action}, вы выбрали {user_action}')

    if bot_action == user_action:
        context.bot.send_message(
            chat_id=chat.id,
            text='Ничья!')

    elif user_action == 'Камень':
        if bot_action == 'Ножницы':
            context.bot.send_message(
                chat_id=chat.id,
                text='Камень бьет ножницы! Вы победили!')
        else:
            context.bot.send_message(
                chat_id=chat.id,
                text='Бумага оборачивает камень! Вы проиграли.')

    elif user_action == 'Бумага':
        if bot_action == 'Камень':
            context.bot.send_message(
                chat_id=chat.id,
                text='Бумага оборачивает камень! Вы победили!')
        else:
            context.bot.send_message(
                chat_id=chat.id,
                text='Ножницы разрещали бумагу! Вы проиграли.')

    elif user_action == 'Ножницы':
        if bot_action == 'Бумага':
            context.bot.send_message(
                chat_id=chat.id,
                text='Ножницы разрезали бумагу! Вы победили!')
        else:
            context.bot.send_message(
                chat_id=chat.id,
                text='Камень бьет ножницы! Вы проиграли.')

    context.bot.send_message(
            chat_id=chat.id,
            text=f'Сыграем еще, {name}? Выбирай!')


def wake_up(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    buttons = ReplyKeyboardMarkup([
        ['Камень'],
        ['Ножницы'],
        ['Бумага']
        ], resize_keyboard=True)

    context.bot.send_message(
        chat_id=chat.id,
        text=(f'Спасибо, что включил меня, {name}!'
              ' Давай сыраем в Камень Ножницы Бумага, делай выбор!'
              ),
        reply_markup=buttons
        )


def main():
    updater = Updater(token)
    updater.dispatcher.add_handler(CommandHandler('start', wake_up))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, battle))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
