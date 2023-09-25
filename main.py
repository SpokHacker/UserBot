import telebot

import os
from pyrogram import Client, filters
from googletrans import Translator
spambots = ["5750837116:AAHjkckRW7SvMLGtaV8qW4bNumHvxOksib8",
"6262856402:AAE4azw1YFaMaI_HV7RpBAwqE-TapI4wAxo",
"6053378618:AAGtu-H5j1w3AjgWln1q3Meig2GKHV5T_fA",
"6154281184:AAF0Mo-D63vnejHoWSmhZFyL63wg6aGQxq0",
"6424154462:AAHd2JAuFw7K0t21bhRrG-XSRP4fpTd_Oc4",
"6307519348:AAGgyeu0-bQST2ESzaHwy-EARVQxoAVBBuU",
"6034336772:AAGfSUYPSxnU_WN2adFmVQQtck24-NCXems",
"6508957022:AAGxeEBP29LR9eySOGRRmHSvYbeIiY8qPqU",
"5944003224:AAF12zEe_1ZUNb8-LMWGNXY1UTzTduo_0UU"]

from pyrogram.errors import FloodWait
import pyrogram
import base64

import time
from pyrogram.raw import functions

lefter = False


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
.steal <ответ на сообщение> - скопировать имя ,фамилию ,описание и аву
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
.botclear - очистка текста написаного ботами из списка токенов
    '''
    app.send_message(chatid, helps)





def _(chatid, text, omsg):  # Шаблон
    pass
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



    # for i in spambots:
    #     bot = telebot.TeleBot(i)
    #     bot.remove_webhook()
def getidd(chatid, text, omsg):
    msgtosend =f'''CHATID: {chatid}
USERNAME: {omsg.reply_to_message.from_user.username}
USERID: {omsg.reply_to_message.from_user.id}'''
    app.send_message(chatid,msgtosend)
    print(omsg)

def addbots(chatid, text, omsg):
    for i in spambots:
        app.add_chat_members(chatid, telebot.TeleBot(i).get_me().username)
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
        app.send_message(chatid, "Нажми просто очистить историю)))")
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
        # app.delete_messages(d.chat.id, d.id)
        dicev = d.dice.value


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
app = Client("my_account", 666,"919adb3e55666666a417d1a0348ba")
tgfunctions = {".botclear":botclear,".addbots":addbots,".id":getidd,".dn":n,".dText":dText,".steal":cram,".dice":dice,".gpt":chatgpt,".spam":lagspam,".en":trans,".heart":heart,".calc":calc,".log":logs,".aDell":dell,".help":help,".banall":banall,".spamjoin":botjoiner,".jlbots":jlbot,".botmsg":botmsg}


@app.on_message(filters.left_chat_member & filters.group)
def left(client,mess):
    if lefter:
        app.send_message(mess.chat.id,f"Ливнул - {mess.left_chat_member.first_name}")


@app.on_message(filters.me & filters.text)
def s(client,mess):
    m = mess.text.split()
    if m[0] in tgfunctions.keys():
        app.delete_messages(mess.chat.id,mess.id)
        tgfunctions.get(m[0])(mess.chat.id," ".join(m[1:]),mess)



print("UserBot Strarted")
app.run()
