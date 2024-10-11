import telebot
import os
from pyrogram import Client, filters
from googletrans import Translator
from pyrogram.enums import UserStatus, ChatAction
from datetime import datetime
from pyrogram.errors import FloodWait
import time

notiferbot = "add your bot"

spambots = ["6424154462:AAHd2JAuFw7K0t21bhRrG-XSRP4fpTd_Oc4",
            "6307519348:AAGgyeu0-bQST2ESzaHwy-EARVQxoAVBBuU",
            "5618638676:AAF4va3Ae5gFPffeH9QAOr1i_TikhcKAces",
            "1668653860:AAH61P0HXn9K5yNmYXuiqLeDcOuMdZJQXZE",
            "6980680619:AAGma0Bpak9-xzjbmovRZgtVIMa_9AkjTVk",
            "6905063370:AAFYe9nQLrqTQ-v9swanwUwENHafYE7rh18",
            "6715565004:AAHV7PIs63ARmF_tOFvupO0tkvt7ZkUUgps",
            "1919231868:AAGYYYcEGYXlM5d67Zb8zX8tOKb200eD2MU",
            "6862301136:AAHfF5AhtnxzI54mHxYKR2KhLwPFt94lGEU",
            "5937952685:AAGm_VKuB4FKas-cMPUfVmtDNdJPw3FCDhs",
            "7415177117:AAFwA8Ruwp1E0mij5O8hxiHFJepN8a64g98",
            ]

actions = {
    "TYPING":ChatAction.TYPING,
    "CHOOSE_CONTACT":ChatAction.CHOOSE_CONTACT,
    "CHOOSE_STICKER":ChatAction.CHOOSE_STICKER,
    "UPLOAD_VIDEO":ChatAction.UPLOAD_VIDEO,
    "UPLOAD_AUDIO":ChatAction.UPLOAD_AUDIO,
    "UPLOAD_PHOTO":ChatAction.UPLOAD_PHOTO,
    "UPLOAD_DOCUMENT":ChatAction.UPLOAD_DOCUMENT,
    "UPLOAD_VIDEO_NOTE":ChatAction.UPLOAD_VIDEO_NOTE,
    "FIND_LOCATION":ChatAction.FIND_LOCATION,
    "IMPORT_HISTORY":ChatAction.IMPORT_HISTORY,
    "PLAYING":ChatAction.PLAYING,
    "RECORD_AUDIO":ChatAction.RECORD_AUDIO,
    "RECORD_VIDEO":ChatAction.RECORD_VIDEO,
    "RECORD_VIDEO_NOTE":ChatAction.RECORD_VIDEO_NOTE,
    "SPEAKING":ChatAction.SPEAKING,
    "STOP":ChatAction.CANCEL,
}








# Функция чтобы заливать файлы на 0x0.st
# _____________________________________________________________
import requests


def st0x0(filename):
    url = 'http://0x0.st'
    with open(filename, 'rb') as file:
        response = requests.post(url, files={'file': file})
    return response.text


# -------------------------------------------------------------


def help(chatid, text, omsg):
    helps = f'''
BY @SPOKHACKER
USERBOT:
.dText <текст> - Эфект печатающегося текста
.bText [текст] - прикольный эффект текста
.steal <ответ на сообщение> - скопировать имя ,фамилию ,описание и аву
.dn <текст> - пишет и удаляет сообщение каждые 3 сек 30 раз 
.dice <число кубика> подобрать dice
.gpt <вопрос у chat gpt> - спросить у чат гпт
.spam <Количесто стикеров> - спамит лагучими стикерами
.en <текст> - перевести текст на англиский
.heart - отправляет сердце у которого каждые 2 секунды меняется цвет
.calc <текст под считать пример 2+2> - подсчитать
.log - получить логи чата в виде ссылки на 0x0.st
.aDell - удалить все мои сообщения в этом чате
.banall - забанит всех в чате
.botclear - очистит всё от ботов
.spamjoin [текст] - к чату подключаются боты и спамят [текст]
.jlbots - к чату будут подключаться боты и выходить
.botmsg - отправить соощение от бота если он есть в чате
.addbots - добавить ботов из списка токенов
.clock <задержка> - выводит время
.online <ответ на сообщение> - присылает уведомление если человек появился в сети
.setAction <Навание действия> - устанавливает действие например TYPING


    '''

    app.send_message(chatid, helps)

