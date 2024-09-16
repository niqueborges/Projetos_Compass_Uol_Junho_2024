import boto3
import telebot
from fuzzywuzzy import fuzz, process

# tokens
BOT_TOKEN = ''  # telebot
AWS_ACCESS_KEY = ''
AWS_SECRET_KEY = ''
AWS_REGION = ''
LEX_BOT_NAME = ''
LEX_BOT_ALIAS = ''

# Inicializando o bot do Telegram
bot = telebot.TeleBot(BOT_TOKEN)

# Inicializando o cliente do Amazon Lex
lex_client = boto3.client(
    'lex-runtime',
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=AWS_REGION
)

# Lista dinâmica de diagnóstico
diagnosticos_hardware = {
    "O computador não liga": [
        "computador não liga", "pc não liga", "não consigo ligar o computador", "não inicia", "o pc está morto",
        "não dá sinal", "luz do pc não acende", "o pc está desligado"
    ],
    "Tela preta ao ligar": [
        "tela preta", "sem imagem no monitor", "monitor não liga", "liguei e a tela não aparece nada",
        "pc liga mas a tela fica preta", "o monitor está em preto", "monitor não dá sinal"
    ],
    "Reinicializações aleatórias": [
        "reinicia sozinho", "reboots aleatórios", "reinicia sem aviso", "computador reiniciando",
        "pc reiniciando sozinho", "meu pc reinicia do nada", "reinicialização aleatória", "reset automático"
    ],
    "Ruídos anormais": [
        "ruídos estranhos", "barulhos no computador", "pc fazendo barulho", "ruído esquisito", "sons incomuns",
        "barulho no ventilador", "barulho estranho no cooler", "o pc está muito barulhento"
    ],
    "Desempenho lento": [
        "computador lento", "pc devagar", "lentidão", "demora para abrir programas", "lento",
        "o pc está muito lento", "demora para iniciar", "programas demorando a abrir", "velocidade baixa"
    ],
    "Superaquecimento": [
        "esquentando muito", "superaquecido", "pc aquecendo", "temperatura alta", "calor excessivo",
        "cpu esquentando", "o pc está muito quente", "aquecimento da máquina"
    ]
}

# Função para o Lex e receber a resposta
def consultar_lex(user_input, user_id):
    try:
        response = lex_client.post_text(
            botName=LEX_BOT_NAME,
            botAlias=LEX_BOT_ALIAS,
            userId=user_id,  # Use um identificador único para o usuário
            inputText=user_input
        )
        return response.get('message', "Não foi possível obter uma resposta no momento.")
    except Exception as e:
        return f"Erro ao consultar o Lex: {str(e)}"

# Função para corrigir entradas de texto com erros de digitação usando fuzzywuzzy
def corrigir_mensagem(input_user, diagnosticos):
    todas_frases = [frase for lista in diagnosticos.values() for frase in lista]
    melhor_correspondencia, pontuacao = process.extractOne(input_user, todas_frases, scorer=fuzz.token_set_ratio)
    if pontuacao >= 70:  # Pontuação de igualdade com a palavra
        return melhor_correspondencia
    else:
        return None

# iniciar o chatbot
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Olá! Eu sou o HelpDesk bot, seu assistente técnico de hardware. Descreva o problema que você está enfrentando, e eu vou tentar diagnosticá-lo e encontrar soluções!")

# Func diagnosticar o problema e corrigir a mensagem
@bot.message_handler(func=lambda message: True)
def diagnosticar_problema(message):
    user_input = message.text.lower()
    user_id = message.from_user.id

    # Corrigir a mensagem do usuário usando fuzzywuzzy
    input_corrigido = corrigir_mensagem(user_input, diagnosticos_hardware)

    if input_corrigido:
        # Identificar o problema associado à correspondência
        for problema, frases in diagnosticos_hardware.items():
            if input_corrigido in frases:
                # Envia o input corrigido para o Amazon Lex
                resposta_lex = consultar_lex(problema, user_id)
                bot.reply_to(message, f"Você quis dizer: '{input_corrigido}'?\n{resposta_lex}")
                return
    else:
        bot.reply_to(message, "Desculpe, não consegui entender o problema. Tente ser mais específico ou verifique se descreveu corretamente.")

# Inicializando o telebot
bot.polling()
