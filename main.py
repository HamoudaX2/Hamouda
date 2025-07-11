from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, BotCommand
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = '7791741484:AAHlwgYznnvRn8vRUtFIpHKipvlNycsnsic'

# ✅ محفظة USDT
USDT_WALLET = "TMCHvjPEpHL1uXw6NrWur6dLWWb2KLjvGs"

# ✅ روابط الصور + وصف منسق
GUIDE_CONTENT = [
    {
        "url": "https://j.top4top.io/p_347436fga2.jpg",
        "caption": "__⚡ Bot Update Finished - Weekly Plan 60% Off Ends Soon, Get Your Plan Today ⚡__\n\n_Contact us for more details:_ [@ThunderFlashOfficialchat_BOT](https://t.me/ThunderFlashOfficialchat_BOT)\n\n_BOT LINK:_ [@ThunderFlashOfficial_BOT](https://t.me/ThunderFlashOfficial_BOT)"
    },
    {
        "url": "https://h.top4top.io/p_347432ydk0.jpg",
        "caption": "__⚡ Bot Update Finished - ⚡__\n\n_🔴 Need Any Help With Thunder Flash Bot, Contact Us:_ [@ThunderFlashOfficialchat_BOT](https://t.me/ThunderFlashOfficialchat_BOT)\n\n_BOT LINK:_ [@ThunderFlashOfficial_BOT](https://t.me/ThunderFlashOfficial_BOT)"
    },
    {
        "url": "https://i.top4top.io/p_3474uz7nr1.jpg",
        "caption": "__⚡ Bot Update Finished - Trust Wallet Token Staying Time Extended For 200 Days ⚡__\n\n_Contact us for more details:_ [@ThunderFlashOfficialchat_BOT](https://t.me/ThunderFlashOfficialchat_BOT)\n\n_BOT LINK:_ [@ThunderFlashOfficial_BOT](https://t.me/ThunderFlashOfficial_BOT)"
    }
]

# ✅ رسالة الترحيب
WELCOME_MESSAGE = """
⚡️ Welcome to Thunder Flash Bot ⚡️

This bot you can send flash tokens on Ethereum, BNB, Fantom, BTC, Polygon, SOL network with any desired amount, which are real and all of the transactions are visible on Etherscan, bscscan, Blockchain & etc. Those tokens will be displayed on the balances of wallets that show confirmed transactions, such as Exodus, Trust wallet, Meta mask, Phantom, Bitget And More Wallet.

Supported tokens:
— USDT
— USDC
— ETH
— DAI
— Fantom
— SHIBA INU
— ChainLink
— Pepe
— Cronos
— Uniswap
— SOL

🚀 Use send to make a transaction.
💎 If you don't have an active plan, use purchase to get the prices and buy a suggested one.

⁉️ Still got any questions? Contact @ThunderFlashOfficialchat_BOT

🔗 Bot Link
@ThunderFlashOfficial_BOT

-------------------------------------------------------

❗ Notice for new users
We are not responsible for any illegal Activities if you Doing using this service.
"""

# ✅ قالب الطلب
ORDER_TEMPLATE = """
📌 *Created a New Order*

*Price:* _{price}_
*Plan:* _{plan} 💎_

*Send Payment to this USDT Wallet:*
`{link}`

⚠️ _Your plan will activate automatically after the transaction is confirmed._

🕐 _Invoice expires in 1 hour._
"""

# ✅ الخطط
PLANS = {
    "Daily": {
        "price": "25$ 💎",
        "link": USDT_WALLET
    },
    "Weekly": {
        "price": "30$ 💎",
        "link": USDT_WALLET
    },
    "Monthly": {
        "price": "350$ 💎",
        "link": USDT_WALLET
    },
    "Lifetime": {
        "price": "500$ 💎",
        "link": USDT_WALLET
    }
}

