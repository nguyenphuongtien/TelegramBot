import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
import json
import requests
import time
import os
import datetime

# ID group telegram
LIST_GROUP_ACCESS = [-4572602252, 7988356940]

async def start(update, context):
    if command == '/start':
        await update.message.reply_text("Hell world")
        return

if __name__ == '__main__':
    application = ApplicationBuilder().token('7988356940:AAF5FnQt3smGbjCihh3VNgAsakhM-tVU9vM').read_timeout(10).write_timeout(10).get_updates_http_version('1.1').http_version('1.1').build()

    application.add_handler(CommandHandler('start', start))

    application.run_polling()