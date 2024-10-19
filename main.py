import os
from dotenv import load_dotenv
import speedtest
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from pymongo import MongoClient

# Load .env file
load_dotenv()
TOKEN = os.getenv('TELEGRAM_TOKEN')
GROUP_CHAT_ID = os.getenv('GROUP_CHAT_ID')
CHAT_ID = os.getenv('CHAT_ID')
MONGODB_URI = os.getenv('MONGODB_URI')  # URI MongoDB dari .env

# Koneksi ke MongoDB
client = MongoClient(MONGODB_URI)
db = client.telegram_bot
users_collection = db.users

async def check_subscription(update: Update, context: ContextTypes.DEFAULT_TYPE) -> bool:
    user_id = update.message.from_user.id
    try:
        member = await context.bot.get_chat_member(CHAT_ID, user_id)
        print(f"User ID: {user_id}, Member Status: {member.status}")
        return member.status in ['member', 'administrator', 'creator']
    except Exception as e:
        print(f"Error checking subscription: {e}")
        return False

def is_user_registered(user_id: int) -> bool:
    return users_collection.find_one({"user_id": user_id}) is not None

def register_user(user_id: int, user_first_name: str) -> None:
    users_collection.insert_one({"user_id": user_id, "first_name": user_first_name})

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_first_name = update.message.from_user.first_name
    await update.message.reply_text(f'Selamat datang, {user_first_name}! Gunakan /test untuk menguji kecepatan internetmu.')

async def test_speed(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_first_name = update.message.from_user.first_name
    user_id = update.message.from_user.id
    
    # Check subscription status
    if not await check_subscription(update, context):
        keyboard = [[InlineKeyboardButton("Masuk Dulu👀", url='https://t.me/hanyachkecil')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text(
            'Anda harus bergabung kembali dengan channel kami untuk menggunakan bot ini.\n'
            'Silakan bergabung terlebih dahulu:',
            reply_markup=reply_markup
        )
        return

    # Register user if not already registered
    if not is_user_registered(user_id):
        register_user(user_id, user_first_name)
        await context.bot.send_message(
            chat_id=GROUP_CHAT_ID,
            text=f'{user_first_name} telah bergabung dengan channel.'
        )

    await update.message.reply_text('Mengukur kecepatan...🚀')

    # Speed test
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    upload_speed = st.upload() / 1_000_000      # Convert to Mbps
    ping = st.results.ping

    result_message = (
        f'𝗞𝗲𝗰𝗲𝗽𝗮𝗻 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱-𝗠𝘂: {download_speed:.2f} Mbps\n'
        f'𝗞𝗲𝗰𝗲𝗽𝗮𝗻 𝗨𝗽𝗹𝗼𝗮𝗱-𝗠𝘂: {upload_speed:.2f} Mbps\n'
        f'𝗣𝗶𝗻𝗴: {ping} ms'
    )

    keyboard = [[InlineKeyboardButton("𝗦𝘂𝗽𝗽𝗼𝗿𝘁🫱🏼‍🫲🏼", url='https://t.me/fonzyhere')]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(result_message, reply_markup=reply_markup)

def main() -> None:
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("test", test_speed))

    print("ʙoᴛ ʙᴇʀᴊᴀʟᴀɴ...🔥")  # Log di konsol
    app.run_polling()

if __name__ == '__main__':
    main()
