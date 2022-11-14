import input_n
import main
import log

from time import sleep
import logging
from telegram import __version__ as TG_VER
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (Application, CommandHandler, ContextTypes, ConversationHandler, MessageHandler, filters)
 


reply_keyboard_next_action = [["Продожить"],\
                            ["Новый ввод"],\
                            ["Главное меню"],\
                            ["Выход"]]


markup_next_action = ReplyKeyboardMarkup(reply_keyboard_next_action, one_time_keyboard=True)

async def excep_check_zero (update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        input_n.x / input_n.y
        return main.action_menu
    except ZeroDivisionError:
        await update.message.reply_text ('Ошибка! Деление на ноль. Повторите ввод данных')
        log.universal_logger("Деление на 0", data_description = "Ошибка")
        await update.message.reply_text(f'Продолжить вычисления с числами "{input_n.x}" и "{input_n.y}"?\n \
Продожить\nНовый ввод\nГлавное меню\nВыход', reply_markup=markup_next_action)
        return main.next_action
