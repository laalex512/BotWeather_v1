from aiogram import types
from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, ReplyKeyboardMarkup

def create_buttons_builder(width: int = 1, *args: str, **kwargs: str):
    # Initial builder for keyboard
    menu = ReplyKeyboardBuilder()

    # List of buttons
    buttons = []

    if args:
        for button in args:
            buttons.append(KeyboardButton(text=button))

    if kwargs:
        for key, value in kwargs.items():
            buttons.append(KeyboardButton(text=value))

    menu.row(*buttons, width=width)
    return menu.as_markup(resize_keyboard=True,
        input_field_placeholder="Выберите город ниже или введите свой")



def create_buttons_markup(*args: str, **kwargs: str):
    # List of buttons
    buttons = []

    if args:
        for button in args:
            buttons.append(types.KeyboardButton(text=button))

    if kwargs:
        for key, value in kwargs.items():
            buttons.append(types.KeyboardButton(text=value))
    buttons = [buttons]

    menu = types.ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True,
        input_field_placeholder="Выберите город ниже или введите свой"
    )
    return menu
