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
	print 'Comando usado ', comando	
	temp = commands.getoutput("vcgencmd measure_temp | cut -c 6-12")
	bot.sendMessage(chat_id, "Temperatura atual: %s" % str(temp))
	
	if chat_id < 0:
       		print 'Received a %s from %s, by %s' % (content_type, m.chat, m.from_)
    	else:
        	print 'Received a %s from %s' % (content_type, m.chat)

    elif comando == 'Memoria':
	print 'Comando usado ', comando
	men = commands.getoutput("free -h | cut -c 1-45 | head -2")
	bot.sendMessage(chat_id,"Estado da memoria: %s" % str(men))
	
	if chat_id < 0:
	        print 'Received a %s from %s, by %s' % (content_type, m.chat, m.from_)
    	else:
       		print 'Received a %s from %s' % (content_type, m.chat)

    elif comando == 'UpTime':
	print 'Comando usado ',  comando
	uptime = commands.getoutput("uptime -p")
	bot.sendMessage(chat_id,"Up Time do sistema: %s" % str(uptime))

	if chat_id < 0:
        	print 'Received a %s from %s, by %s' % (content_type, m.chat, m.from_)
    	else:
        	print 'Received a %s from %s' % (content_type, m.chat)
	
    elif comando == 'UsoSD':
	print 'Comando usado ', comando
	sd = commands.getoutput("df -hlT")
	bot.sendMessage(chat_id,"Uso do MicroSD: %s" % str(sd))
	
	if chat_id < 0:
	        print 'Received a %s from %s, by %s' % (content_type, m.chat, m.from_)
    	else:
        	print 'Received a %s from %s' % (content_type, m.chat)

    elif comando == 'Data':
	print 'Comando usado ', comando
	data = commands.getoutput("date")
 	bot.sendMessage(chat_id,"Data e hora do Sistema: %s" % str(data))
	
	if chat_id < 0:
	        print 'Received a %s from %s, by %s' % (content_type, m.chat, m.from_)
    	else:
        	print 'Received a %s from %s' % (content_type, m.chat)
	
    elif comando == 'IP':
	bot.sendMessage(chat_id, 'Aguarde... no futuro ta dificel  de fazer agora =/')
	print 'Comando usado ', comando

	if chat_id < 0:
                print 'Received a %s from %s, by %s' % (content_type, m.chat, m.from_)
        else:
                print 'Received a %s from %s' % (content_type, m.chat)
                
    elif comando == 'Processos':
	print 'Comando usado ', comando
	quantProc = commands.getoutput("ps -aux | wc -l")
	bot.sendMessage("Quantidade de processos rodando e : %i", int(quantProc))
	
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
	bot.sendMessage(chat_id, 'Ainda nao sei ler =,(')

bot = telepot.Bot('346248441:AAEGri00lPsFmKEzshGtthdoEgyawJO8s5k')
bot.message_loop(handle)

print 'Aguardando comandos ...'

while 1:
	time.sleep(5)
