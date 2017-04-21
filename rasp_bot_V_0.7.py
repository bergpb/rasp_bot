#!/usr/bin/python
# -*- coding: UTF-8 -*-

# aqui e os import das lib que estao sendo usadas
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
import telepot
import time
import os
import commands
import urllib2

# função principal do bot estrutura de decisão
def handle(msg):
	# configurações da variavel para controlar 
	# a estrutura de decisao saporra aqui e importante	
	comando = msg['text']
	content_type, chat_type, chat_id = telepot.glance(msg)
	m = telepot.namedtuple.Message(**msg)
	
	# função criada para evitar repetindo o codigo ele faz 
	# verificação se a messagem foi enviada de um grupo ou de um chat privado
	def getinfo(chat_id):
		if chat_id < 0:
			print '%s %s %s' % (content_type, m.chat, m.from_)
			bot.sendMessage(chat_id, 'Grupo legal')
		elif chat_id == 83074778:
			bot.sendMessage(chat_id, 'Vai durmir Douglas')
		elif chat_id == 24774270:
			bot.sendMessage(chat_id, 'Corre berg')
		else:
			print '%s %s' % (content_type, m.chat)

	
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
		memt = commands.getoutput("free -h | grep 'Mem' | cut -c 15-18")
		bot.sendMessage(chat_id, 'Memoria total: ')
		bot.sendMessage(chat_id, memt)
		memu = commands.getoutput("free -h | grep 'Mem' | cut -c 26-29")
		bot.sendMessage(chat_id, 'Memoria em uso: ')
		bot.sendMessage(chat_id, memu)
		memf = commands.getoutput("free -h | grep 'Mem' | cut -c 37-40")
		bot.sendMessage(chat_id, 'Memoria livre: ')
		bot.sendMessage(chat_id, memf)
		
		getinfo(chat_id)
		
	elif comando == 'UpTime':
		print 'Comando usado ',  comando
		uptime = commands.getoutput("uptime -p")
		bot.sendMessage(chat_id,"Up Time do sistema:")
  		bot.sendMessage(chat_id, str(uptime))
		
		getinfo(chat_id)
		
    	elif comando == 'UsoSD':
		print 'Comando usado ', comando
		bot.sendMessage(chat_id, 'Estado da partiçao Boot')
		partBoot = commands.getoutput("df -h | grep '/mmc'| head -6")
		bot.sendMessage(chat_id, partBoot)
		bot.sendMessage(chat_id, 'Estado da partiçao root')
		partRoot = commands.getoutput("df -h | grep '/dev'| head -1")
		bot.sendMessage(chat_id, partRoot)
		
		getinfo(chat_id)
		
	elif comando == 'Data':
		print 'Comando usado ', comando
		data = commands.getoutput("date")
 		bot.sendMessage(chat_id,"Data e hora do Sistema: ")
  		bot.sendMessage(chat_id, str(data))
		
		getinfo(chat_id)
	
	elif comando == 'IP':
		print 'Comando usado ', comando
		if chat_id == 345318600 or chat_id == 83074778 or chat_id == 24774270:
			
			# aqui pega o ip da lan
			iplan = commands.getoutput("ifconfig wlan0 |  grep inet | cut -c 21-37 | head -1")
			bot.sendMessage(chat_id, 'Endereço de ip local :')
			bot.sendMessage(chat_id,str(iplan))
				
			# aqui pega o ip externo dessa bagaça 
			response = urllib2.urlopen('http://bot.whatismyipaddress.com/')
			ipex = response.read()			
			bot.sendMessage(chat_id, 'Endereço de ip externo :')
			bot.sendMessage(chat_id,str(ipex))
	
		else:
			bot.sendMessage(chat_id, 'Sai daqui voce nao vai ver o endereço de IP!!! ')
  		
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
bot = telepot.Bot('API BOT here')
bot.message_loop(handle)

print 'Aguardando comandos ...'

while 1:
      time.sleep(5)
