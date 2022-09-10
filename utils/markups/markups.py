from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


def get_student_mainMenu() -> ReplyKeyboardMarkup:
    """
    Возвращает основную клавиатуру, с клавишами:
        Расписание, Задание
    """
    button_schedule = InlineKeyboardButton(text='Расписание')
    button_tasks = InlineKeyboardButton(text='Задания')
    ReplyKeyboardMarkup_student = InlineKeyboardMarkup().add(button_schedule, button_tasks)

    return ReplyKeyboardMarkup_student
