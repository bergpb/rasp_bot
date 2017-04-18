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
		bot.sendMessage(chatid, '''temperatura : ''')


    elif comando == 'Memoria':
		bot.sendMessage(chatid, '''Memoria em uso: ''')


    elif comando == ' UpTime':
		bot.sendMessage(chatid, ''' Uptime do Sistema''')


    elif comando == 'Hostname':
		bot.sendMessage(chatid, '''Hostname da maquina: ''')


    elif comando == 'Data':
		bot.sendMessage(chatid, '''Data e Hora da maquina''')


    elif comando == 'IP':
		if chatid == '':
			bot.sendMessage(chatid, '''Use os comandos no teclado para que possa ter acesso as opcoes do bot.''')
		else:
			bot.sendMessage(chatid, '''Voce nao tem permissao para ver o IP''')
			
    elif comando == 'CPU_Info':
		bot.sendMessage(chatid, '''Aqui estao as informacoes sobre a CPU''')


    elif comando == 'Ajuda':
		bot.sendMessage(chatid, '''Menu de Ajuda aqui voce nao vai encotrar ajuda nem uma =/ ''')


    else:
        bot.sendMessage(chatid, '''Use os comandos no teclado''')

bot = telepot.Bot('346248441;AAEGri00lPsFmKEzshGtthdoEgyawJ08s5k')
bot.message_loop(handle)

print 'Aguardando comandos ...'

while 1:
 time.sleep(5)
