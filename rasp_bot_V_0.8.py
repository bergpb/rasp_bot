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
			print '%s %s %s' % (content_type, m.chat, m.from_)
		elif chat_id == 83074778:
			bot.sendMessage(chat_id, 'Vai durmir Douglas')
		elif chat_id == 24774270:
			bot.sendMessage(chat_id, 'Corre berg')
		else:
			print '%s %s' % (content_type, m.chat)
			print '%s %s ' % (chat_id, chat_username)

	
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
		print 'Comando usado ', comando	
		temp = commands.getoutput("vcgencmd measure_temp | cut -c 6-12")
		bot.sendMessage(chat_id, "Temperatura atual: ")
  		bot.sendMessage(chat_id, str(temp))
		
		getinfo(chat_id)
		
	# segunda verificaçao verifica se o comando memoria
	# foi escolhido se escolhido retorna a memoria toral
	# memoria em uso e memoria livre respectivamente
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
	
	# terceira verificaçao verifica se o comando uptime
	# foi escolhido se escolhido retorna o uptime do sistema 
	elif comando == 'UpTime':
		print 'Comando usado ',  comando
		uptime = commands.getoutput("uptime -p")
		bot.sendMessage(chat_id,"Up Time do sistema:")
  		bot.sendMessage(chat_id, str(uptime))
		
		getinfo(chat_id)
		
	# quarta verificaçao verifica se o comando SD 
	# foi escolhido se escolhido retorna informaçes 
	# de espaço nas partiçoes de boot e root do sistema
    	elif comando == 'UsoSD':
		print 'Comando usado ', comando
		bot.sendMessage(chat_id, 'Estado da partiçao Boot')
		partBoot = commands.getoutput("df -h | grep '/mmc'| head -6")
		bot.sendMessage(chat_id, partBoot)
		bot.sendMessage(chat_id, 'Estado da partiçao root')
		partRoot = commands.getoutput("df -h | grep '/dev'| head -1")
		bot.sendMessage(chat_id, partRoot)
		
		getinfo(chat_id)
	
	# quinta verificação verifica se o comando data 
	# foi escolhido se escolhido retorna as 
	# informaçoes de data e hora atual da raspberry
	elif comando == 'Data':
		print 'Comando usado ', comando
		data = commands.getoutput("date")
 		bot.sendMessage(chat_id,"Data e hora do Sistema: ")
  		bot.sendMessage(chat_id, str(data))
		
		getinfo(chat_id)
	
	# sexta verificação verifica se o comando ip foi executado
	# se executado verifica o chat_id de quem solicitou se o 
	# chat_id do solicitante for igual aos listados 
	# abaixo ele retorna o endereço de ip local e externo
	elif comando == 'IP':
		print 'Comando usado ', comando
		# ip local para min dougras e berg
		if chat_id == 345318600 or chat_id == 83074778 or chat_id == 24774270:
			
			# aqui pega o ip da lan
			iplan = commands.getoutput("ifconfig wlan0 |  grep inet | cut -c 21-37 | head -1")
			bot.sendMessage(chat_id, 'Endereço de ip local :')
			bot.sendMessage(chat_id,str(iplan))
			
			#ip externo so pra min
			if chat_id == 345318600:	
				# aqui pega o ip externo dessa bagaça 
				response = urllib2.urlopen('http://bot.whatismyipaddress.com/')
				ipex = response.read()			
				bot.sendMessage(chat_id, 'Endereço de ip externo :')
				bot.sendMessage(chat_id,str(ipex))
			
			bot.senMessage(chat_id, 'Aqui ta o IP porra!!!!')
	
		else:
			bot.sendMessage(chat_id, 'Sai daqui voce nao vai ver o endereço de IP!!! ')
  		
		getinfo(chat_id)
		
	# setima verificaçao verifica se o comando processos 
	# foi escolhido se escolhido ele conta quantos 
	# processos estao rodando no momento e retorna para o usuario	
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

while 1:
time.sleep(5)
