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
	command = msg['text']
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
            [KeyboardButton(text="Temperatura"), KeyboardButton(text="Processos")],
            [KeyboardButton(text="Memoria"), KeyboardButton(text="UpTime")],
            [KeyboardButton(text="UsoSD"),  KeyboardButton(text="Data")],
            [KeyboardButton(text="Rede"), KeyboardButton(text="IP")],
        ])
	
	# primeiro IF que inicia o bot quando começa a 
	# conversa envia apenas messagens de boas vindas
	if command == '/start':
		bot.sendMessage(chat_id, ' Bem Vindo!!')
		bot.sendMessage(chat_id, ' Bot desenvolvido por @joao_slv')
		bot.sendMessage(chat_id, ' Iniciando o Bot...')
		bot.sendMessage(chat_id, ' Use os comandos do teclado abaixo: ', reply_markup=keyboard )
		
		getinfo(chat_id)
		
	# primeira verificaçao verifica se o comando temperatura
	# foi escolhido se escolhido retorna a temperatura da cpu	
	elif command == 'Temperatura':
		print '---------------------------'
		print 'Comando usado ', command
		print '---------------------------'
		temp = commands.getoutput("vcgencmd measure_temp | cut -c 6-12")
		bot.sendMessage(chat_id, 'Temperatura atual: ')
  		bot.sendMessage(chat_id, str(temp))
		
		getinfo(chat_id)
		
	# segunda verificação verifica se o comando processos 
	# foi escolhido se escolhido ele conta quantos 
	# processos estao rodando no momento e retorna para o usuario	
    	elif command == 'Processos':
		print '---------------------------'
		print 'Comando usado ', command
		print '---------------------------'
		quantProc = commands.getoutput("ps -aux | wc -l")
		bot.sendMessage(chat_id, 'Quantidade de processos rodando e :')
  		bot.sendMessage(chat_id, str(quantProc))
		
		getinfo(chat_id)
		
	# terceira verificaçao verifica se o comando memoria
	# foi escolhido se escolhido retorna a memoria toral
	# memoria em uso e memoria livre respectivamente
	elif command == 'Memoria':
		print '---------------------------'
		print 'Comando usado ', command
		print '---------------------------'
		# memoria total
		mem_total = commands.getoutput("free -h | grep 'Mem' | cut -c 15-18")
		bot.sendMessage(chat_id, 'Memoria total: ')
		bot.sendMessage(chat_id, str(mem_total))
		# memoria em uso
		mem_used = commands.getoutput("free -h | grep 'Mem' | cut -c 26-29")
		bot.sendMessage(chat_id, 'Memoria em uso: ')
		bot.sendMessage(chat_id, str(mem_used))
		# memoria livre
		mem_free = commands.getoutput("free -h | grep 'Mem' | cut -c 37-40")
		bot.sendMessage(chat_id, 'Memoria livre: ')
		bot.sendMessage(chat_id, str(mem_free))
		
		getinfo(chat_id)
	
	# quarta verificaçao verifica se o comando uptime
	# foi escolhido se escolhido retorna o uptime do sistema 
	elif command == 'UpTime':
		print '---------------------------'
		print 'Comando usado ',  command
		print '---------------------------'
		uptime = commands.getoutput("uptime -p")
		bot.sendMessage(chat_id, 'Up Time do sistema: ')
  		bot.sendMessage(chat_id, str(uptime))
		
		getinfo(chat_id)
		
	# quinta verificaçao verifica se o comando SD 
	# foi escolhido se escolhido retorna informaçes 
	# de espaço nas partiçoes de boot e root do sistema
    	elif command == 'UsoSD':
		print '---------------------------'
		print 'Comando usado ', command
		print '---------------------------'
		partRoot = commands.getoutput("df -h | grep '/dev'| head -1")
		bot.sendMessage(chat_id, 'Estado da partiçao root')
		bot.sendMessage(chat_id, str(partRoot))
		
		getinfo(chat_id)
	
	# sexta verificação verifica se o comando data 
	# foi escolhido se escolhido retorna as 
	# informaçoes de data e hora atual da raspberry
	elif command == 'Data':
		print '---------------------------'
		print 'Comando usado ', command
		print '---------------------------'
		date = commands.getoutput("date")
 		bot.sendMessage(chat_id,'Data e hora do Sistema: ')
  		bot.sendMessage(chat_id, str(date))
		
		getinfo(chat_id)
		
	# setima verificação verifica se o comando Rede foi executa
	# se executado ele pega a quantidade de bytes trafegadas 
	# pelas interfaces de rede desde a ultima reinicializaçao
	elif command == 'Rede':
		print '---------------------------'
		print 'Comando usado ', command
		print '---------------------------'
		getinfo(chat_id)
		# pegar a quantidade de dados enviados pelo Wireless desde a ultima reinicialização  
		# trocar o wlan0 pela sua interface wireless
		rx_wifi = commands.getoutput("cat /sys/class/net/wlan0/statistics/rx_bytes")
		bot.sendMessage(chat_id,'Quantidade de banda recebida pela rede Wifi: ')
		bot.sendMessage(chat_id,str(rx_wifi))
		
		# pega a quantidade de dados recebidas pelo cabo desde a ultima reinicialização
		# trocar o wlan0 pela sua interface de rede semfio
		tx_wifi = commands.getoutput("cat /sys/class/net/wlan0/statistics/tx_bytes")
		bot.sendMessage(chat_id,'Quantidade de banda enviada pela rede Wifi: ')
		bot.sendMessage(chat_id,str(tx_wifi)
		
		# pega a quantidade de dados enviados pelo cabo desde a ultima reinicialização
		# trocar o eth0 pela sua interface de rede cabeada
		rx_cable = commands.getoutput("cat /sys/class/net/eth0/statistics/rx_bytes")
		bot.sendMessage(chat_id,'Quantidade de banda recebida pela rede cabeada: ')
		bot.sendMessage(chat_id,str(rx_cable))
		
		# pega a quantidade de dados recebidos pelo cabo desde a ultima reinicialização
		# trocar o eth0 pela sua interface de rede cabeada
		tx_cable = commands.getoutput("cat /sys/class/net/eth0/statistics/tx_bytes")
		bot.sendMessage(chat_id,'Quantidade de banda enviada pela rede cabeada')
		bot.sendMessage(chat_id,str(tx_cable))
		
	# oitava verificação verifica se o comando ip foi executado
	# se executado verifica o chat_id de quem solicitou se o 
	# chat_id do solicitante for igual aos listados 
	# abaixo ele retorna o endereço de ip local e externo
	elif command == 'IP':
		print '---------------------------'
		print 'Comando usado ', command
		print '---------------------------'
		# ip local 
		if chat_id == 345318600 or chat_id == 83074778 or chat_id == 24774270:
			
			# aqui pega o ip da lan   ** eth0 para cabo wlan0 para wifi **
			ip_lan = commands.getoutput("ifconfig eth0 |  grep inet | cut -c 21-37 | head -1")
			bot.sendMessage(chat_id, 'Endereço de ip local :')
			bot.sendMessage(chat_id,str(ip_lan))
			
			#ip externo so pra min
			if chat_id == 345318600:	
				# aqui pega o ip externo dessa bagaça 
				response = urllib2.urlopen('http://bot.whatismyipaddress.com/')
				ip_ex = response.read()			
				bot.sendMessage(chat_id, 'Endereço de ip externo :')
				bot.sendMessage(chat_id,str(ip_ex))
	
		else:
			bot.sendMessage(chat_id, 'Sai daqui voce nao vai ver o meu endereço de IP!!! ')
  		
		getinfo(chat_id)	
	
		
	
	# IF do menu de ajuda agora tem alguma coisa pra ajudar 	
	elif  command == '/help':
		print '---------------------------'
		print 'Comando usado ', command
		print '---------------------------'
		bot.sendMessage(chat_id, 'Menu de Ajuda. Encontre aqui informações sobre os comandos')
		bot.sendMessage(chat_id, 'Comando Temperatura --> Comando que tem como função retornar ao usuario as informações de temperatura da CPU')
		bot.sendMessage(chat_id, 'Comando Processos --> Comando que tem como função contar e retornar ao usuario a quantidade de processos que estao sendo execuados')
		bot.sendMessage(chat_id, 'Comando Memoria --> Comando que tem como funçao retornar ao usuario dados da memoria como memoria total, memoria em uso e memoria livre')
		bot.sendMessage(chat_id, 'Comando UpTime --> Comando que tem como funçao retornar ao usuario a informaçao do UpTime do sistema ou seja a quanto tempo a maquina esta ligada')
		bot.sendMessage(chat_id, 'Comando UsoSD --> Comando que tem como função retornar informação de espaço utilizando e espaço livre na partição principal do sistema')
		bot.sendMessage(chat_id, 'Comando Data --> Comando que tem como funçao retornar ao usuario a Hora e Data exatas do sistema')
		bot.sendMessage(chat_id, 'Comando Rede --> Comando que tem como funçao medir e retornar ao usuario a quantidade de banda que foi utilizada em Upload e Download tanto em Wifi ou Ethernet')
		bot.sendMessage(chat_id, 'Comando IP --> Comando que tem como funçao pegaro IP externo e IP local e retornar para o administrador ambos IPs e para usuarios normais somente o IP local')
					      
		getinfo(chat_id)
		
	# messagem para caso o usuario envie comandos digitados manualmente	
	else:
        	bot.sendMessage(chat_id, 'Use os comandos no teclado')
		bot.sendMessage(chat_id, 'Ainda nao sei ler =(')
		
# Aqui fica API do bot gerada pelo botfather
bot = telepot.Bot('')
bot.message_loop(handle)

print 'Aguardando comandos ...'

while 1:
	time.sleep(5)
