#!/usr/bin/python
# -*- coding: UTF-8 -*-

# importaçao das bibliotecas que estao sendo usadas 
import time
import telepot
import urllib2
import commands
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

# primeira função que inicia o bot quando 
# clicado em começar ou enviado /start
# envia messagens de boas vindas e ativa o teclado
def start():
  bot.sendMessage(chat_id, ' Bem Vindo!!')
  bot.sendMessage(chat_id, ' Bot desenvolvido por @joao_slv')
  bot.sendMessage(chat_id, ' Iniciando o Bot...')
  bot.sendMessage(chat_id, ' Use os comandos do teclado abaixo: ', reply_markup=keyboard)

# função temperature verifica qual opçao do teclado
# foi selecionada e se o command for igual a temperatura 
# executa o conteudo da funçao fazendo a leitura da temperatura
# e gravnado em uma variacel que sera retornada para o usuario do bot
def temperature(chat_id, command):
  print '---------------------------'
  print 'Comando usado ', command
  print '---------------------------'
  temp = commands.getoutput("vcgencmd measure_temp | cut -c 6-12")
  bot.sendMessage(chat_id, 'Temperatura atual: ')
  bot.sendMessage(chat_id, str(temp))


# função process verifica qual opçao do teclado
# foi selecionada e se o command for igual a process
# executa o conteudo da funçao fazendo de contar quantos
# processo estao ativos rodando no momento e gravando 
# em uma variavel que sera retornada para o usuario do bot
def process(chat_id, command):
  print '---------------------------'
  print 'Comando usado ', command
  print '---------------------------'
  quantProc = commands.getoutput("ps -aux | wc -l")
  bot.sendMessage(chat_id, 'Quantidade de processos rodando e :')
  bot.sendMessage(chat_id, str(quantProc))

# função memory verifica qual opçao do teclado
# foi selecionada e se o command for igual a memory
# executa o conteudo da funçao fazendo uma leitura da 
# quantidade de memoria total, memoria em uso e memoria livre
# gravando  em uma variavel que sera retornada para o usuario do bot
def memory(chat_id, command):
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

# funçao upTime verifica qual opção do teclado
# foi selecionada e se o command for igual a upTime
# executa o conteudo da funçao que pega o upTime 
# do sistema(tempo ativo desde a ultima reinicialização)
# gravando  em uma variavel que sera retornada para o usuario do bot
def upTime(chat_id, command):
  print '---------------------------'
  print 'Comando usado ', command
  print '---------------------------'
  uptime = commands.getoutput("uptime -p")
  bot.sendMessage(chat_id, 'Up Time do sistema: ')
  bot.sendMessage(chat_id, str(uptime))

# funçao sdCard verifica qual opção do teclado
# foi selecionada e se o command for igual a 
# sdCard executa o conteudo da funçao que realiza
# uma leitura do estado de uso do MicroSD 
# ou HD que esta em uso gravando  em uma variavel 
# que sera retornada para o usuario do bot
def sdCard(chat_id, command):
  print '---------------------------'
  print 'Comando usado ', command
  print '---------------------------'
  sd = commands.getoutput("df -h | grep '/dev'| head -1")
  bot.sendMessage(chat_id, 'Estado do MicroSD: ')
  bot.sendMessage(chat_id, str(sd))

# funçao date verifica qual opção do teclado
# foi selecionada e se o command foi igual a 
# date executa o conteudo da funçao que pega
# a data/hora atual do sistema e grava em uma
# variavel e retorna para  usuario do bot
def date(chat_id, command):
  print '---------------------------'
  print 'Comando usado ', command
  print '---------------------------'
  date = commands.getoutput("date")
  bot.sendMessage(chat_id, 'Data e hora do Sistema: ')
  bot.sendMessage(chat_id, str(date))

# funçao network verifica qual opção do teclado 
# foi selecionada e se o command foi igual a network
# executa o conteudo da função que faz a leitura 
# da quantidade de banda enviada e recebida pelas 
# interfaces de rede disponiveis ao sistemas
# sejam elas redes wireless ou rede ethernet grava
# em uma variavel e retonar para o usuario do bot
def network(chat_id, command):
  print '---------------------------'
  print 'Comando usado ', command
  print '---------------------------'
