
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
import telepot
import time
import os

def handle(msg):
    chatid = msg['chat']['id']
    comando = msg['text']
    
     keyboard=ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Temperatura"), KeyboardButton(text="IP")],
            [KeyboardButton(text="Memoria"), KeyboardButton(text="Hostname")],
            [KeyboardButton(text="UpTime"),  KeyboardButton(text="Data")],
            [KeyboardButton(text="CPU_Info"), KeyboardButton(text="Ajuda")],
        ])
    
    if comando == '/start':
        bot.sendMessage(chatid, '''Bem Vindo!! 
        Bot desenvolvido por @joao_slv!
        Use /start - Iniciando o Bot
        Use os comandos do teclado abaixo: ''', reply_markup=keyboard )
        
    elif comando == 'Temperatura':
    
    elif comando == 'Memoria':
        
    elif comando == ' UpTime':
   
    elif comando == 'Hostname':
   
    elif comando == 'Data':
    
    elif comando == 'IP':
    
    elif comando == 'CPU_Info':
    
    elif comando == 'Ajuda':
       
    else:
        bot.sendMessage(chatid, '''Use os comandos no teclado para que possa ter acesso as opções do bot.''')

    
bot = telepot.Bot('346248441;AAEGri00lPsFmKEzshGtthdoEgyawJ08s5k')
bot.message_loop(handle)
              
print 'Aguardando comandos ...'

while 1:
    time.sleep(5)
