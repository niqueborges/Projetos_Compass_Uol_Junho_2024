Aqui está o **README.md** atualizado para o seu projeto de API Text-to-Speech (TTS) com AWS:

# **API TTS - Text-to-Speech**

## **👥 Desenvolvedores**

| [<img loading="lazy" src="https://avatars.githubusercontent.com/u/173844994?v=4" width="115" alt="Erick Felix de Oliveira">](https://github.com/Erick8874) <br>[*Erick Felix de Oliveira](https://github.com/Erick8874) | [<img loading="lazy" src="https://avatars.githubusercontent.com/u/173863078?v=4" width="115" alt="Marcel Barbosa">](https://github.com/MarcelDBarbosa) <br>[Marcel Barbosa](https://github.com/MarcelDBarbosa) | [<img loading="lazy" src="https://avatars.githubusercontent.com/u/95103547?v=4" width="115" alt="Monique da Silva Borges">](https://github.com/niqueborges) <br>[Monique da Silva Borges*](https://github.com/niqueborges) |
|:---:|:---:|:---:|

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
🚀 **Status:** Em andamento.

O projeto está em desenvolvimento, com a implementação da API de Text-to-Speech utilizando AWS Polly, DynamoDB, S3, e Lambdas gerenciados pelo Serverless Framework.

---

## **✨ Funcionalidades**
1. **Geração de Áudio a partir de Texto**: A API converte texto para áudio utilizando o Amazon Polly.
2. **Verificação no DynamoDB**: Antes de gerar o áudio, a API verifica se a frase já foi convertida e armazenada anteriormente.
3. **Armazenamento de Áudio no S3**: O áudio gerado é armazenado no Amazon S3, e a URL é retornada ao usuário.
4. **Hashing**: A API gera um hash único para cada frase convertida, garantindo que áudios não sejam gerados duplicadamente para a mesma entrada.
5. **API REST**: Disponibiliza endpoints HTTP para enviar frases e recuperar o áudio gerado.

---

## **⚙️ Arquitetura e Fluxo de Trabalho**

1. **Entrada de Texto**:
   - O usuário faz uma requisição `POST` com uma frase para `/v1/tts`.
   
2. **Verificação no DynamoDB**:
   - A frase é transformada em um hash, e o sistema verifica no **DynamoDB** se o hash já existe.
   
3. **Geração do Áudio**:
   - Se o hash não existir, o texto é enviado para o **Amazon Polly**, que gera o áudio.
   
4. **Armazenamento no S3**:
   - O áudio gerado é armazenado no **Amazon S3** e o DynamoDB é atualizado com o hash e a URL do áudio.
   
5. **Resposta**:
   - A API retorna a URL do áudio junto com outras informações, como o hash da frase e um timestamp.

---

## **🗃️ Banco de Dados**
- **DynamoDB**: Usado para armazenar o hash das frases e suas respectivas URLs no S3. Cada registro contém:
  - `unique_id`: O hash da frase.
  - `phrase`: A frase original.
  - `audio_url`: A URL do áudio gerado no S3.
  - `timestamp`: Data e hora da criação.

---

## **⚙️ Variáveis de Ambiente**
Para configurar o ambiente de desenvolvimento, adicione as seguintes variáveis no arquivo `~/.aws/credentials`:

| Variável                | Descrição                                       | Exemplo                                                      |
|-------------------------|-------------------------------------------------|--------------------------------------------------------------|
| `aws_access_key_id`     | Chave de acesso da AWS                          | EXAMPLE1234567890                                            |
| `aws_secret_access_key` | Chave secreta da AWS                            | exampleSecretKey1234567890                                   |
| `aws_session_token`     | Token da Sessão (caso necessário)               | EXAMPLETOKEN123456                                           |

---

## **📦 Como Rodar a Aplicação**

### **Usando Serverless Framework**:
1. **Clone o repositório**:
   ```bash
   git clone https://github.com/usuario/api-tts.git
   cd api-tts
   ```

2. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Deploy da aplicação no AWS**:
   ```bash
   serverless deploy
   ```

4. **Teste a API localmente**:
   ```bash
   serverless invoke local --function v1Description
   ```

---

## **🚀 Deploy**
O deploy é realizado com o Serverless Framework, que gerencia as funções Lambda, S3, Polly e DynamoDB no AWS.

### **AWS Services Utilizados**:
- **Lambda**: Para executar a lógica de conversão de texto para áudio.
- **API Gateway**: Gerenciar endpoints HTTP da API.
- **Polly**: Para gerar o áudio a partir do texto.
- **DynamoDB**: Para armazenar as frases e URLs dos áudios.
- **S3**: Para armazenar os arquivos de áudio gerados.

---

## **💻 Tecnologias Utilizadas**
- **Python 3.12**
- **AWS Lambda**
- **AWS Polly**
- **AWS S3**
- **AWS DynamoDB**
- **Serverless Framework**
- **Boto3 (SDK AWS para Python)**

---

## **📂 Estrutura de Diretórios**

```plaintext
api-tts/
│
├── handler.py                 # Funções principais da Lambda
├── requirements.txt           # Dependências do projeto Python
├── serverless.yml             # Configuração do Serverless Framework
├── utils/                     # Módulos utilitários para AWS (DynamoDB, Polly, S3)
│   ├── dynamo_utils.py
│   ├── polly_utils.py
│   └── s3_utils.py
├── tests/                     # Testes unitários
│   ├── test_handler.py
│   ├── test_dynamo_utils.py
│   ├── test_polly_utils.py
│   └── test_s3_utils.py
└── README.md                  # Documentação do projeto
```

---

## **📐 Padrões Utilizados**

- **Commits Semânticos**: Os commits seguem o padrão semântico para manter o histórico do Git organizado.
- **Modularização**: Código dividido em módulos (`utils/`) para facilitar a manutenção e testes.
- **Serverless**: Utilização do Serverless Framework para gerenciar a infraestrutura.

---

## **📅 Metodologia de Desenvolvimento**
- **Scrum**: Utilizado para organizar as tarefas e o progresso do desenvolvimento em sprints.

---

## **😿 Principais Dificuldades**
- **Configuração de Permissões AWS**: Configurar permissões adequadas para interação entre Polly, S3 e DynamoDB.
- **Sincronização com o DynamoDB**: Garantir que as frases não sejam duplicadas com hashes diferentes.
- **Limitação de Tamanho de Áudio do Polly**: Gerenciamento de frases muito longas.

---

## **📝 Licença**
Este projeto é licenciado sob a [Licença MIT](LICENSE).

---

<div align="center">
   <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python" height="30" width="40">
   <img src="https://img.shields.io/badge/Amazon_AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white" alt="Amazon AWS" height="30" width="40">
   <img src="https://img.shields.io/badge/Serverless-000000?style=for-the-badge&logo=serverless&logoColor=white" alt="Serverless" height="30" width="40">
   <img src="https://img.shields.io/badge/docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker" height="30" width="40">
</div>

---

Este README fornece uma visão geral e instruções completas para a configuração, deploy e utilização da API