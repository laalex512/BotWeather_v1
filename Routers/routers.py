from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.filters import CommandStart
from Keyboards.keyboards import create_buttons_markup, create_buttons_builder
from Lexicon.lexicon_ru import LEXICON_MENU
from main import logger
from python_weather import Locale
import python_weather

router = Router()

start_keyboard = create_buttons_builder(2, **LEXICON_MENU)
start_keyboard2 = create_buttons_markup(**LEXICON_MENU)


@router.message(CommandStart())
async def process_start_comand(message: Message):
    await message.answer('Hi', reply_markup=start_keyboard2)

# @router.message(F.text == LEXICON_MENU['1'])
# async def button1(message: Message):
#     await message.answer("You press button 1", reply_markup=start_keyboard2)


@router.message()
async def echo(message: Message):
    try:
        city = message.text
        async with python_weather.Client(unit=python_weather.METRIC, locale=Locale.RUSSIAN) as client:
            weather = await client.get(city)

            resp_msg = f'{weather.nearest_area}\n'
            resp_msg += f'{weather.current.temperature}°C\n'
            resp_msg += f'{weather.current.description}\n'
            resp_msg += f'Ощущается: {weather.current.feels_like}C\n\nПрогноз:\n'

            for forecast in weather.forecasts:
                resp_msg += f'{forecast.date}:\n{forecast.lowest_temperature}°C - {forecast.highest_temperature}°C\n'
            logger.info(f'{message.from_user.full_name} asked: {city}\n'
                         f'Answer:\n{resp_msg}')
            await message.answer(resp_msg)

    except TypeError:
        await message.answer("Nice try!")


