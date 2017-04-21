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
   		print 'oi' 		
    	elif comando == 'Memoria':
        	print 'oi'
    	elif comando == 'UpTime':
		print 'oi'   		
    	elif comando == 'UsoSD':
   		print 'oi'
    	elif comando == 'Data':
    		print 'oi'
    	elif comando == 'IP':
    		print 'oi'
    	elif comando == 'CPU_Info':
    		print 'oi'
    	elif comando == 'Ajuda':
       		print 'oi'
    	else:
        	bot.sendMessage(chatid, 'Use os comandos no teclado para... Nem tem teclado aqui')

bot = telepot.Bot('API BOT here')
bot.message_loop(handle)
              
print 'Aguardando comandos ...'

while 1:
    time.sleep(5)
