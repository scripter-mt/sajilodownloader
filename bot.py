import requests
from telegram import *
from telegram.ext import Updater, CommandHandler, CallbackContext, \
    MessageHandler, Filters


def get_Download_URL_From_API(url):
    API_URL = "https://getvideo.p.rapidapi.com/"
    querystring = {"url": f"{url}"}

    headers = {
        'x-rapidapi-host': "getvideo.p.rapidapi.com",
        'x-rapidapi-key': "f46d0d682dmsh95ed9f4dc7225e2p146570jsn1d8f86b7de46"  # This is your API key token. Keep it secret!
    }

    response = requests.request("GET", API_URL, headers=headers, params=querystring)
    data = response.json()
    return data['streams'][0]['url']

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(text='Welcome to URL downloader!\nPlease provide a valid url')


def textHandler(update: Update, context: CallbackContext) -> None:
    user_message = str(update.message.text)

    if update.message.parse_entities(types=MessageEntity.URL):
        download_url = get_Download_URL_From_API(user_message)
        update.message.reply_text(text=f'Your download url is: {download_url}')



def main():
    TOKEN = "YOUR BOT TOKEN"
    updater = Updater(TOKEN, use_context=True)
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(MessageHandler(Filters.all & ~Filters.command, textHandler, run_async=True))
   updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
updater.bot.setWebhook('https://sajilodownloader.herokuapp.com/' + TOKEN)
    updater.idle()


if __name__ == '__main__':
    main()
