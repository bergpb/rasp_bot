# -*- coding: utf-8 -*-

# bibliotecas que estao sendo usadas 
import time
import telepot
import urllib2
import commands
import configparser
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

# conexao com o arquivo de configuraçao externo config.ini
config = configparser.ConfigParser()
config.read('config.ini')
# bot API 
BOT_API = config['BOT_API'] ['api']
# id do administrador
admin_id = config['ADMIN'] ['id'] 
admin_id = int(admin_id)
# id autorizado 1
autho_1 = config['AUTHORIZED'] ['id_1']
autho_1 = int(autho_1)
# id autorizado 2
autho_2 = config['AUTHORIZED'] ['id_2']
autho_2 = int(autho_2)

# teclado que aparece para o usuario 
keyboard = ReplyKeyboardMarkup(
	keyboard=[
		[KeyboardButton(text="Temperatura"), KeyboardButton(text="Usuarios")],
       		[KeyboardButton(text="Memoria"), KeyboardButton(text="UpTime")],
       		[KeyboardButton(text="UsoSD"), KeyboardButton(text="Data")],
       		[KeyboardButton(text="Rede"), KeyboardButton(text="IP")],
       		[KeyboardButton(text="NEXT")],
])
# segund teclado chamado ao clicar em next
newkeyboard = ReplyKeyboardMarkup(
	keyboard=[
        	[KeyboardButton(text="..."), KeyboardButton(text="...")],
        	[KeyboardButton(text="..."), KeyboardButton(text="...")],
        	[KeyboardButton(text="..."), KeyboardButton(text="...")],
        	[KeyboardButton(text="..."), KeyboardButton(text="...")],
        	[KeyboardButton(text="BACK")],
])

# inicia o bot quando /start e enviado
# envia messagens de boas vindas e ativa o primeiro teclado
def start(chat_id, command):
	bot.sendMessage(chat_id, ' Este bot foi criado por @joao_slv =)')
	bot.sendMessage(chat_id, 'https://github.com/joaovitor57/rasp_bot/')
	bot.sendMessage(chat_id, ' Use os comandos do teclado abaixo:', reply_markup=keyboard)
# função temperature executa leitura e  retorna 
# o valor atual da temperatura da cpu em Celsius 
def temperature(chat_id, command):
	temp = commands.getoutput("vcgencmd measure_temp | cut -c 6-12")
	bot.sendMessage(chat_id, '*Temperatura atual da CPU: *', parse_mode="Markdown")
	bot.sendMessage(chat_id, "`%s`" % temp, parse_mode="Markdown")

# busca  quais usuarios estao logados no sistema
def users(chat_id, command):
	sesr = commands.getoutput("w")
		
	bot.sendMessage(chat_id, '*Usuarios logados no sistema: *', parse_mode="Markdown")
	bot.sendMessage(chat_id, "`%s`" % users, parse_mode="Markdown")
	bot.sendMessage(chat_id, '*Hora que foi feito o login: *', parse_mode="Markdown")
	bot.sendMessage(chat_id, "`%s`" % hora_login, parse_mode="Markdown")
	bot.sendMessage(chat_id, '*IP de onde esta logado sessão : *', parse_mode="Markdown")
	bot.sendMessage(chat_id, "`%s`" % local_login, parse_mode="Markdown")

# função memory informa o status da memoria RAM total, em uso e livre
# memoria total
def memory(chat_id, command):
	mem_total = commands.getoutput("free -h | grep 'Mem' | cut -c 15-18")
	bot.sendMessage(chat_id, '*Memoria total: *', parse_mode="Markdown")
	bot.sendMessage(chat_id, "`%s`MB" % mem_total, parse_mode="Markdown")
# memoria em uso
	mem_used = commands.getoutput("free -h | grep 'Mem' | cut -c 27-30")
	bot.sendMessage(chat_id, '*Memoria em uso: *', parse_mode="Markdown")
	bot.sendMessage(chat_id, "`%s`MB" % mem_used, parse_mode="Markdown")
