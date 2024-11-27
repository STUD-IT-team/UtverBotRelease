from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

yes_no_text = ["Да", "Нет"]
def make_yes_no_kb():
    kb = [
        [
            KeyboardButton(text=yes_no_text[0])
        ],
        [
            KeyboardButton(text=yes_no_text[1])
        ],
    ]

    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Здесь был IT"
    )

    return keyboard
