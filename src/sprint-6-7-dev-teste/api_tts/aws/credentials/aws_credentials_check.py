import os
import time
from pathlib import Path

# Função para limpar o terminal
def clean_terminal():
    # Verifica o sistema operacional e executa o comando adequado
    if os.name == 'nt':  # Para Windows
        os.system('cls')
    else:  # Para Linux ou macOS
        os.system('clear')

# Função para receber o input do usuário
def user_input(msg):
    response = input(msg)
    # Se o input for "skip", retorna imediatamente para pular a verificação
    if response.lower().strip() == "skip":
        print("Pulo solicitado. Executando serverless offline diretamente.")
        exit(0)  # Sai do script e a próxima tarefa será executada
    return response        

# Função para determinar o caminho do arquivo credentials da AWS
def aws_credentials_file_path():
    home_dir = Path.home()
    return home_dir / '.aws' / 'credentials'

# Função para verificar a data de modificação do arquivo de credenciais
def check_credentials_file():
    credentials_path = aws_credentials_file_path()

    if not credentials_path.exists():
        print("Arquivo de credenciais não encontrado.")
        return False

    # Obtendo a data de modificação do arquivo
    last_modified_time = credentials_path.stat().st_mtime
    twelve_hours_ago = time.time() - (12 * 60 * 60)

    # Verificando se o arquivo foi modificado nas últimas 12 horas
    return last_modified_time >= twelve_hours_ago  # Retorna True ou False

# Função para solicitar credenciais AWS do usuário
def ask_for_credentials():
    access_key = user_input("Insira sua AWS Access Key: ")
    secret_key = user_input("Insira sua AWS Secret Key: ")
    session_token = user_input("Insira seu AWS Session Token: ")

    # Limpa o terminal
    clean_terminal()

    return {
        'aws_access_key_id': access_key,
        'aws_secret_access_key': secret_key,
        'aws_session_token': session_token
    }

# Função para salvar credenciais no arquivo
def save_credentials(credentials):
    credentials_path = aws_credentials_file_path()

    # Conteúdo a ser escrito no arquivo credentials
    credentials_content = f"""
[default]
aws_access_key_id = {credentials['aws_access_key_id']}
aws_secret_access_key = {credentials['aws_secret_access_key']}
aws_session_token = {credentials['aws_session_token']}
"""

    # Gravando as novas credenciais no arquivo
    try:
        with open(credentials_path, 'w') as file:
            file.write(credentials_content)
        print("Credenciais salvas com sucesso.")
    except Exception as e:
        print(f"Erro ao salvar credenciais: {e}")

# Função principal que verifica e solicita credenciais
def main():
    # Verifica se o arquivo foi modificado nas últimas 12 horas
    if not check_credentials_file():
        print("As credenciais são antigas ou estão faltando. Solicitando novas credenciais...")
        credentials = ask_for_credentials()
        save_credentials(credentials)
    else:
        print("As credenciais ainda não expiraram.")

# Executa o script
if __name__ == "__main__":
    main()
