# **Avaliação de Custo de Hospedagem** 

## **👥 Desenvolvedores**

- [Marcel Dupret Lopes Barbosa](https://github.com/MarcelDBarbosa)
- [Monique da Silva Borges](https://github.com/niqueborges)
- [Erick](https://github.com/Erick8874)

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
🚀 **Status:** Finalizado

O projeto de Avaliação de Custo de Hospedagem está completo e o modelo de machine learning foi implantado em produção. A API está operacional e acessível conforme o planejado nas sprints 4 e 5 do programa de bolsas.

---

## **✨ Funcionalidades**
1. **Treinamento do Modelo**: 
   - Utilização do AWS SageMaker para treinar um modelo de machine learning que classifica reservas de hotel em diferentes faixas de preço.

2. **API de Inferência**:
   - Desenvolvida utilizando Flask/FastAPI, a API carrega o modelo treinado do S3 e realiza inferências em tempo real com os dados fornecidos.

3. **Deploy na AWS**:
   - A API foi implantada utilizando serviços da AWS, como EC2, Lambda e API Gateway, para garantir alta disponibilidade e escalabilidade.

4. **Persistência de Dados**:
   - O conjunto de dados é armazenado no AWS RDS e o modelo é armazenado no S3.

5. **Infraestrutura como Código**:
   - Dockerfile disponível para containerização e scripts para facilitar o deploy da aplicação.

---

## **⚙️ Arquitetura e Fluxo de Trabalho**
1. **Pré-processamento e Treinamento do Modelo**:
   - Os dados são pré-processados para criar a coluna `label_avg_price_per_room`, que classifica as reservas. O modelo é então treinado no AWS SageMaker e armazenado no S3.

2. **API de Inferência**:
   - A API carrega o modelo treinado do S3 e oferece um endpoint POST `/api/v1/inference` para inferências baseadas nos dados de reserva.

3. **Deploy**:
   - A aplicação foi implantada em uma instância EC2 da AWS, com configuração de segurança apropriada para tráfego HTTP/HTTPS.

---

## **🗃️ Banco de Dados**
- **AWS RDS**: Usado para armazenar tanto o conjunto de dados original quanto o processado.
- Para rodar localmente, é necessário configurar um banco de dados no AWS RDS e obter as credenciais de conexão.

---

## **⚙️ Variáveis de Ambiente**
Para configurar o ambiente de desenvolvimento, crie um arquivo `.env` na raiz do projeto e adicione as seguintes variáveis:

| Variável         | Descrição                                      | Exemplo                                                      |
|------------------|------------------------------------------------|--------------------------------------------------------------|
| `AWS_ACCESS_KEY` | Chave de acesso da AWS                         | `EXAMPLE1234567890`                                          |
| `AWS_SECRET_KEY` | Chave secreta da AWS                           | `exampleSecretKey1234567890`                                 |
| `S3_BUCKET_NAME` | Nome do bucket S3 onde o modelo está armazenado | `hotel-reservations-models`                                  |
| `RDS_CONNECTION` | String de conexão para o AWS RDS               | `host=hostname user=username password=password dbname=dbname`|

---

## **📦 Como Rodar a Aplicação**

### **Utilizando Docker:**
1. **Clone o repositório:**
   ```bash
   git clone -b grupo-1 https://github.com/Compass-pb-aws-2024-JUNHO/sprints-4-5-pb-aws-junho.git
   ```

2. **Crie a imagem Docker para a API:**
   ```bash
   docker build -t hotel-reservations-api .
   ```

3. **Execute o container Docker:**
   ```bash
   docker run -p 80:5000 hotel-reservations-api
   ```

### **Sem Docker:**
1. **Clone o repositório:**
   ```bash
   git clone -b grupo-1 https://github.com/Compass-pb-aws-2024-JUNHO/sprints-4-5-pb-aws-junho.git
   ```

2. **Instale as dependências:**
   ```bash
   pip install -r api/requirements.txt
   ```

3. **Execute a aplicação:**
   ```bash
   python api/app.py
   ```

   - Acesse a API em: `http://localhost:5000/api/v1/inference`

---

## **🚀 Deploy**
### **AWS EC2**:
1. Crie uma instância EC2 na região us-east-1.
2. Conecte-se via SSH à instância e instale o Docker.
3. Faça o pull da imagem Docker e execute o container.
4. Configure o security group para permitir tráfego HTTP/HTTPS.

---

## **💻 Tecnologias Utilizadas**
- **Python**
- **AWS S3**
- **AWS RDS**
- **AWS SageMaker**
- **Flask**
- **FastAPI**
- **Docker**
- **Git**

---

## **📂 Estrutura de Diretórios**

```plaintext
src/
│
├── assets/                            # Recursos visuais e outros assets
│   ├── dataset_schema.png
│   └── sprint4-5.jpg
├── config/                            # Configurações e arquivos relacionados
│   ├── .dockerignore
│   ├── .gitignore
│   ├── accuracy.txt
│   ├── dockerfile                     # Dockerfile movido para config
│   └── requirements.txt               # Dependências do projeto
├── data/                              # Conjuntos de dados utilizados no projeto
│   ├── raw/                           # Dados brutos
│   │   └── Hotel Reservations.csv
│   ├── processed/                     # Dados processados
│   │   └── Hotel Reservations Quantif.csv
├── models/                            # Modelos e scripts relacionados a modelos
│   ├── kernel_svm.py
│   ├── logistic_regression.py
│   ├── random_forest_classification.py
│   ├── xg_boost.py
│   ├── xgboost-model/                 # Modelo treinado e outros artefatos
│   ├── XGBoostSage.ipynb
│   └── model.pkl                      # Arquivo do modelo salvo
├── scripts/                           # Scripts e pipelines de processamento
│   ├── data_processing/               # Scripts relacionados ao processamento de dados
│   │   └── converte_csv.py
│   ├── training/                      # Scripts relacionados ao treinamento do modelo
│   │   └── train_model.py
│   ├── inference/                     # Scripts para inferência e previsões
│   │   ├── main.py
│   │   └── previsoes.py
├── LICENSE                            # Licença do projeto
└── README.md                          # Documentação do projeto



```

---

## **📐 Padrões Utilizados**

- **Commits Semânticos**: Todos os commits seguem o padrão de commits semânticos para manter o histórico do Git organizado.
- **Estrutura de Pastas**: A estrutura do projeto é organizada por responsabilidade, separando a API, o modelo e outros componentes.

---

## **📅 Metodologia de Desenvolvimento**

- **Scrum**: A metodologia Scrum foi aplicada utilizando o Trello para gerenciar as tarefas em sprints:

  - **Sprint 1**: Pré-processamento e treinamento do modelo.
  - **Sprint 2**: Desenvolvimento da API e Dockerização.
  - **Sprint 3**: Deploy e validação do sistema.

---

## **😿 Principais Dificuldades**
- **Configuração do SageMaker**: Lidar com grandes volumes de dados no AWS SageMaker.
- **Otimização de Performance**: Melhorar o tempo de resposta da API durante o carregamento do modelo.

---

## **📝 Licença**

Este projeto é licenciado sob a [Licença MIT](src/LICENSE).

---

<div align="center">
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="Python" height="30" width="40">
  <img src="https://img.shields.io/badge/Amazon_AWS-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white" alt="AWS" height="30" width="40">
  <img src="https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white" alt="Docker" height="30" width="40">
</div>

Este README foi preparado para garantir que todos os aspectos do projeto sejam claros e bem documentados, alinhando-se às melhores práticas recomendadas pelo programa de bolsas da Compass UOL e AWS.

--- 

