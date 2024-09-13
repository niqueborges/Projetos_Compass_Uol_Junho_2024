# **API TTS - Text-to-Speech**

## **👥 Desenvolvedores**
(Preencha com os nomes dos desenvolvedores)

---

## **📑 Índice**
- [📈 Status do Projeto](#-status-do-projeto)
- [✨ Funcionalidades](#-funcionalidades)
- [⚙️ Arquitetura e Fluxo de Trabalho](#-arquitetura-e-fluxo-de-trabalho)
- [🗃️ Banco de Dados](#-banco-de-dados)
- [⚙️ Variáveis de Ambiente](#-variáveis-de-ambiente)
- [📦 Como Rodar a Aplicação](#-como-rodar-a-aplicação)
- [🚀 Deploy](#-deploy)
- [💻 Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [📂 Estrutura de Diretórios](#-estrutura-de-diretórios)
- [📐 Padrões Utilizados](#-padrões-utilizados)
- [📅 Metodologia de Desenvolvimento](#-metodologia-de-desenvolvimento)
- [😿 Principais Dificuldades](#-principais-dificuldades)
- [📝 Licença](#-licença)

---

## **📈 Status do Projeto**
🚀 **Status**: Em andamento

Este projeto tem como objetivo o desenvolvimento de uma API de Text-to-Speech (TTS) utilizando a AWS Polly para conversão de textos em áudio, armazenamento dos arquivos no S3, e uso do DynamoDB para gerenciar metadados. A API será integrada futuramente a um chatbot com Amazon Lex para fornecer respostas em áudio.

---

## **✨ Funcionalidades**
1. **Conversão de Texto para Áudio**:
   - A API recebe frases via POST, gera um hash exclusivo da frase e verifica no DynamoDB se o áudio já foi gerado. Caso contrário, um novo arquivo de áudio é criado pelo Polly e armazenado no S3.
   
2. **Integração com Chatbot Amazon Lex** (em desenvolvimento):
   - Um chatbot será capaz de capturar informações dos usuários e retornar respostas em formato de áudio usando a API TTS.

3. **Persistência de Dados**:
   - Frases e metadados são armazenados no DynamoDB, enquanto os arquivos de áudio são salvos no S3.

---

## **⚙️ Arquitetura e Fluxo de Trabalho**
A arquitetura do projeto envolve os seguintes componentes:

1. **API de TTS**:
   - Ao receber uma frase, a API gera um hash único. Este hash é usado como chave no DynamoDB para verificar se o áudio correspondente já foi criado. Se não, o Polly gera o áudio e o arquivo é salvo no S3. O registro com a URL do áudio é gravado no DynamoDB.
   
   Exemplo de requisição POST:
   ```json
   {
     "phrase": "converta esse texto para áudio e salve uma referencia no dynamoDB."
   }
   ```

   Exemplo de resposta:
   ```json
   {
     "received_phrase": "converta esse texto para áudio",
     "url_to_audio": "https://meu-bucket/audio-xyz.mp3",
     "created_audio": "02-02-2023 17:00:00",
     "unique_id": "123456"
   }
   ```

2. **Chatbot com Amazon Lex**:
   - O chatbot utilizará intents para interagir com os usuários e fornecer respostas em áudio. A integração com a API TTS permitirá que o Lex utilize essa funcionalidade.

---

## **🗃️ Banco de Dados**
O projeto utiliza dois principais serviços de armazenamento:

- **DynamoDB**: Armazena o hash das frases e suas respectivas URLs no S3. Campos importantes:
  - `unique_id`: Hash gerado a partir da frase.
  - `phrase`: A frase original.
  - `audio_url`: URL do áudio gerado e armazenado no S3.
  - `timestamp`: Data e hora de criação do registro.

- **S3**: Armazena os arquivos de áudio gerados pela API TTS.

---

## **⚙️ Variáveis de Ambiente**
Para configurar o ambiente de desenvolvimento, adicione suas credenciais da AWS no arquivo `~/.aws/credentials`. As variáveis essenciais incluem:

| Variável                | Descrição                                       | Exemplo                        |
|-------------------------|-------------------------------------------------|--------------------------------|
| `aws_access_key_id`     | Chave de acesso da AWS                          | EXAMPLE1234567890              |
| `aws_secret_access_key` | Chave secreta da AWS                            | exampleSecretKey1234567890     |
| `aws_session_token`     | Token da Sessão (se necessário)                 | EXAMPLETOKEN123456             |

---

## **📦 Como Rodar a Aplicação**

### **Pré-requisitos**:
- **Serverless Framework** instalado.
- Credenciais AWS configuradas corretamente.

### **Passos**:

1. **Clone o repositório e crie uma branch para o grupo**:
   ```bash
   git clone https://github.com/Compass-pb-aws-2024-JUNHO/sprints-6-7-pb-aws-junho.git
   git checkout -b grupo-n
   ```

2. **Instale o Serverless Framework** (se necessário):
   ```bash
   npm install -g serverless
   ```

3. **Configure as credenciais AWS**:
   ```bash
   serverless config credentials --provider aws --key <AWS_ACCESS_KEY> --secret <AWS_SECRET_KEY>
   ```

4. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Execute o deploy da aplicação**:
   ```bash
   cd api-tts
   serverless deploy
   ```

6. **Verifique os endpoints gerados** e utilize a rota `/v1/tts` para transformar texto em áudio.

7. **Teste a API localmente**:
   ```bash
   serverless invoke local --function v1Description
   ```

---

## **🚀 Deploy**
O deploy é realizado via **Serverless Framework**, que configura e gerencia os serviços AWS necessários:

- **Lambda** para a lógica de conversão.
- **API Gateway** para exposição das rotas.
- **Polly** para geração de áudio.
- **DynamoDB** e **S3** para armazenamento de dados e arquivos.

---

## **💻 Tecnologias Utilizadas**
- **Python 3.9**
- **AWS Lambda**
- **AWS Polly**
- **AWS S3**
- **AWS DynamoDB**
- **Serverless Framework**
- **Boto3 (SDK AWS para Python)**
- **Git**

<div align="center">
   <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python" height="30" width="40">
   <img src="https://img.shields.io/badge/Amazon_AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white" alt="Amazon AWS" height="30" width="40">
   <img src="https://img.shields.io/badge/Serverless-000000?style=for-the-badge&logo=serverless&logoColor=white" alt="Serverless" height="30" width="40">
   <img src="https://img.shields.io/badge/GIT-E44C30?style=for-the-badge&logo=git&logoColor=white" alt="Git" height="30" width="40">
</div>

---

---

## **📂 Estrutura de Diretórios**

```plaintext
src/
│
├── assets/                    # Recursos visuais
│   └── sprint6-7.jpg
│
├── api-tts/                   # Código da API TTS
│   ├── handler.py             # Funções Lambda principais
│   ├── requirements.txt       # Dependências Python
│   ├── serverless.yml         # Configuração do Serverless Framework
│   └── utils/                 # Módulos utilitários (DynamoDB, Polly, S3)
│       ├── dynamo_utils.py
│       ├── polly_utils.py
│       └── s3_utils.py
├── tests/                     # Testes unitários
│   └── test_handler.py
├── chatbot/                   # Chatbot com Amazon Lex
│   └── intents/
├── .gitignore
├── LICENSE                            # Licença do projeto
└── README.md                          # Documentação do projeto
```

---

## **📐 Padrões Utilizados**
- **Commits Semânticos**: Para manter um histórico claro e organizado.
- **Modularização**: Código dividido em módulos para facilitar manutenção e testes.
- **Serverless Framework**: Utilizado para gestão e deploy da infraestrutura.

---

## **📅 Metodologia de Desenvolvimento**
Adotamos a metodologia **Scrum**, com duas sprints principais:

- **Sprint 6**: Foco no desenvolvimento da API TTS e deploy na AWS.
- **Sprint 7**: Integração do chatbot com o Amazon Lex e sua conexão com a API TTS.

---

## **😿 Principais Dificuldades**
- **Configuração do Serverless**: Ajustes complexos nas permissões e autenticação com AWS.
- **Controle de Permissões AWS**: Gerenciar as permissões adequadas para que Polly, S3 e DynamoDB interajam corretamente.
- **Gerenciamento de Frases Longas no Polly**: Ajustar limites do Polly para frases muito extensas.

---

## **📝 Licença** 
Este projeto está licenciado sob a [Licença MIT](LICENSE).

---


Este README foi estruturado conforme as melhores práticas recomendadas no Programa de Bolsas Compass UOL e AWS.