def fake_action(chatid, text, omsg):

    if text == "" or text == " ":
        _temp = "Помощь:\n"
        for i in actions.keys():
            _temp += f"{i}\n"
        g = app.send_message(chatid,_temp)
        time.sleep(20)
        app.delete_messages(chatid,g.id)
        return
    elif text in actions.keys():
        app.send_chat_action(chatid, actions[text])

    else:
        app.send_message(chatid, "Ненайдено \n Напишите .setAction")


def text_effect1(chatid, text, omsg):
    t = ""
    mess = app.send_message(chatid,"g")
    for i in text:
        t += i
        if len(t) >= 7:
            t = t[1:]
        try:
            app.edit_message_text(chatid,mess.id,f"| {t} |")
        except:
            pass
        time.sleep(0.2)
    app.delete_messages(chatid,mess.id)












def botclear(chatid, text, omsg):

    ids = {}
    
    history = app.get_chat_history(chat_id=chatid,limit=140)
    for i in spambots:
        botid =(telebot.TeleBot(i).get_me().username)
        ids[botid] = i

    for i in history:
        if i.from_user.is_bot:
            if i.from_user.username in ids.keys():
                bot = telebot.TeleBot(ids[i.from_user.username])
                bot.remove_webhook()
                bot.delete_message(chatid,i.id)



def getidd(chatid, text, omsg):
    msgtosend =f'''CHATID: {chatid}
USERNAME: {omsg.reply_to_message.from_user.username}
USERID: {omsg.reply_to_message.from_user.id}'''
    app.send_message(chatid,msgtosend)
    print(omsg)

def addbots(chatid, text, omsg):
    for i in spambots:
        try:
            app.add_chat_members(chatid, telebot.TeleBot(i).get_me().username)
        except:
            pass

def clocktime(chatid, text, omsg):
    g = app.send_message(chatid, "Функция успешно запущена")
    while True:
        time.sleep(int(text))
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        app.edit_message_text(chatid, g.id, current_time)
def notifercheak(chatid, text, omsg):
    id = omsg.reply_to_message.from_user.id
    username = omsg.reply_to_message.from_user.username
    g = app.send_message(chatid,"Функция успешно запущена")
    while UserStatus.OFFLINE == app.get_users(id).status:
        time.sleep(4)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        app.edit_message_text(chatid,g.id,current_time)
    bot = telebot.TeleBot(notiferbot)
    bot.delete_webhook()

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    bot.send_message(app.get_me().id,f"Юзер зашёл в телеграм \nUsername: {username}\nВремя: {current_time}")
def botmsg(chatid, text, omsg):
    for i in spambots:
        bot = telebot.TeleBot(i)
        bot.remove_webhook()
        try:
            bot.send_message(chatid,text)
        except:
            pass
def jlbot(chatid, text, omsg):
    for i in range(7):
        for i in spambots:

            app.add_chat_members(chatid,telebot.TeleBot(i).get_me().username)
            # except:
            #     pass
        for i in spambots:
            bot = telebot.TeleBot(i)
            bot.remove_webhook()
            try:
                bot.leave_chat(chatid)
            except:
                pass


def botjoiner(chatid, text, omsg):

    for i in spambots:
        try:
            app.add_chat_members(chatid,telebot.TeleBot(i).get_me().username)
        except:
            pass
    for i in range(7):
        for i in spambots:
            bot = telebot.TeleBot(i)
            bot.remove_webhook()
            bot.send_message(chatid,(text*4095)[:4095])
            time.sleep(0.3)
    for i in spambots:
        bot = telebot.TeleBot(i)
        bot.remove_webhook()
        bot.leave_chat(chatid)


def n(chatid, text, omsg):
    for i in range(30):
        g = app.send_message(chatid, text)
        time.sleep(3)
        app.delete_messages(chatid, g.id)



def banall(chatid, text, omsg):
    me = app.get_me().id
    for i in app.get_chat_members(chatid):
        if i.user.id != me:
            try:
                app.ban_chat_member(chatid, i.user.id)
            except:
                print("can't ban", i.user.first_name)


