import telebot
from fuzzywuzzy import fuzz, process

# Configurações
TOKEN = '7276005402:AAHf9cYWY9kqKA-IvEblxlM-AJElFCTbGT0'
MATCH_THRESHOLD = 70  # Pontuação mínima para correspondência

bot = telebot.TeleBot(TOKEN)

# Diagnósticos de hardware
DIAGNOSTICOS_HARDWARE = {
    "O computador não liga": [
        "computador não liga", "pc não liga", "não consigo ligar o computador", "não inicia", "o pc está morto"
    ],
    "Tela preta ao ligar": [
        "tela preta", "sem imagem no monitor", "monitor não liga", "liguei e a tela não aparece nada"
    ],
    "Reinicializações aleatórias": [
        "reinicia sozinho", "reboots aleatórios", "reinicia sem aviso", "computador reiniciando"
    ],
    "Ruídos anormais": [
        "ruídos estranhos", "barulhos no computador", "pc fazendo barulho", "ruído esquisito", "sons incomuns"
    ],
    "Desempenho lento": [
        "computador lento", "pc devagar", "lentidão", "demora para abrir programas", "lento"
    ],
    "Superaquecimento": [
        "esquentando muito", "superaquecido", "pc aquecendo", "temperatura alta", "calor excessivo"
    ]
}

# Soluções para problemas de hardware
SOLUCOES_HARDWARE = {
    "O computador não liga": [
        "Verificar se o cabo de energia está conectado corretamente",
        "Verificar se a fonte de alimentação está funcionando",
        "Problema na placa-mãe",
        "Problema na fonte de alimentação"
    ],
    "Tela preta ao ligar": [
        "Verificar se o monitor está ligado e conectado",
        "Problema na placa de vídeo",
        "Problema com a memória RAM",
        "Problema na BIOS"
    ],
    "Reinicializações aleatórias": [
        "Superaquecimento da CPU",
        "Problema com a fonte de alimentação",
        "Falha de memória RAM",
        "Conexões soltas na placa-mãe"
    ],
    "Ruídos anormais": [
        "Problema com ventoinhas ou cooler",
        "Disco rígido com falha",
        "Fonte de alimentação defeituosa",
        "Componentes soltos"
    ],
    "Desempenho lento": [
        "Falta de memória RAM",
        "Processador sobrecarregado",
        "Disco rígido muito cheio ou fragmentado",
        "Problemas de driver"
    ],
    "Superaquecimento": [
        "Verificar o cooler da CPU",
        "Checar se a ventoinha está funcionando corretamente",
        "Trocar a pasta térmica",
        "Limpar poeira interna do gabinete"
    ]
}

# Funções de diagnóstico e resposta
def encontrar_diagnostico(mensagem_usuario):
    """Encontra o diagnóstico baseado na entrada do usuário com tolerância a erros."""
    todas_variacoes = [variacao for variacoes in DIAGNOSTICOS_HARDWARE.values() for variacao in variacoes]
    correspondencia, pontuacao = process.extractOne(mensagem_usuario, todas_variacoes, scorer=fuzz.token_set_ratio)
    if pontuacao >= MATCH_THRESHOLD:
        for problema, variacoes in DIAGNOSTICOS_HARDWARE.items():
            if correspondencia in variacoes:
                return problema
    return None

def gerar_resposta_diagnostico(problema):
    """Gera a resposta com base no problema identificado."""
    solucoes = SOLUCOES_HARDWARE.get(problema, [])
    return f"Possíveis soluções para '{problema}':\n" + "\n".join(solucoes)

# Handlers do bot
@bot.message_handler(commands=['start', 'help'])
def enviar_boas_vindas(message):
    bot.reply_to(message, "Olá! Eu sou o HelpDesk bot, seu assistente técnico de hardware. Descreva o problema e tentarei encontrar uma solução.")

@bot.message_handler(func=lambda message: True)
def diagnosticar_problema(message):
    mensagem_usuario = message.text.lower()
    problema_encontrado = encontrar_diagnostico(mensagem_usuario)
    
    if problema_encontrado:
        resposta = gerar_resposta_diagnostico(problema_encontrado)
        bot.reply_to(message, resposta)
    else:
        bot.reply_to(message, "Desculpe, não consegui identificar o problema. Tente ser mais específico.")

# Inicialização do bot
bot.polling()

