import requests
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from urllib.parse import quote

from main import dp
from utils.constants import API_URL
from utils.keyboards import menu_kb, choose_series_kb

import aiogram

from utils.models import QuoteResponse


class ChooseSeriesState(StatesGroup):
    choose_series = State()
    create_quote = State()


@dp.message_handler(commands=['start'])
async def welcome(message: aiogram.types.Message):
    await message.answer("Bot for getting quotes from several series", reply_markup=menu_kb)


@dp.message_handler(lambda msg: msg.text == "Get random quote")
async def get_random_quote(message: aiogram.types.Message):
    response = requests.get(API_URL + "/quote")
    quote_message = str(QuoteResponse(**response.json()[0]))

    await message.answer(quote_message, parse_mode=aiogram.types.ParseMode.MARKDOWN)


@dp.message_handler(lambda msg: msg.text == "Get random quote from series")
async def get_random_quote_from_series(message: aiogram.types.Message):
    await message.answer("Choose series", reply_markup=choose_series_kb)
    await ChooseSeriesState.choose_series.set()


@dp.callback_query_handler(state=ChooseSeriesState.choose_series)
async def choose_series(callback_query: aiogram.types.CallbackQuery, state: FSMContext):
    series = callback_query.data
    print(series)
    response = requests.get(API_URL + f"/quote?series={series}")
    print(response.json())
    quote_message = str(QuoteResponse(**response.json()[0]))

    await callback_query.message.answer(quote_message, parse_mode=aiogram.types.ParseMode.MARKDOWN)
    await state.finish()


@dp.message_handler(lambda msg: msg.text == "Get random quote with image")
async def get_random_quote_with_image(message: aiogram.types.Message):
    photo = API_URL + '/pic/image?text_size=25&background_img_url=' + quote("https://picsum.photos/600?blur=2")
    await message.answer_photo(photo=photo,
                               caption="Your quote with random image")


@dp.message_handler(lambda msg: msg.text == "Create your quote with random image")
async def create_quote_with_image(message: aiogram.types.Message):
    await message.answer("Send me your quote")
    await ChooseSeriesState.create_quote.set()


@dp.message_handler(state=ChooseSeriesState.create_quote)
async def create_quote(message: aiogram.types.Message, state: FSMContext):
    quote_message = message.text
    photo = API_URL + f'/pic/custom?text={quote(quote_message)}&text_size=25&image_url=' + quote("https://picsum.photos/600?blur=2")
    await message.answer_photo(photo=photo,
                               caption="Your quote with random image")
    await state.finish()