# ✅ لوحة التحكم الرئيسية
main_menu_keyboard = InlineKeyboardMarkup([
    [InlineKeyboardButton("🚀 Send Transaction", callback_data='send')],
    [InlineKeyboardButton("💎 Purchase A Plan", callback_data='purchase')],
    [InlineKeyboardButton("📩 Import Custom Wallet", callback_data='import')],
    [
        InlineKeyboardButton("✅ Profile", callback_data='profile'),
        InlineKeyboardButton("🔐 Revert Transaction", callback_data='revert')
    ],
    [InlineKeyboardButton("📘 Guide", callback_data='guide')]
])

# ✅ لوحة رجوع وخروج ثابتة
back_main_keyboard = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("⬅️ Back", callback_data='back_menu'),
        InlineKeyboardButton("🏠 Main Menu", callback_data='main_menu')
    ]
])
                                                           # ✅ لوحة الشراء
purchase_menu_keyboard = InlineKeyboardMarkup([
    [                                                              InlineKeyboardButton("🗓️ Daily", callback_data='plan_daily'),                                                          InlineKeyboardButton("🗓️ Weekly", callback_data='plan_weekly'),
        InlineKeyboardButton("🗓️ Monthly", callback_data='plan_monthly')                                                   ],                                                         [InlineKeyboardButton("🗓️ Lifetime", callback_data='plan_lifetime')],                                                  [
        InlineKeyboardButton("⬅️ Back", callback_data='back_menu'),
        InlineKeyboardButton("🏠 Main Menu", callback_data='main_menu')                                                   ]
])

# ✅ /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(                               WELCOME_MESSAGE,
        reply_markup=main_menu_keyboard
    )

# ✅ /guide
async def guide(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    for item in GUIDE_CONTENT:
        try:
            await context.bot.send_photo(chat_id=chat_id, photo=item["url"])
        except Exception:
            await context.bot.send_message(chat_id=chat_id, text=f"⚠️ Couldn't load image from: {item['url']}")
        await context.bot.send_message(
            chat_id=chat_id,
            text=item["caption"],
            parse_mode='Markdown',
            reply_markup=back_main_keyboard
        )

# ✅ التعامل مع الأزرار
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query                              await query.answer()
    user_id = query.from_user.id                               data = query.data

    if data in ["revert", "import"]:
        await query.message.reply_text(                                "❗ You don't have permission to access this feature.",
            reply_markup=back_main_keyboard                        )

    elif data == "profile":
        await query.message.reply_text(
            f"❗ You don't have any active plan.\n\n"                  "• Click 💎 *Purchase Plan* to buy a plan.\n\n"
            f"User ID: `{user_id}`",
            parse_mode='Markdown',
            reply_markup=back_main_keyboard
        )

    elif data == "send":                                           await query.message.reply_text(
            "❗ You don't have any active plan.\n\n"
            "• Click 💎 *Purchase Plan* to buy a plan.",
            parse_mode='Markdown',
            reply_markup=back_main_keyboard
        )

    elif data == "purchase":
        await query.message.reply_text(
            "*💎 Choose Your Plan:*",
            parse_mode='Markdown',
            reply_markup=purchase_menu_keyboard
        )

    elif data in ["plan_daily", "plan_weekly", "plan_monthly", "plan_lifetime"]:
        plan_key = data.split("_")[1].capitalize()
        plan_info = PLANS.get(plan_key)
        if plan_info:
            price = plan_info["price"]
            link = plan_info["link"]
            await query.message.reply_text(
                ORDER_TEMPLATE.format(plan=plan_key, price=price, link=link),
                parse_mode='Markdown',
                disable_web_page_preview=True,
                reply_markup=back_main_keyboard
            )

    elif data in ["back_menu", "main_menu"]:
        await query.message.reply_text(
            WELCOME_MESSAGE,
            reply_markup=main_menu_keyboard
        )

    elif data == "guide":
        await guide(update, context)

# ✅ إعداد الأوامر الرسمية للبوت
async def setup_commands(app):
    await app.bot.set_my_commands([
        BotCommand("start", "📍 Start & Show Main Menu"),
    ])

# ✅ تشغيل البوت
def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("guide", guide))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.post_init = setup_commands
    app.run_polling()

if __name__ == '__main__':
    main()
