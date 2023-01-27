from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from .constants import SeriesEnum

choose_series_kb = InlineKeyboardMarkup(row_width=2)
buttons_text = {
    "Games Of Thrones": SeriesEnum.game_of_thrones,
    "Breaking Bad": SeriesEnum.breaking_bad,
    "Dark": SeriesEnum.dark,
    "Money Heist": SeriesEnum.money_heist
}
for text, callback_data in buttons_text.items():
    choose_series_kb.insert(InlineKeyboardButton(text, callback_data=callback_data))

menu_kb = ReplyKeyboardMarkup(resize_keyboard=True)
menu_kb.add("Get random quote", "Get random quote from series",
            "Get random quote with image", "Create your quote with random image")
