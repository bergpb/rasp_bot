import telepot
import time

def handle(msg):
    chatid = msg['chat']['id']
    comando = msg['text']
    
     
    
    if comando == '/start':
        bot.sendMessage(chatid,'Bem Vindo!!') 
        bot.sendMessage(chatid,'Bot desenvolvido por @joao_slv!)
        bot.sendMessage(chatid,'Iniciando o Bot...')
        bot.sendMessage(chatid,'Use os comandos do teclado abaixo' )
        
    elif comando == 'Temperatura':
    
    elif comando == 'Memoria':
        
    elif comando == 'UpTime':
   
    elif comando == 'UsoSD':
   
    elif comando == 'Data':
    
    elif comando == 'IP':
    
    elif comando == 'CPU_Info':
    
    elif comando == 'Ajuda':
       
    else:
        bot.sendMessage(chatid, 'Use os comandos no teclado para que possa ter acesso as opções do bot.')

bot = telepot.Bot('346248441;AAEGri00lPsFmKEzshGtthdoEgyawJ08s5k')
bot.message_loop(handle)
              
print 'Aguardando comandos ...'

while 1:
    time.sleep(5)
