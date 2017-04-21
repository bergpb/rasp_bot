from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
import telepot
import time
import os
import commands

def handle(msg):
# configuracao do conversa
    comando = msg['text']
    content_type, chat_type, chat_id = telepot.glance(msg)
    m = telepot.namedtuple.Message(**msg)
#pegas as informacoes da conversa

# Configuracoes do teclado 
    keyboard=ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Temperatura"), KeyboardButton(text="Memoria")],
            [KeyboardButton(text="UpTime"), KeyboardButton(text="UsoSD")],
            [KeyboardButton(text="Data"),  KeyboardButton(text="IP")],
            [KeyboardButton(text="Processos"), KeyboardButton(text="Ajuda")],
        ])
#menssagem incial do bot depois do comando \start
    if comando == '/start':
        bot.sendMessage(chat_id, ' Bem Vindo!!')
	bot.sendMessage(chat_id, ' Bot desenvolvido por @joao_slv')
	bot.sendMessage(chat_id, ' Iniciando o Bot...')
	bot.sendMessage(chat_id, ' Use os comandos do teclado abaixo: ', reply_markup=keyboard )
	
	if chat_id < 0:
       		print 'Received a %s from %s, by %s' % (content_type, m.chat, m.from_)
   	else:
        	print 'Received a %s from %s' % (content_type, m.chat)

    elif comando == 'Temperatura':
	bot.sendMessage(chat_id, ' Temperatura da CPU : ')
	print 'Comando usado ', comando	

	if chat_id < 0:
       		print 'Received a %s from %s, by %s' % (content_type, m.chat, m.from_)
    	else:
        	print 'Received a %s from %s' % (content_type, m.chat)

    elif comando == 'Memoria':
	bot.sendMessage(chat_id, ' Memoria em uso: ')
	print 'Comando usado ', comando

	if chat_id < 0:
	        print 'Received a %s from %s, by %s' % (content_type, m.chat, m.from_)
    	else:
       		print 'Received a %s from %s' % (content_type, m.chat)

    elif comando == 'UpTime':
	bot.sendMessage(chat_id, ' Uptime do Sistema: ')
	print 'Comando usado ',  comando

	if chat_id < 0:
        	print 'Received a %s from %s, by %s' % (content_type, m.chat, m.from_)
    	else:
        	print 'Received a %s from %s' % (content_type, m.chat)
	
    elif comando == 'UsoSD':
	bot.sendMessage(chat_id,'Informacoes sobre o uso do MicroSD')
	print 'Comando usado ', comando

	if chat_id < 0:
	        print 'Received a %s from %s, by %s' % (content_type, m.chat, m.from_)
    	else:
        	print 'Received a %s from %s' % (content_type, m.chat)

    elif comando == 'Data':
	bot.sendMessage(chat_id, 'Data e Hora da maquina ')
	print 'Comando usado ', comando

	if chat_id < 0:
	        print 'Received a %s from %s, by %s' % (content_type, m.chat, m.from_)
    	else:
        	print 'Received a %s from %s' % (content_type, m.chat)
	
    elif comando == 'IP':
	bot.sendMessage(chat_id, 'Aguarde essa funcao no futuro ta dificel  de fazer agora =/')
	print 'Comando usado ', comando

	if chat_id < 0:
                print 'Received a %s from %s, by %s' % (content_type, m.chat, m.from_)
        else:
                print 'Received a %s from %s' % (content_type, m.chat)
                
    elif comando == 'Processos':
	bot.sendMessage(chat_id, 'Aqui esta o numero de processos: ')
	print 'Comando usado ', comando

	if chat_id < 0:
	        print 'Received a %s from %s, by %s' % (content_type, m.chat, m.from_)
	else:
        	print 'Received a %s from %s' % (content_type, m.chat)


    elif comando == 'Ajuda':
	bot.sendMessage(chat_id, 'Menu de Ajuda')
	bot.sendMessage(chat_id, 'Aqui era pra ter informacoes uteis mas nao tem =/')
	print 'Comando usado ', comando

	if chat_id < 0:
        	print 'Received a %s from %s, by %s' % (content_type, m.chat, m.from_)
    	else:
        	print 'Received a %s from %s' % (content_type, m.chat)

    else:
        bot.sendMessage(chat_id, 'Use os comandos no teclado')
	bot.sendMessage(chat_id, 'Ainda nao sei ler')

bot = telepot.Bot('BOT API here')
bot.message_loop(handle)

print 'Aguardando comandos ...'

while 1:
    time.sleep(5)
