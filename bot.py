import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiohttp import web # Render o'chirib qo'ymasligi uchun veb-server

# BotFather bergan tokeningizni shu yerga qo'ying
TOKEN = "O'ZINGIZNING_TOKENINGIZNI_QO'YING"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# 1. /start buyrug'i bosilganda
@dp.message(CommandStart())
async def start_tizimi(message: types.Message):
    await message.answer("Salom! Men Samandarning yordamchisiman. U hozir band, nima deb qo'yay?")

# 2. Kelgan xabarlarga sizning o'rningizga javob berish
@dp.message()
async def chat_bot_miya(message: types.Message):
    matn = message.text.lower()

    if "salom" in matn or "assalomu alaykum" in matn or "qaleysiz" in matn:
        await message.answer("Va alaykum assalom! Samandar hozir band edi. Agar muhim gap bo'lsa, yozib qoldiring, ko'rgan zahoti aloqaga chiqadi. 👍")
    elif "nima qilyapsiz" in matn or "ishlar qanaqa" in matn:
        await message.answer("Rahmat, hammasi yaxshi! Hozirda yangi loyihalar va darslar bilan band. O'zingizda nima gaplar?")
    elif "rahmat" in matn or "sog' bo'ling" in matn:
        await message.answer("Arziydi! Salomat bo'ling. 🤝")
    elif "xayr" in matn or "ko'rishguncha" in matn:
        await message.answer("Xayr, sog' bo'ling! Yaxshi kun.")
    else:
        await message.answer("Xabaringizni qabul qildim. Samandar bo'shashi bilan buni o'qiydi va sizga javob beradi. Ungacha kuting. ⏳")

# Render uchun soxta veb-sahifa funksiyasi
async def handle(request):
    return web.Response(text="Bot ishlamoqda...")

async def main():
    # 1. Veb-serverni sozlash va ishga tushirish (Render talabi uchun)
    app = web.Application()
    app.router.add_get('/', handle)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', 10000) # Render kutadigan standart port
    asyncio.create_task(site.start())

    print("Sizning o'rinbosaringiz (Chat-bot) ishga tushdi...")
    
    # 2. Botni ishga tushirish
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())