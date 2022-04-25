from pyrogram import Client as c, filters as f
from random import choice, randint
from time import time
from asyncio import sleep
from os import getenv
###############################


TOKEN = getenv("STRING") # String i '' Bunun İçine Yaz
fotoUrl = getenv("fotoUrl").replace(' ', ',').split(',') # videoların Linkini '' Bunun İçine (,)virgül İle Ayırarak Gir
pmMesaj = getenv("pmMesaj").split('""')

chatMessage = {}

emojiList = [
"🥰","🥺","❤️","🥵","😘","🤍","💗","💖","💘","💝","💔"
]

spamCeza={}
spamliList=[]
spamTime={}
spamMsg={}
chatSend={}

grupTanıtma = ["selam{}","naber{}","napiyonuz{}","napiyorsunuz{}","nbr{}","şlm{}","slm{}","npynz{}","npyrsnz{}","şelam{}"]

chatFilter = ["selam","naber","napiyon","napiyorsun","nbr","şlm","slm","npyn","npyrsn","şelam"]

s_k = c(
    "TOKEN",
    api_id="5775802",
    api_hash="6011ffc6cec69c60ef86456db0ce4d09",
    session_string=TOKEN,
    in_memory=True)

def filter_(a):
    b=None
    if a == "selam":
        b="Selammmm {}"
    elif a == "naber":
        b="İyiii Aşkım Senn {}"
    elif a == "napiyon":
        b = "Iıı, Şeyy Seni Özeledim Aşkım Aklımdan Hiç Cıkmadığın İçin Seni Düşünüyorummm Sen Napıyorsunn {}"
    elif a == "napiyorsun":
        b = "Iıı, Şeyy Seni Özeledim Aşkım Aklımdan Hiç Cıkmadığın İçin Seni Düşünüyorummm Sen Napıyorsunn {}"
    elif a== "nbr":
        b = "İyiii Aşkım Senn {}"
    elif a== "slm":
        b = "Selammmm {}"
    elif a== "şlm":
        b = "Şelammmm {}"
    elif a== "npyn":
        b = "Iıı, Şeyy Seni Özeledim Aşkım Aklımdan Hiç Cıkmadığın İçin Seni Düşünüyorummm Sen Napıyorsunn {}"
    elif a== "npyrsn":
        b = "Iıı, Şeyy Seni Özeledim Aşkım Aklımdan Hiç Cıkmadığın İçin Seni Düşünüyorummm Sen Napıyorsunn {}"
    elif a== "şelam":
        b = "Şelammmm {}"

    return "**"+b+"**"



@s_k.on_message(f.me & f.command("alive", ""))
async def _(b,m):
    await m.edit("Çalışıyorum!")
    
aktifZaman = time()
@s_k.on_message(f.private |f.mentioned | f.group)
async def _(b, m):
    global aktifZaman
    user = m.from_user
    chat = m.chat
    if str(user.id) in spamliList:
      if int(time()-spamCeza[str(user.id)])>=300:
        spamliList.remove(str(user.id))
        del(spamTime[str(user.id)])
        del(spamMsg[str(user.id)])
        del(spamCeza[str(user.id)])
        return
      else:
        return
    else:
      try:
        if int(time()-spamTime[str(user.id)])<=5 and spamMsg[str(user.id)]>=10:
          spamliList.append(str(user.id))
          spamCeza[str(user.id)]=time()
          return
        else:
          pass
      except:
        pass
    
    if str(chat.type) != 'ChatType.PRIVATE':
      if str(chat.id) in chatSend:
        if int(time()-chatSend[str(chat.id)])>=10800:
          try:
            await b.send_message(chat.id, choice(grupTanıtma).format(choice(emojiList)))
          except:
            await chat.archive
        else:
          chatSend[str(chat.id)]=time()
          
    if str(user.id) in spamTime and int(time()-spamTime[str(user.id)])>=300:
      del(spamTime[str(user.id)])
      del(spamMsg[str(user.id)])
    else:
      spamTime[str(user.id)]=time()
      

    try:
        if user.is_self:
            return
    except:
        pass
    if str(chat.type) != "ChatType.PRIVATE" and m.reply_to_message and not m.mentioned:
        return
    a= ""
    if m.text:
        for i in list(m.text):
            a=a+i.lower()
            if a in chatFilter:
                try:
                    await m.reply_text(filter_(a).format(choice(emojiList)))
                    if str(user.id) not in spamMsg:
                      spamMsg[str(user.id)]=0
                    spamMsg[str(user.id)]+=1
                except:
                    await chat.archive()
                return
    if chat.id not in chatMessage:
        chatMessage[chat.id] = 1
    if chatMessage[chat.id]%2==0:
        return
    if str(chat.type) != "ChatType.PRIVATE" and not m.mentioned:
        chatMessage[chat.id] += 1
    if chatMessage[chat.id] % 60==0:
        try:
            await b.send_message(chat.id, choice(grupTanıtma).format(choice(emojiList)))
        except:
            await chat.archive()
    if str(chat.type) == "ChatType.PRIVATE" or m.mentioned:
        if user.is_bot:
            return
        if m.mentioned:
            try:
                await m.reply_text("**Özelden Yazarmısın Aşkmmmm {}".format(choice(emojiList)))
                if str(user.id) not in spamMsg:
                  spamMsg[str(user.id)]=0
                spamMsg[str(user.id)]+=1
            except:
                await chat.archive()
            return

        try:
            a = choice(fotoUrl)
        except:
            pass

        try:
            await b.send_photo(chat.id, photo=a, caption=choice(pmMesaj).format(choice(emojiList), choice(emojiList), choice(emojiList), choice(emojiList), choice(emojiList)))
        except:
            try:
                await b.send_video(chat.id, video=a, caption=choice(pmMesaj).format(choice(emojiList), choice(emojiList), choice(emojiList), choice(emojiList), choice(emojiList)))
            except:
                try:
                    await b.send_audio(chat.id, audio=a, caption=choice(pmMesaj).format(choice(emojiList), choice(emojiList), choice(emojiList), choice(emojiList), choice(emojiList)))
                except:
                    try:
                        await b.send_voice(chat.id, voice=a, caption=choice(pmMesaj).format(choice(emojiList), choice(emojiList), choice(emojiList), choice(emojiList), choice(emojiList)))
                    except:
                        try:
                            await b.send_message(chat.id, choice(pmMesaj).format(choice(emojiList), choice(emojiList), choice(emojiList), choice(emojiList), choice(emojiList)))
                        except Exception as r:
                            print(r)
    
    if str(user.id) not in spamMsg:
      spamMsg[str(user.id)]=0
    spamMsg[str(user.id)]+=1
s_k.run()
