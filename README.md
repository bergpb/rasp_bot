# Rasp Bot
Bot do telegram feito em python rodando na raspberry pi usando a biblioteca Telepot

## Telepot
[Telepot](https://github.com/nickoala/telepot)


# Versões


## Versão 1.8
* Novo comando /About
* Nova mensagem de Saudação
* Encaminhamento de mensagens de texto
* Envio de audios

## Versão 1.7
* Correção na saida comando Memoria
* Correção na saida do comando IP
* Substituição do comamdo Processos pelo comando Usuarios 

## Versão 1.6
* Envio de imagens usando qualquer botao do segundo teclado e feito o envio de uma imagem

## Versão 1.5
* Foi adicionado um segundo teclado para funções futuras
* Criado a função next que chama o segundo teclado 
* Criado a função back que chama de volta o primeiro teclado 

## Versão 1.4
* Arquivo de configuraçao externo config.ini usado para guardar API do bot e chat_id com privilegios
* Feita pelo [René](https://github.com/shenef)
* Bug maldito corrigido pelo [Berg](https://github.com/bergpb)

## Versão 1.3 
* Constantes com os chatid do admin e autorizados as verem o ip

## Versão 1.2
* Estruturação do codigo em funçoes facilitando a manutençao e alteração 
* Feita pelo [Douglas Zuqueto](https://github.com/douglaszuqueto/)

## Versão 1.1
* Informações retornadas formatadas com Markedown

## Versão 1.0
* Formatação da saida do comando Rede
* Adicionada data/hora na saida das informações lado servidor

## Versão 0.9
* Adicionado comandos para informações do trafego de banda comando Rede
* Mudança de local do menu de Ajuda do teclado para o /help

## Versão 0.8
* Retornar ip externo apenas para meu usuario
* Melhora na saida do comando UsoSD
* Separaçao das saidas das informações do chat

## Versão 0.7
* Verficação de identidade para retornar o IP apenas para quem tem autorização 
* Utilizaçao de uma API para pegar o ip externo

## Versão 0.6
* Melhorias nas saidas dos comandos Memoria e UsoSD
* Comando IP retornando o ip local da maquina

## Versão 0.5
* Melhora na estetica da saida das informaçoes do lado servidor
* Modificação no codigo evitando repetições
* Correção dos erros de codificação utf-8

## Versão 0.4
* Executa comandos no terminal
* Grava o resultado dos comandos em variaveis
* Retorna o valor das variaveis para o usuario no telegram

## Versão 0.3
* Mostra quem esta utilizando o bot
* Informa se o chat e em grupo ou privado
* Mostra qual comando foi usado

## Versão 0.2
* Teclado com opções 
* Retorno de mensagens 

## Versão 0.1
* Esqueleto do bot
* Estrutura de decisão