def dell(chatid, text, omsg):
    if chatid == app.get_me().id:
        app.send_message(chatid, f"Нажми просто очистить историю)))\n{len(tuple(app.get_chat_history(chatid)))} сообщений")
    else:
        history = tuple(app.get_chat_history(chatid))[::-1]
        for i in history:
            try:
                if i.from_user.id == omsg.from_user.id:
                    app.delete_messages(chatid, i.id)
            except:
                pass


def logs(chatid, text, omsg):
    j = open("logs.txt", "w", encoding="utf-8")
    tt = ()
    for i in tuple(app.get_chat_history(chatid))[::-1]:
        try:

            tt += (("[" + i.from_user.first_name + "]: " + i.text),)
        except:
            pass
    j.write("By @SpokHacker\n" + "\n".join(tt))
    j.close()
    app.send_message(chatid, f"Логи чата: {st0x0('logs.txt')}")
    os.remove("logs.txt")


def calc(chatid, text, omsg):
    app.send_message(chatid, str(eval(text)))


def heart(chatid, text, omsg):
    h = ("❤", "🧡", "💛", "💚", "💙", "💜", "🤍")
    m = app.send_message(chatid, h[0])

    while True:
        for i in h[1:]:
            try:
                app.edit_message_text(chat_id=m.chat.id, message_id=m.id, text=i)
                time.sleep(2.2)
            except FloodWait as e:
                time.sleep(e.x)

            except:
                break


def flefter(chatid, text, omsg):
    global lefter
    if lefter:
        lefter = False
    else:
        lefter = True
    app.send_message(chatid, f"lefter now is {lefter}")


def trans(chatid, text, omsg):
    tr = Translator()
    en = str(tr.translate(text, dest="en").text)
    app.send_message(chatid, en)


def lagspam(chatid, text, omsg):
    for _ in range(int(text)):
        app.send_sticker(chatid, "CAACAgIAAxkBAAIqAAFkKrx44LmwJfcSz9z6gj8tC7Z21wACnSsAAvOcIEuI0tVhzCmjyC8E")


def chatgpt(chatid, text, omsg):
    pass
    # otv = openai.Completion.create(
    #     model="text-davinci-003",
    #     prompt=text,
    #     max_tokens=1028,
    #     temperature=0)
    # app.send_message(omsg.chat.id, otv.choices[0].text)





def dice(chatid, text, omsg):
    dicev = -1

    while dicev != int(text):

        d = app.send_dice(omsg.chat.id, "🎲")
        dicev = d.dice.value
        if (dicev != int(text)):
            app.delete_messages(chatid,d.id)
            time.sleep(0.005)





def cram(chatid, userid, omsg):
    user = app.get_users(omsg.reply_to_message.from_user.id)
    bio = (app.get_chat(omsg.reply_to_message.from_user.id)).bio
    try:
        ava = app.download_media(user.photo.big_file_id, file_name="newfile.jpg")
    except:
        pass
    app.set_profile_photo(photo=ava)
    app.update_profile(first_name=user.first_name, last_name=(user.last_name if user.last_name != None else "ᅠ"))
    app.update_profile(bio=(bio if bio != None else "ᅠ"))


def dText(id_chat, text, omsg=0):
    msg = app.send_message(id_chat, text[0])
    d = str(text[0])
    for i in text[1:]:
        time.sleep(0.2)
        d += i
        app.edit_message_text(id_chat, (msg.id), (d + "▓"))
    app.edit_message_text(id_chat, (msg.id), (d))
    return False
app = Client("my_account", 666666,"hash")
tgfunctions = {".setAction":fake_action,".bText":text_effect1,".clock":clocktime,".online":notifercheak,".botclear":botclear,".addbots":addbots,".id":getidd,".dn":n,".dText":dText,".steal":cram,".dice":dice,".gpt":chatgpt,".spam":lagspam,".en":trans,".heart":heart,".calc":calc,".log":logs,".aDell":dell,".help":help,".banall":banall,".spamjoin":botjoiner,".jlbots":jlbot,".botmsg":botmsg}





@app.on_message(filters.me & filters.text)
def s(client,mess):

    m = mess.text.split()
    if m[0] in tgfunctions.keys():
        app.delete_messages(mess.chat.id,mess.id)
        tgfunctions.get(m[0])(mess.chat.id," ".join(m[1:]),mess)



print("UserBot Strarted")
app.run()
