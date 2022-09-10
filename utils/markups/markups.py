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


def get_professor_mainMenu() -> ReplyKeyboardMarkup:
    """
    Возвращает основную клавиатуру, с клавишами:
        Добавить задание, Просмотреть добавленные задания
    """
    button_addTask = InlineKeyboardButton(text='Добавить задание')
    button_viewTasks = InlineKeyboardButton(text='Просмотреть добавленные задания')
    ReplyKeyboardMarkup_professor = InlineKeyboardMarkup().add(button_addTask, button_viewTasks)

    return ReplyKeyboardMarkup_professor


def get_ADMIN_mainMenu() -> ReplyKeyboardMarkup:
    """
        Возвращает основную клавиатуру, с клавишами:

        """
    pass