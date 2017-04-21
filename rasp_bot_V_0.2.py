from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
import telepot
import time

def handle(msg):
	chatid = msg['chat']['id']
    	comando = msg['text']

    	keyboard=ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Temperatura"), KeyboardButton(text="IP")],
            [KeyboardButton(text="Memoria"), KeyboardButton(text="UsoSD")],
            [KeyboardButton(text="UpTime"),  KeyboardButton(text="Data")],
            [KeyboardButton(text="CPU_Info"), KeyboardButton(text="Ajuda")],
        ])

    	if comando == '/start':
        	bot.sendMessage(chatid,'Bem Vindo!!') 
        	bot.sendMessage(chatid,'Bot desenvolvido por @joao_slv!')
        	bot.sendMessage(chatid,'Iniciando o Bot...')
        	bot.sendMessage(chatid,'Use os comandos do teclado abaixo', reply_markup=keyboard )

    	elif comando == 'Temperatura':
		bot.sendMessage(chatid, 'Temperatura : ')


    	elif comando == 'Memoria':
		bot.sendMessage(chatid, 'Memoria em uso: ')


	elif comando == 'UpTime':
		bot.sendMessage(chatid, 'Uptime do Sistema: ')


	elif comando == 'UsoSD':
		bot.sendMessage(chatid, 'Uso do MicroSD: ')


	elif comando == 'Data':
		bot.sendMessage(chatid, 'Data e Hora do sistema: ')


    	elif comando == 'IP':
		bot.sendMessage(chatid, 'O Meu IP: 127.0.0')
			
    	elif comando == 'CPU_Info':
		bot.sendMessage(chatid, 'Aqui estao as informacoes sobre a CPU:')


    	elif comando == 'Ajuda':
		bot.sendMessage(chatid, 'Menu de Ajuda aqui voce nao vai encotrar ajuda nem uma =/ ')


    	else:
        	bot.sendMessage(chatid, 'Use os comandos no teclado')

bot = telepot.Bot(' BOT API here')
bot.message_loop(handle)

print 'Aguardando comandos ...'

while 1:
	time.sleep(5)
