from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


def get_mainMenu() -> ReplyKeyboardMarkup:
    """
    Возвращает основную клавиатуру, с клавишами:
        Студент, Учитель, Админ
    """
    button_student = InlineKeyboardButton(text='Студент')
    button_professor = InlineKeyboardButton(text='Учитель')
    button_ADMIN = InlineKeyboardButton(text='Админ')
    ReplyKeyboardMarkup_main = InlineKeyboardMarkup().add(button_student, button_professor, button_ADMIN)

    return ReplyKeyboardMarkup_main


def get_student_mainMenu() -> ReplyKeyboardMarkup:
    """
    Возвращает основную клавиатуру, с клавишами:
        Расписание, Задание
    """
    button_schedule = InlineKeyboardButton(text='Расписание')
    button_tasks = InlineKeyboardButton(text='Задания')
    ReplyKeyboardMarkup_student_1 = InlineKeyboardMarkup().add(button_schedule, button_tasks)

    return ReplyKeyboardMarkup_student_1


def get_student_mainMenu() -> ReplyKeyboardMarkup:
    """
    Возвращает основную клавиатуру, с клавишами:
        Расписание, Задание
    """
    button_NextClass = InlineKeyboardButton(text='Следующее занятие')
    button_Tommorow = InlineKeyboardButton(text='Завтра')
    button_Week = InlineKeyboardButton(text='Неделя')
    button_All = InlineKeyboardButton(text='Все')
    ReplyKeyboardMarkup_student_2 = InlineKeyboardMarkup().add(button_NextClass, button_Tommorow, button_Week, button_All)

    return ReplyKeyboardMarkup_student_2


def get_professor_mainMenu() -> ReplyKeyboardMarkup:
    """
    Возвращает основную клавиатуру, с клавишами:
        Добавить задание, Просмотреть добавленные задания
    """
    button_addTask = InlineKeyboardButton(text='Добавить задание')
    button_viewTasks = InlineKeyboardButton(text='Просмотреть добавленные задания')
    ReplyKeyboardMarkup_professor_1 = InlineKeyboardMarkup().add(button_addTask, button_viewTasks)

    return ReplyKeyboardMarkup_professor_1


def get_ADMIN_mainMenu() -> ReplyKeyboardMarkup:
    """
        Возвращает основную клавиатуру, с клавишами:

        """
    pass