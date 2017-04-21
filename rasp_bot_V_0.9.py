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
	# tem tambem a tupla que salva as info do chat 
	comando = msg['text']
	content_type, chat_type, chat_id = telepot.glance(msg)
	m = telepot.namedtuple.Message(**msg)
	
	# função criada para evitar repetindo o codigo ele faz 
	# verificação se a messagem foi enviada de um grupo ou de um chat privado
	def getinfo(chat_id):
		if chat_id < 0:
			print 'Menssage do tipo %s' % (content_type,)
			print '-------------------------------------'
			print 'Chat ID : %s' % m.chat[0]
			print 'Tipo de chat : %s' % m.chat[1]
			print 'Nome do Grupo: %s' % m.chat[2]
			print 'Username : %s' % m.chat[3]
			print 'First Name: %s' % m.chat[4]
			print 'Last Name: %s' % m.chat[5]
			print 'Enviada por %s' % (m.from_,)
			print '--------------------------------------'
		# envia messangens de acordo com o chat id
		elif chat_id == 83074778:
			bot.sendMessage(chat_id, 'Seja Bem Vindo Sr. Douglas Zuqueto')
		elif chat_id == 24774270:
			bot.sendMessage(chat_id, 'Corre berg')
		else:
			print 'Messagem do tipo %s ' % (content_type,)
			print '--------------------------------------'
			print 'Chat ID : %s' % m.chat[0]
			print 'Tipo de chat : %s' % m.chat[1]
			print 'Username : %s' % m.chat[3]
			print 'First Name: %s' % m.chat[4]
			print 'Last Name: %s' % m.chat[5]
			print '--------------------------------------'
	
	# Aqui e o teclado que aparece para o usuario 
	# define as palavras que aparecem e os comanos
	# que seram enviadas quando forem clicados
	keyboard=ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Temperatura"), KeyboardButton(text="Memoria")],
            [KeyboardButton(text="UpTime"), KeyboardButton(text="UsoSD")],
            [KeyboardButton(text="Data"),  KeyboardButton(text="IP")],
            [KeyboardButton(text="Processos"), KeyboardButton(text="Ajuda")],
        ])
	
	# primeiro IF que inicia o bot quando começa a 
	# conversa envia apenas messagens de boas vindas
	if comando == '/start':
		bot.sendMessage(chat_id, ' Bem Vindo!!')
		bot.sendMessage(chat_id, ' Bot desenvolvido por @joao_slv')
		bot.sendMessage(chat_id, ' Iniciando o Bot...')
		bot.sendMessage(chat_id, ' Use os comandos do teclado abaixo: ', reply_markup=keyboard )
		
		getinfo(chat_id)
		
	# primeira verificaçao verifica se o comando temperatura
	# foi escolhido se escolhido retorna a temperatura da cpu	
	elif comando == 'Temperatura':
		print '---------------------------'
		print 'Comando usado ', comando	
		print '---------------------------'
		temp = commands.getoutput("vcgencmd measure_temp | cut -c 6-12")
		bot.sendMessage(chat_id, "Temperatura atual: ")
  		bot.sendMessage(chat_id, str(temp))
		
		getinfo(chat_id)
		
	# segunda verificaçao verifica se o comando memoria
	# foi escolhido se escolhido retorna a memoria toral
	# memoria em uso e memoria livre respectivamente
	elif comando == 'Memoria':
		print '---------------------------'
		print 'Comando usado ', comando
		print '---------------------------'
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
	
	# terceira verificaçao verifica se o comando uptime
	# foi escolhido se escolhido retorna o uptime do sistema 
	elif comando == 'UpTime':
		print '---------------------------'
		print 'Comando usado ',  comando
		print '---------------------------'
		uptime = commands.getoutput("uptime -p")
		bot.sendMessage(chat_id,"Up Time do sistema:")
  		bot.sendMessage(chat_id, str(uptime))
		
		getinfo(chat_id)
		
	# quarta verificaçao verifica se o comando SD 
	# foi escolhido se escolhido retorna informaçes 
	# de espaço nas partiçoes de boot e root do sistema
    	elif comando == 'UsoSD':
		print '---------------------------'
		print 'Comando usado ', comando
		print '---------------------------'
		bot.sendMessage(chat_id, 'Estado da partiçao root')
		partRoot = commands.getoutput("df -h | grep '/dev'| head -1")
		bot.sendMessage(chat_id, partRoot)
		
		getinfo(chat_id)
	
	# quinta verificação verifica se o comando data 
	# foi escolhido se escolhido retorna as 
	# informaçoes de data e hora atual da raspberry
	elif comando == 'Data':
		print '---------------------------'
		print 'Comando usado ', comando
		print '---------------------------'
		data = commands.getoutput("date")
 		bot.sendMessage(chat_id,"Data e hora do Sistema: ")
  		bot.sendMessage(chat_id, str(data))
		
		getinfo(chat_id)
	
	# sexta verificação verifica se o comando ip foi executado
	# se executado verifica o chat_id de quem solicitou se o 
	# chat_id do solicitante for igual aos listados 
	# abaixo ele retorna o endereço de ip local e externo
	elif comando == 'IP':
		print '---------------------------'
		print 'Comando usado ', comando
		print '---------------------------'
		# ip local 
		if chat_id == 345318600 or chat_id == 83074778 or chat_id == 24774270:
			
			# aqui pega o ip da lan   ** eth0 para cabo wlan0 para wifi **
			iplan = commands.getoutput("ifconfig eth0 |  grep inet | cut -c 21-37 | head -1")
			bot.sendMessage(chat_id, 'Endereço de ip local :')
			bot.sendMessage(chat_id,str(iplan))
			
			#ip externo so pra min
			if chat_id == 345318600:	
				# aqui pega o ip externo dessa bagaça 
				response = urllib2.urlopen('http://bot.whatismyipaddress.com/')
				ipex = response.read()			
				bot.sendMessage(chat_id, 'Endereço de ip externo :')
				bot.sendMessage(chat_id,str(ipex))
	
		else:
			bot.sendMessage(chat_id, 'Sai daqui voce nao vai ver o endereço de IP!!! ')
  		
		getinfo(chat_id)
		
	# setima verificaçao verifica se o comando processos 
	# foi escolhido se escolhido ele conta quantos 
	# processos estao rodando no momento e retorna para o usuario	
    	elif comando == 'Processos':
		print '---------------------------'
		print 'Comando usado ', comando
		print '---------------------------'
		quantProc = commands.getoutput("ps -aux | wc -l")
		bot.sendMessage(chat_id, 'Quantidade de processos rodando e :')
  		bot.sendMessage(chat_id, str(quantProc))
		
		getinfo(chat_id)
		
	# IF do menu de ajuda so que ainda nao tem nada de ajudar nessa porra tbm	
	elif comando == 'Ajuda' or comando == '/help':
		print '---------------------------'
		print 'Comando usado ', comando
		print '---------------------------'
		bot.sendMessage(chat_id, 'Seja Bem Vindo ao Menu de Ajuda')
		bot.sendMessage(chat_id, 'Aqui voce encontra informaçoes sobre os comandos disponiveis nesse bot.')
    		bot.sendMessage(chat_id, 'Escolha um comando para ter informaçoes sobre ele.' reply_markup=keyboardHelp)
		
		getinfo(chat_id)
		
		comandoHelp = msg['text']
		
		keyboardHelp=ReplyKeyboardMarkup(
        	keyboardHelp=[
            	[KeyboardButton(text="Temperatura"), KeyboardButton(text="Memoria")],
            	[KeyboardButton(text="UpTime"), KeyboardButton(text="UsoSD")],
            	[KeyboardButton(text="Data"),  KeyboardButton(text="IP")],
            	[KeyboardButton(text="Processos"), KeyboardButton(text="Ajuda")],
		])
		if comandoHelp == 'Temperatura':
			bot.sendMessage(chat_id, 'Aqui voce encontra informações sobre o comando Temperatura')
			bot.sendMessage(chat_id, 'Lorem ipsum dolor sit amet, consectetur adipiscing elite')
		elif comandoHelp == 'Memoria':
			bot.sendMessage(chat_id, 'Aqui voce encontra informaçes sobre o comando Memoria')
			bot.sendMessage(chat_id, 'Lorem ipsum dolor sit amet, consectetur adipiscing elite')
		elif comandoHelp == 'UpTime':
			bot.sendMessage(chat_id, 'Aqui voce encontra informações sobre o comando UpTime')
			bot.sendMessage(chat_id, 'Lorem ipsum dolor sit amet, consectetur adipiscing elite')
		elif comandoHelp == 'UsoSD':
			bot.sendMessage(chat_id, 'Aqui voce encontra informações sobre o comando UsoSD')
			bot.sendMessage(chat_id, 'Lorem ipsum dolor sit amet, consectetur adipiscing elite')
		elif comandoHelp == 'Data':
			bot.sendMessage(chat_id, 'Aqui voce encontra informações sobre o comando  Data')
			bot.sendMessage(chat_id, 'Lorem ipsum dolor sit amet, consectetur adipiscing elite')
		elif comandoHelp == 'IP':
			bot.sendMessage(chat_id, 'Aqui voce encontra informações sobre o comando IP')
			bot.sendMessage(chat_id, 'Lorem ipsum dolor sit amet, consectetur adipiscing elite')
		elif comandoHelp == 'Processos':
			bot.sendMessage(chat_id, 'Aqui voce encontra informações sobre o comando Processos')
			bot.sendMessage(chat_id, 'Lorem ipsum dolor sit amet, consectetur adipiscing elite')
		elif comandoHelp == 'Ajuda':
			bot.sendMessage(chat_id, 'Aqui voce encontra informações sobre o comando Ajuda')
			bot.sendMessage(chat_id, 'Lorem ipsum dolor sit amet, consectetur adipiscing elite')
	# messagem para caso o usuario envie comandos digitados manualmente	
	else:
        	bot.sendMessage(chat_id, 'Use os comandos no teclado')
		bot.sendMessage(chat_id, 'Ainda nao sei ler =(')
		
# Aqui fica API do bot gerada pelo botfather
bot = telepot.Bot('346248441:AAEGri00lPsFmKEzshGtthdoEgyawJO8s5k')
bot.message_loop(handle)

print 'Aguardando comandos ...'

while 1:
	time.sleep(5)
