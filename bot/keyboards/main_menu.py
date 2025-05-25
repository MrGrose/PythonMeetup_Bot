from telegram import ReplyKeyboardMarkup


def get_main_menu_keyboard(is_speaker=False):
    """
    Возвращает основное меню.
    Для спикера добавляет отдельный ряд с кнопками функций спикера.
    """
    buttons = [
        ["📋 Программа", "❓ Задать вопрос"],
        ["🤝 Познакомиться", "💰 Донат"],
        ["🔔 Подписка", "🎤 Стать спикером"],
    ]
    if is_speaker:
        buttons.append(["📋 Выступаю", "Вопросы", "Выступил"])
    return ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=False)
