from aiogram.filters import Filter
from aiogram import types


class CallbackFilter(Filter):
    def __init__(self, command: str):
        self.command = command

    async def __call__(self, call_back: types.CallbackQuery):
        return call_back.data.startswith(f'{self.command}:') or call_back.data == self.command
