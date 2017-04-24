import telepot
import time

def handle(msg):
	chatid = msg['chat']['id']
    	comando = msg['text']
    
     
    	if comando == '/start':
        	bot.sendMessage(chatid,'Bem Vindo!!') 
       		bot.sendMessage(chatid,'Bot desenvolvido por @joao_slv!')
        	bot.sendMessage(chatid,'Iniciando o Bot...')
        	bot.sendMessage(chatid,'Iniciado saporra ainda nao faz nada.' )
        
    	elif comando == 'Temperatura':
   		print 'Comando temperatura: ok' 		
    	elif comando == 'Memoria':
        	print 'Comando Memoria: ok'
    	elif comando == 'UpTime':
		print 'Comando UpTime: ok'   		
    	elif comando == 'UsoSD':
   		print 'Comando UsoSD: ok'
    	elif comando == 'Data':
    		print 'Comando Data: oj'
    	elif comando == 'IP':
    		print 'Comando ip: ok'
    	elif comando == 'CPU_Info':
    		print 'comando cpu_info: ok'
    	elif comando == 'Ajuda':
       		print 'comando ajuda: ok'
    	else:
        	bot.sendMessage(chatid, 'Use os comandos no teclado para!! Nem tem teclado aqui ainda ...')

bot = telepot.Bot('API BOT here')
bot.message_loop(handle)
              
print 'Aguardando comandos ...'

while 1:
	time.sleep(5)