# memoria livre
	mem_free = commands.getoutput("free -h | grep 'Mem' | cut -c 76-78")
	bot.sendMessage(chat_id, '*Memoria livre: *', parse_mode="Markdown")
	bot.sendMessage(chat_id, "`%s`MB" % mem_free, parse_mode="Markdown")
# retorna o uptime do sistema
def upTime(chat_id, command):
	uptime = commands.getoutput("uptime -p")
	bot.sendMessage(chat_id, '*Up Time do sistema: *',parse_mode="Markdown")
	bot.sendMessage(chat_id,  "_%s_" % uptime, parse_mode="Markdown")

#verifica a capacidade total do hd e retorna a sua utilização
def sdCard(chat_id, command):
	sd = commands.getoutput("df -h | grep '/dev'| head -1")
	bot.sendMessage(chat_id, '*Uso do MicroSD: *', parse_mode="Markdown")
	bot.sendMessage(chat_id,  "`%s`" % sd, parse_mode="Markdown")
# informa o date time atual do sistema 
def date(chat_id, command):
	date = commands.getoutput("date")
	bot.sendMessage(chat_id,'*Data e hora do Sistema: *', parse_mode="Markdown")
	bot.sendMessage(chat_id,  "_%s_" % date, parse_mode="Markdown")
# informaçoes sobre a quantidade de dados trafegados 
# pelas interfaces de rede disponiveis no dispositivo
def network(chat_id, command):
# quantidade de dados recebidos via wireless
	rx_wifi = commands.getoutput("cat /sys/class/net/wlan0/statistics/rx_bytes")
	bot.sendMessage(chat_id, '*Quantidade de banda recebida pela rede Wifi: *', parse_mode="Markdown")
	rx_float = float(rx_wifi)
	rx_float_mb = rx_float / 1024 / 1024
	if rx_float_mb > 1024:
		rx_float_gb = rx_float_mb / 1024
		bot.sendMessage(chat_id, '`%.2f Gbs`' % rx_float_gb, parse_mode="Markdown")
	else:
		bot.sendMessage(chat_id, '`%.2f Mbs`' % rx_float_mb, parse_mode="Markdown")
# quantidade de dados eviados via wireless
	tx_wifi = commands.getoutput("cat /sys/class/net/wlan0/statistics/tx_bytes")
	bot.sendMessage(chat_id, '*Quantidade de banda enviada pela rede Wifi: *', parse_mode="Markdown")
	tx_float = float(tx_wifi)
	tx_float_mb = tx_float / 1024 / 1024
	if tx_float_mb > 1024:
		tx_float_gb = tx_float_mb / 1024
		bot.sendMessage(chat_id, '`%.2f Gbs`' % tx_float_gb, parse_mode="Markdown")
	else:
		bot.sendMessage(chat_id, '`%.2f Mbs`' % tx_float_mb, parse_mode="Markdown")
# quantidade de dados recebidos via cabo ethernet
	rx_cable = commands.getoutput("cat /sys/class/net/eth0/statistics/rx_bytes")
	bot.sendMessage(chat_id, '*Quantidade de banda recebida pela rede cabeada: *', parse_mode="Markdown")
	rx_float = float(rx_cable)
	rx_float_mb = rx_float / 1024 / 1024
	if rx_float_mb > 1024:
		rx_float_gb = rx_float_mb / 1024
		bot.sendMessage(chat_id, '`%.2f Gbs`' % rx_float_gb, parse_mode="Markdown")
	else:
		bot.sendMessage(chat_id, '`%.2f Mbs`' % rx_float_mb, parse_mode="Markdown")
