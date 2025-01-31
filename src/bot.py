import sys, logging, asyncio
from aiogram import Bot, Dispatcher, Router, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, ReplyKeyboardRemove, FSInputFile
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage

from config import get_token
from keyboards import *
from gsheets import *
from consts import *

bot = Bot(token=get_token(), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage())
router = Router()

dp.include_router(router)


# BOT --------------------------------------------------------------------

class UserStates(StatesGroup):
    What = State()
    Print = State()
    Link = State()

@router.message(Command("status"))
async def command_send_handler(message: Message, state: FSMContext):
    await message.answer(text=status_text, reply_markup=ReplyKeyboardRemove())
    await state.clear()


@router.message(Command("send"))
async def command_send_handler(message: Message, state: FSMContext):
    await message.answer(text=what_text, reply_markup=ReplyKeyboardRemove())
    await state.set_state(UserStates.What)

@router.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext):
    await message.answer(text=start_text, reply_markup=ReplyKeyboardRemove())
    await state.clear()

@router.message(UserStates.What)
async def what_handler(message: Message, state: FSMContext):
    await state.update_data(what=message.text)
    await message.answer(text=print_text, reply_markup=make_yes_no_kb())
    await state.set_state(UserStates.Print)


@router.message(UserStates.Print, F.text.in_(yes_no_text))
async def print_handler(message: Message, state: FSMContext):
    await state.update_data(print=(message.text == yes_no_text[0]))
    await message.answer(text=link_text, reply_markup=ReplyKeyboardRemove())
    await state.set_state(UserStates.Link)

@router.message(UserStates.Print)
async def print_handler(message: Message, state: FSMContext):
    await message.answer(text=error)

@router.message(UserStates.Link)
async def link_handler(message: Message, state: FSMContext):
    if not message.text.startswith(yd_url):
        await message.answer(text=error)
    else:
        data = await state.get_data()
        what = data.get("what", None)
        print_ = data.get("print", None)
        if what is None or print_ is None:
            await message.answer(text=error)
            return
        link = message.text
        add_to_gsheets("@"+message.chat.username, what, print_, link)
        await message.answer(text=sent_text)
        await state.clear()

@router.message()
async def unknown_command(message: Message):
    await message.answer(text=start_text)


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