# pega a quantidade de dados recebidos pela rede wireless
  rx_wifi = commands.getoutput("cat /sys/class/net/wlan0/statistics/rx_bytes")
  bot.sendMessage(chat_id, 'Quantidade de banda recebida pela rede Wifi: ')
  rx_float = float(rx_wifi)
  rx_float_mb = rx_float / 1024 / 1024
  if rx_float_mb > 1024:
    rx_float_gb = rx_float_mb / 1024
    bot.sendMessage(chat_id, '%.2f Gbs' % rx_float_gb)
  else:
    bot.sendMessage(chat_id, '%.2f Mbs' % rx_float_mb)
# pega a quantidade de dados eviados pela rede wireless
  tx_wifi = commands.getoutput("cat /sys/class/net/wlan0/statistics/tx_bytes")
  bot.sendMessage(chat_id, 'Quantidade de banda enviada pela rede Wifi: ')
  tx_float = float(tx_wifi)
  tx_float_mb = tx_float / 1024 / 1024
  if tx_float_mb > 1024:
    tx_float_gb = tx_float_mb / 1024
    bot.sendMessage(chat_id, '%.2f Gbs' % tx_float_gb)

  else:
    bot.sendMessage(chat_id, '%.2f Mbs' % tx_float_mb)
# pega a quantidade de dados recebidos pela rede ethernet
  rx_cable = commands.getoutput("cat /sys/class/net/eth0/statistics/rx_bytes")
  bot.sendMessage(chat_id, 'Quantidade de banda recebida pela rede cabeada: ')
  rx_float = float(rx_cable)
  rx_float_mb = rx_float / 1024 / 1024
  if rx_float_mb > 1024:
    rx_float_gb = rx_float_mb / 1024
    bot.sendMessage(chat_id, '%.2f Gbs' % rx_float_gb)

  else:
    bot.sendMessage(chat_id, '%.2f Mbs' % rx_float_mb)
# pega quantidade de dados enviados pela rede ethernet
  tx_cable = commands.getoutput("cat /sys/class/net/eth0/statistics/tx_bytes")
  bot.sendMessage(chat_id, 'Quantidade de banda enviada pela rede cabeada')
  tx_float = float(tx_cable)
  tx_float_mb = tx_float / 1024 / 1024
  if tx_float_mb > 1024:
    tx_float_gb = tx_float_mb / 1024
    bot.sendMessage(chat_id, '%.2f Gbs' % tx_float_gb)

  else:
    bot.sendMessage(chat_id, '%.2f Mbs' % tx_float_mb)
	
# funçao ip verifica qual opção do teclado foi 
# selecionada e se o command for igual a ip
# executa o conteudo da função que pega o valor do ip local
# atraves de comandos e o ip externo atraves de uma API 
# grava em uma variavel e retorna para usuario do bot
def ip(chat_id, command):
  print '---------------------------'
  print 'Comando usado ', command
  print '---------------------------'
  # ip local para quem tem permissao do 
  if chat_id == 345318600 or chat_id == 83074778 or chat_id == 24774270:

    # aqui pega o ip da lan   **Trocar o eth0 para sua interface de rede**
    ip_lan = commands.getoutput("ifconfig wlan0 |  grep inet | cut -c 21-37 | head -1")
    bot.sendMessage(chat_id, 'Endereço de ip local :')
    bot.sendMessage(chat_id, str(ip_lan))

    # ip externo so para o administrador
    if chat_id == 345318600:
    # aqui pega o ip externo usando uma API
      response = urllib2.urlopen('http://bot.whatismyipaddress.com/')
      ip_ex = response.read()
      bot.sendMessage(chat_id, 'Endereço de ip externo :')
      bot.sendMessage(chat_id, str(ip_ex))

  else:
    bot.sendMessage(chat_id, 'Sai daqui voce nao vai ver o meu endereço de IP!!!')