# quantidade de dados enviados via cabo ethernet
	tx_cable = commands.getoutput("cat /sys/class/net/eth0/statistics/tx_bytes")
	bot.sendMessage(chat_id, '*Quantidade de banda enviada pela rede cabeada: *', parse_mode="Markdown")
	tx_float = float(tx_cable)
	tx_float_mb = tx_float / 1024 / 1024
	if tx_float_mb > 1024:
		tx_float_gb = tx_float_mb / 1024
		bot.sendMessage(chat_id, '`%.2f Gbs`' % tx_float_gb, parse_mode="Markdown")
	else:
		bot.sendMessage(chat_id, '`%.2f Mbs`' % tx_float_mb, parse_mode="Markdown")

# faz a leitura dos indereços ip e retorna apenas para os autorizados		
def ip(chat_id, command):
# verifica se o chat id e igual ao do admin ou de alguns dos autorizados
	if chat_id == admin_id or chat_id == autho_1 or chat_id == autho_2:
# pega o ip local da maquina por meio de comandos no terminal
		ip_lan = commands.getoutput("ifconfig wlan0 |  grep inet | cut -c 13-27 | head -1")
		bot.sendMessage(chat_id, '*IP local: *', parse_mode="Markdown")
		bot.sendMessage(chat_id, '%s' % ip_lan, parse_mode="Markdown")
# verifica se o chat id e igual ao do admin 
		if chat_id == admin_id:
# pega o ip externo atraves de api 
			response = urllib2.urlopen('http://bot.whatismyipaddress.com/')
			ip_ex = response.read()
			bot.sendMessage(chat_id, '*IP externo: *', parse_mode="Markdown")
			bot.sendMessage(chat_id, '`%s`' % ip_ex, parse_mode="Markdown")
# se o chat id nao estiver na lista retonar essa menssagem
	else:	
		bot.sendMessage(chat_id, 'Voce nao pode ver o meu IP')
		bot.sendMessage(chat_id, '127.0.0.1') 
		
def next(chat_id, command):
	bot.sendMessage(chat_id,'Teclado 2 como novos comandos', reply_markup=newkeyboard)
	
def back(chat_id, command):
	bot.sendMessage(chat_id,'Teclado 1 de volta', reply_markup=keyboard)

# funçao help informa dados referentes aos comandos
def help(chat_id, command):
	bot.sendMessage(chat_id, 'Ajuda. Encontre aqui informacoes sobre os comandos')
	bot.sendMessage(chat_id, '*Comando Temperatura*', parse_mode="Markdown") 
	bot.sendMessage(chat_id, 'Comando que tem como funcao retornar ao usuario as informacoes de temperatura da CPU')
	time.sleep(0.5)
	bot.sendMessage(chat_id, '*Comando Usuarios*', parse_mode="Markdown")
	bot.sendMessage(chat_id, 'Comando que tem como funcao contar e retornar a quais usuario que estao logados no sistema')
	time.sleep(0.5)
	bot.sendMessage(chat_id, '*Comando Memoria*', parse_mode="Markdown") 
	bot.sendMessage(chat_id, 'Comando que tem como funcao retornar ao usuario dados da memoria como memoria total, memoria em uso e memoria livre')
	time.sleep(0.5)
	bot.sendMessage(chat_id, '*Comando UpTime*', parse_mode="Markdown")
	bot.sendMessage(chat_id, 'Comando que tem como funcao retornar ao usuario a informacao do UpTime do sistema ou seja a quanto tempo a maquina esta ligada')
	time.sleep(0.5)
	bot.sendMessage(chat_id, '*Comando UsoSD*', parse_mode="Markdown")
	bot.sendMessage(chat_id, 'Comando que tem como funcao retornar informacao de espaco utilizando e espaco livre na particao principal do sistema')
	time.sleep(0.5)
	bot.sendMessage(chat_id, '*Comando Data*', parse_mode="Markdown")
	bot.sendMessage(chat_id, 'Comando que tem como funcao retornar ao usuario a Hora e Data exatas do sistema')
	time.sleep(0.5)
	bot.sendMessage(chat_id, '*Comando Rede*', parse_mode="Markdown")
	bot.sendMessage(chat_id, 'Comando que tem como funcao medir e retornar ao usuario a quantidade de banda que foi utilizada em Upload e Download tanto em Wifi ou Ethernet')
	time.sleep(0.5)
	bot.sendMessage(chat_id, '*Comando IP*', parse_mode="Markdown")
	bot.sendMessage(chat_id, 'Comando que tem como funcao pegar o IP externo e IP local e retornar para o administrador ambos IPs e para usuarios normais somente o IP local')

