#!/usr/bin/python
# -*- coding: UTF-8 -*-

# aqui e os import das lib que estao sendo usadas
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
import telepot
import time
import os
import commands

# função principal do bot estrutura de decisão
def handle(msg):
	# configurações da variavel para controlar 
	# a estrutura de decisao saporra aqui e importante	
	comando = msg['text']
	content_type, chat_type, chat_id = telepot.glance(msg)
	m = telepot.namedtuple.Message(**msg)
	
	# Aqui e o teclado que aparece para o usuario 
	# define as palavras que aparecem e as que seram 
	# enviadas quando forem selecionadas
	keyboard=ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Temperatura"), KeyboardButton(text="Memoria")],
            [KeyboardButton(text="UpTime"), KeyboardButton(text="UsoSD")],
            [KeyboardButton(text="Data"),  KeyboardButton(text="IP")],
            [KeyboardButton(text="Processos"), KeyboardButton(text="Ajuda")],
        ])
	# primeiro IF que inicia o bot quando começa a 
	# conversar envia apenas messagens de boas vindas, 
	# desenvolvedor e versao do bot
	if comando == '/start':
		bot.sendMessage(chat_id, ' Bem Vindo!!')
		bot.sendMessage(chat_id, ' Bot desenvolvido por @joao_slv')
		bot.sendMessage(chat_id, ' Versão 0.5')
		bot.sendMessage(chat_id, ' Iniciando o Bot...')
		bot.sendMessage(chat_id, ' Use os comandos do teclado abaixo: ', reply_markup=keyboard )
		
		getinfo(chat_id)
		
	elif comando == 'Temperatura':
		print 'Comando usado ', comando	
		temp = commands.getoutput("vcgencmd measure_temp | cut -c 6-12")
		bot.sendMessage(chat_id, "Temperatura atual: ")
  		bot.sendMessage(chat_id, str(temp))
		
		getinfo(chat_id)
		
	elif comando == 'Memoria':
		print 'Comando usado ', comando
		men = commands.getoutput("free -h | cut -c 1-45 | head -2")
		bot.sendMessage(chat_id,"Estado da memória:")
  		bot.sendMessge(chat_id, str(men))
		
		getinfo(chat_id)
		
	elif comando == 'UpTime':
		print 'Comando usado ',  comando
		uptime = commands.getoutput("uptime -p")
		bot.sendMessage(chat_id,"Up Time do sistema:")
  		bot.sendMessage(chat_id, str(uptime))
		
		getinfo(chat_id)
		
    	elif comando == 'UsoSD':
		print 'Comando usado ', comando
		sd = commands.getoutput("df -h")
		bot.sendMessage(chat_id,"Uso do MicroSD:")
  		bot.sendMessage(chat_id, str(sd))
		
		getinfo(chat_id)
		
	elif comando == 'Data':
		print 'Comando usado ', comando
		data = commands.getoutput("date")
 		bot.sendMessage(chat_id,"Data e hora do Sistema: ")
  		bot.sendMessage(chat_id, str(data))
		
		getinfo(chat_id)
	
	# if comando ip que vai demorar um pouco pra 
	# implementar pois tem que fazer a verificação 
	# por chat_id que uma tupla tem que querbar 
	# ela e pegar os dados separados chatid, username 
	elif comando == 'IP':
		print 'Comando usado ', comando
		bot.sendMessage(chat_id, 'Aguarde essa funçao em versoes futuras')
		bot.sendMessage(chat_id, 'usa esse ip aqui 127.0.0')
  		
		getinfo(chat_id)
    	elif comando == 'Processos':
		print 'Comando usado ', comando
		quantProc = commands.getoutput("ps -aux | wc -l")
		bot.sendMessage(chat_id, 'Quantidade de processos rodando e :')
  		bot.sendMessage(chat_id, str(quantProc))
		
		getinfo(chat_id)
		
	# IF do menu de ajuda so que ainda nao tem nada de ajudar nessa porra tbm	
	elif comando == 'Ajuda':
		print 'Comando usado ', comando
		bot.sendMessage(chat_id, 'Menu de Ajuda')
		bot.sendMessage(chat_id, 'Aqui era pra ter informações uteis mas nao tem =/')
		
		getinfo(chat_id)
		
	# messagem para caso o usuario envie comandos digitados manualmente	
	else:
        	bot.sendMessage(chat_id, 'Use os comandos no teclado')
		bot.sendMessage(chat_id, 'Ainda nao sei ler =(')
		
# Aqui fica API do bot gerada pelo botfather
bot = telepot.Bot('346248441:AAEGri00lPsFmKEzshGtthdoEgyawJO8s5k')
bot.message_loop(handle)

print 'Aguardando comandos ...'

# função criada para evitar repetindo o codigo ele faz 
# verificação se a messagem foi enviada de um grupo ou de um chat privado
def getinfo(chat_id):
	if chat_id < 0:
		print 'Reebido uma %s de %s, por %s' % (content_type, m.chat, m.from_)
	else:
		print 'Recebida uma %s de %s' % (content_type, m.chat)

while 1:
	time.sleep(5)