# funçao help verifica se o command e igual a /help 
# (nao tem no teclado tem que ser digitado manual igua la /start)
# entao retornar infomaçoes de funcionamento de todos os comandos
# disponiveis no bot para o usuario
def help(chat_id, command):
  print '---------------------------'
  print 'Comando usado ', command
  print '---------------------------'
  bot.sendMessage(chat_id, 'Ajuda. Encontre aqui informações sobre os comandos')
  bot.sendMessage(chat_id,
                  'Comando Temperatura :: Comando que tem como função retornar ao usuario as informações de temperatura da CPU')
  bot.sendMessage(chat_id,
                  'Comando Processos :: Comando que tem como função contar e retornar ao usuario a quantidade de processos que estao sendo execuados')
  bot.sendMessage(chat_id,
                  'Comando Memoria :: Comando que tem como funçao retornar ao usuario dados da memoria como memoria total, memoria em uso e memoria livre')
  bot.sendMessage(chat_id,
                  'Comando UpTime :: Comando que tem como funçao retornar ao usuario a informaçao do UpTime do sistema ou seja a quanto tempo a maquina esta ligada')
  bot.sendMessage(chat_id,
                  'Comando UsoSD :: Comando que tem como função retornar informação de espaço utilizando e espaço livre na partição principal do sistema')
  bot.sendMessage(chat_id,
                  'Comando Data :: Comando que tem como funçao retornar ao usuario a Hora e Data exatas do sistema')
  bot.sendMessage(chat_id,
                  'Comando Rede :: Comando que tem como funçao medir e retornar ao usuario a quantidade de banda que foi utilizada em Upload e Download tanto em Wifi ou Ethernet')
  bot.sendMessage(chat_id,
                  'Comando IP :: Comando que tem como funçao pegaro IP externo e IP local e retornar para o administrador ambos IPs e para usuarios normais somente o IP local')

# Função principal do bot, estrutura de decisão 
def handle(msg):
	
# Configurações da variavel para controlar 
# a estrutura de decisao e tambem a variavel
# que salva os dados do chat em uma tupla 
  command = msg['text']
  content_type, chat_type, chat_id = telepot.glance(msg)
  m = telepot.namedtuple.Message(**msg)


# função criada para fazer uma verificação 
# e ver se a messagem foi enviada de um grupo
# ou de um chat privado e tambem mostrar para
# o responsavel pelo bot quem esta utilizando 
# e quais comandos e em que hora ** NO FUTURO SALVAR ISSO NO BANCO**
  def getinfo(chat_id, content_type):
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
      print time.strftime('%Y-%m-%d %H:%M:%S')
      print '--------------------------------------'
    else:
      print 'Messagem do tipo %s ' % (content_type,)
      print '--------------------------------------'
      print 'Chat ID : %s' % m.chat[0]
      print 'Tipo de chat : %s' % m.chat[1]
      print 'Username : %s' % m.chat[3]
      print 'First Name: %s' % m.chat[4]
      print 'Last Name: %s' % m.chat[5]
      print time.strftime('%Y-%m-%d %H:%M:%S')
      print '--------------------------------------'
	
# Aqui e o teclado que aparece para o usuario 
# as palavras do teclado sao os comanos
# que seram enviadas para a estrutura de decisao
  keyboard = ReplyKeyboardMarkup(
    keyboard=[
      [KeyboardButton(text="Temperatura"), KeyboardButton(text="Processos")],
      [KeyboardButton(text="Memoria"), KeyboardButton(text="UpTime")],
      [KeyboardButton(text="UsoSD"), KeyboardButton(text="Data")],
      [KeyboardButton(text="Rede"), KeyboardButton(text="IP")],
    ])

  if command == '/start':
    start(chat_id, keyboard)
    getinfo(chat_id)

  elif command == 'Temperatura':
    temperature(chat_id, command)
    getinfo(chat_id)

  elif command == 'Processos':
    process(chat_id, command)
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

# menssagem de erro caso o usuario digite alguma coisa manualmente
  else:
    bot.sendMessage(chat_id, 'Use os comandos no teclado')
    bot.sendMessage(chat_id, 'Ainda nao sei ler =(')


bot = telepot.Bot('')
bot.message_loop(handle)

print 'Aguardando comandos ...'

# loop while que mantem o bot rodando por tempo indeterminado
while 1:
  time.sleep(5)
