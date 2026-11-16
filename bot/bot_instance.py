from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from bot.config_reader import config

bot = Bot(
    token=config.BOT_TOKEN.get_secret_value(),
    default=DefaultBotProperties(
        parse_mode=ParseMode.HTML,
        link_preview_is_disabled=True,
    ),
)


async def init_bot_info() -> None:
    """Fetch bot info via getMe once at startup; aiogram caches it on the Bot instance."""
    await bot.me()


def get_bot_username() -> str:
    """Bot username resolved from Telegram (requires init_bot_info() to have been awaited)."""
    if bot._me is None:
        raise RuntimeError("Bot info is not loaded yet, call init_bot_info() on startup")
    return bot._me.username


def get_wishlist_link(hashcode: str) -> str:
    return f"t.me/{get_bot_username()}?start=wl_{hashcode}"