# Função principal do bot, estrutura de decisão 
def handle(msg):
	
	command = msg['text']
	content_type, chat_type, chat_id = telepot.glance(msg)
	m = telepot.namedtuple.Message(**msg)

	# dados do utilizados do BOT
	def getinfo(chat_id):
		if chat_id < 0:
			print 'Comando usado -->', command 
			print '---------------------------'
			print 'Menssage do tipo %s: \n' % (content_type,)
			print 'Chat ID do Grupo : %s' % m.chat[0] 
			print 'Tipo de chat : %s' % m.chat[1]
			print 'Nome do Grupo: %s' % m.chat[2]
			print 'Chat Id User: %s' % m.from_[0]
			print 'Username: %s' % m.from_[3] 
			print 'First Name : %s' % m.from_[1]
			print 'Last Name: %s' % m.from_[2]
			print time.strftime('%Y-%m-%d %H:%M:%S')
			print '--------------------------------------'
		else:
			print 'Comando usado -->', command
			print '---------------------------'
			print 'Messagem do tipo %s: \n' % (content_type,)
			print 'Chat ID : %s' % m.chat[0] 
			print 'Tipo de chat : %s' % m.chat[1]
			print 'Username : %s' % m.chat[3] 
			print 'First Name: %s' % m.chat[4]
			print 'Last Name: %s' % m.chat[5]
			print time.strftime('%Y-%m-%d %H:%M:%S')
			print '--------------------------------------'

	if command == '/start':
		start(chat_id, command)
		getinfo(chat_id)

	elif command == 'Temperatura':
		temperature(chat_id, command)
		getinfo(chat_id)

	elif command == 'Usuarios':
		users(chat_id, command)
		getinfo(chat_id)

	elif command == 'Memoria':
		memory(chat_id, command)
		getinfo(chat_id)

	elif command == 'UpTime':
		upTime(chat_id, command)
		getinfo(chat_id)

	elif command == 'UsoSD':
		sdCard(chat_id, command)
		getinfo(chat_id)

	elif command == 'Data':
		date(chat_id, command)
		getinfo(chat_id)

	elif command == 'Rede':
		network(chat_id, command)
		getinfo(chat_id)

	elif command == 'IP':
		ip(chat_id, command)
		getinfo(chat_id)

	elif command == '/help':
		help(chat_id, command)
		getinfo(chat_id)

	elif command == 'NEXT':
		next(chat_id, command)
		getinfo(chat_id)
	
	elif command == '...':
		imagem = "http://i0.kym-cdn.com/entries/icons/mobile/000/004/815/lologuy.jpg" ## link da imagem a ser enviada
		bot.sendPhoto(chat_id, imagem, "") ## funcao que envia a mensagem com a imagem

	elif command == 'BACK':
		back(chat_id,command)
		getinfo(chat_id)

# menssagem de erro caso o usuario digite alguma coisa manualmente
	else:
		bot.sendMessage(chat_id, 'Use os comandos no teclado')
		bot.sendMessage(chat_id, 'Ainda nao sei ler =(')

# colocar aqui a API do bot gerada pelo botfather
bot = telepot.Bot(BOT_API)
bot.message_loop(handle)

print 'Aguardando comandos ...'

# loop while que mantem o bot rodando por tempo indeterminado
while 1:
	time.sleep(5)
