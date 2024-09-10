# Avaliação Sprint 1 - Programa de Bolsas Compass UOL / AWS - turma junho/2024

Avaliação da primeira sprint do programa de bolsas Compass UOL para formação em machine learning para AWS.

***

## Execução (Código Fonte)

Faça um sistema em JavaScript para armazenamento de dados cadastrais. 

**Especificações**:

Passo a passo para iniciar o projeto:

1. Clone o repositório;
2. Substitua o arquivo README.md, colocando sua própria versão;
3. Crie a branch para subir seu código;
4. Faça um arquivo html simples para manipular os dados no cadastro;
5. Desenvolva sua solução colocando seu programa em arquivo.js;
6. Projete o cadastro utilizando o padrão Factory;
7. Os dados mínimos de cadastro são: nome, data de nascimento, telefone e email;
8. Armazene o cadastro aplicando [localStorage](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Client-side_storage#storing_simple_data_%E2%80%94_web_storage), com base [neste código](https://github.com/mdn/learning-area/tree/main/javascript/apis/client-side-storage/web-storage) ;
9. Devem ser permitidas as operações de criação, consulta e deleção dos dados de uma pessoa;
10. À medida que for testando o código na máquina local, suba os arquivos no GitHub;
11. Ao escrever o comentário do commit, utilize os [Commits Semânticos](https://blog.geekhunter.com.br/o-que-e-commit-e-como-usar-commits-semanticos/) .

*Dica 1: lembre de adicionar debug (com console.log()) no seu código para ajudá-lo a identificar e corrigir erros.*

*Dica 2: Além do link de referência do localStorage, há vídeos como estes:*
* [Como gravar dados](https://youtu.be/DvSAbX9o7Uo?feature=shared)
* [Como ler dados](https://youtu.be/IP30D8KqeNE?feature=shared)
* [Como atualizar e remover dados](https://youtu.be/26zf4Gc4sT4?feature=shared)


***

## O que será avaliado?

- Em JavaScript, conforme proposta;
- Seguir as atividades na ordem proposta;
- Organização geral do código fonte:
  - Estrutura de pastas;
  - Estrutura da logica de negócio;
  - Otimização do código fonte (evitar duplicações de código);
- Objetividade do README.md.

***

## Entrega

- Seguir a regra: **o trabalho deve ser individual**;
- Criar uma branch no repositório com o formato nome-sobrenome (Exemplo: daniel-muller);
- Subir o trabalho na branch com um README.md:
  - documentar detalhes sobre como a avaliação foi desenvolvida;
  - apresentar as dificuldades conhecidas;
  - explicar como utilizar o sistema;
- 🔨 colocar o código fonte desenvolvido (Sugestão: pasta `src`);
- O prazo de entrega é até às 14h do dia 08/07/2024 no repositório do github (https://github.com/Compass-pb-aws-2024-JUNHO/sprint-1-pb-aws-junho).

# Avaliação das Sprints 2 e 3 - Programa de Bolsas Compass UOL / AWS - turma JUNHO/2024

Avaliação das segunda e terceira sprints do programa de bolsas Compass UOL para formação em machine learning para AWS.

***

## Execução (Código Fonte)

Faça um sistema em JavaScript/NodeJS que produza uma interface para consulta de API pública. Este sistema deverá estar em container com **Docker**, em cloud AWS. 

**Especificações**:

1. Escolher uma API pública (em <https://any-api.com/> , ou qualquer outra, e **deve ser diferente das demais equipes**);
2. Consumir esta API utilizando NodeJS;
3. Subir esta API utilizando Docker;
4. Criar uma página html para fazer consultas à API construída em NodeJS (pode ser bem simples, o layout não será avaliado).

### Docker

Execução em Docker, dentro da AWS Cloud.

* Subir o projeto NodeJS em Docker na cloud AWS.
* O grupo pode ficar livre quanto à estratégia adotada para executar o Docker na AWS.
* Exemplos de como executar:
  * [Deploy Node js Application on AWS EC2 Server](https://youtu.be/VHzeoDK6L0c?feature=shared)
  * [Docker na AWS: EC2 ou Elastic Beanstalk? O que é melhor?](https://youtu.be/TJSK9MRPZs4?si=FCm_lDQWIVEUAHlj)

***

## O que será avaliado?

- Uso do projeto em NodeJS;
- Solução em Docker;
- Projeto em produção na cloud AWS;
- Seguir as atividades na ordem proposta;
- Subir códigos no git ao longo do desenvolvimento;
- Organização geral do código fonte:
  - Estrutura de pastas;
  - Estrutura da lógica de negócio;
  - Divisão de responsabilidades em arquivos/pastas distintos;
  - Otimização do código fonte (evitar duplicações de código);
- Objetividade do README.md;
- Modelo de organização da equipe para o desenvolvimento do projeto;
- Página criada com acesso online.

***

## Entrega

- **O trabalho deve ser feito em grupos de três ou quatro pessoas**;
- Criar uma branch no repositório com o formato grupo-número (Exemplo: grupo-1);
- Conferir se a API desejada já não foi escolhida por outra equipe;
- Subir o trabalho no repositório da equipe com um README.md:
  - documentar detalhes sobre como a avaliação foi desenvolvida;
  - relatar dificuldades conhecidas;
  - descrever como utilizar o sistema;
  - fornecer a URL para acesso à página;
- 🔨 Disponibilizar o código fonte desenvolvido (Sugestão: pasta `src`);
- Colocar o arquivo com a configuração nginx (se utilizado).
- O prazo de entrega é até às 14h do dia 05/08/2024 no repositório do github (https://github.com/Compass-pb-aws-2024-JUNHO-A/sprints-2-3-pb-aws-junho).

  # Avaliação Sprints 4 e 5 - Programa de Bolsas Compass UOL e AWS - turma junho/2024

Avaliação das quarta e quinta sprints do programa de bolsas Compass UOL para formação em machine learning para AWS.

***

## Execução

1 - Treinar o modelo utilizando SageMaker, a partir do dataset armazenado no AWS RDS, conforme instruções a seguir, e fazer o salvamento do modelo para o S3.

2 - Criar um ambiente Docker no AWS para implementar a API descrita no próximo passo.

3 - Desenvolver um serviço em python (API), utilizando algum framework http (Flask, FastApi...), que deve carregar o modelo treinado do S3 e expor um endpoint para realizar a inferência. O endpoint deve ser um POST com uma rota /api/v1/inference e receber um JSON no corpo da requisição seguindo o exemplo:

```json
{
    "no_of_adults": 3,
    "no_of_children": 3,
    "type_of_meal_plan": "example"
    ...
}
```

A resposta deve seguir este formato:

```json
{
  "result": 1
}
```

4 - Realizar o Deploy do serviço na AWS.

![Esquema mostrando a cloud aws com usuários acessando api gateway esta recebendo o modelo do bucket s3. Sagemaker ligado ao bucket para fornecer o modelo e ao RDS para ler e atualizar o dataset.](assets/sprint4-5.jpg)

***

## Construção do Modelo

O Hotel Reservations Dataset (<https://www.kaggle.com/datasets/ahsan81/hotel-reservations-classification-dataset>) é uma base de dados que trata de informações sobre reservas em hotéis.

Iremos utilizar esse dataset para classificar os dados por faixa de preços de acordo com as informações encontradas em suas colunas (usem o que vocês acharem que faz sentido para análise).

**Queremos saber como cada reserva (cada linha do dataset) se encaixa em qual faixa de preço.** Para isso, a equipe **deve criar uma nova coluna** chamada **label_avg_price_per_room**, que servirá como label para nossa classificação. Essa nova coluna deverá conter número 1 quando a coluna *avg_price_per_room* tiver valor menor ou igual a 85, número 2 quando a coluna *avg_price_per_room* tiver valor maior que 85 e menor que 115 e o valor 3 se a coluna *avg_price_per_room* tiver valor maior ou igual a 115.

Vocês devem então **excluir a coluna avg_price_per_room** e criar um modelo que consiga classificar os dados com base na nova coluna *label_avg_price_per_room*.

Armazene o dataset original e alterado no AWS RDS. O modelo treinado deverá ser armazenado no S3.

Será necessário explicar o porquê da escolha do modelo, como ele funciona. Também será avaliada a taxa de assertividade do modelo.

![Fluxograma para ilustração da descrição do tratamento do modelo.](assets/dataset_schema.png)

***

## O que será avaliado

- Projeto em produção na AWS;
- Código Python utilizado no Sagemaker;
- Código Python usado na infererência (API);
- Código do Dockerfile e/ou docker-compose;
- Sobre o modelo:
  - Divisão dos dados para treino e teste;
  - Taxa de assertividade aceitável (se o modelo está classificando corretamente);
  - Entendimento da equipe sobre o modelo utilizado (saber explicar o que foi feito);
  - Mostrar resposta do modelo para classificação;
- Organização geral do código fonte:
  - Estrutura de pastas;
  - Divisão de responsabilidades em arquivos/pastas distintos;
  - Otimização do código fonte (evitar duplicações de código);
- Objetividade do README.md.

***

## Entrega

- **O trabalho deve ser feito em grupos de três ou quatro pessoas**;
  - **Evitar repetições de grupos de sprints anteriores**;
- Criar uma branch no repositório com o formato grupo-número (Exemplo: grupo-1);
- Subir o trabalho na branch com um README.md:
  - documentar detalhes sobre como a avaliação foi desenvolvida;
  - relatar dificuldades conhecidas;
  - descrever como utilizar o sistema;
- 🔨 Disponibilizar o código fonte desenvolvido (observar estruturas de pastas);
- O prazo de entrega é até às 14h do dia 02/09/2024 no repositório do github (https://github.com/Compass-pb-aws-2024-JUNHO/sprints-4-5-pb-aws-junho).

# Avaliação Sprints 6 e 7 - Programa de Bolsas Compass UOL e AWS - turma junho/2024

Avaliação das sexta e sétima sprints do programa de bolsas Compass UOL para formação em machine learning para AWS.

## Execução (Código Fonte)

Crie uma API que irá capturar uma frase qualquer inserida pelo usuário e transformará essa frase em um audio em mp3 via polly. Após, crie um chatbot que se utilize da API criada.

**Especificações**:

A aplicação deverá ser desenvolvida com o framework 'serverless' e deverá seguir a estrutura que já foi desenvolvida neste repo.

Passo a passo para iniciar o projeto:

1. Crie a branch para o seu grupo e efetue o clone

2. Instale o framework serverless em seu computador. Mais informações [aqui](https://www.serverless.com/framework/docs/getting-started)

```json
npm install -g serverless
```

3. Gere suas credenciais (AWS Acess Key e AWS Secret) na console AWS pelo IAM. Mais informações [aqui](https://www.serverless.com/framework/docs/providers/aws/guide/credentials/)

4. Em seguida insira as credenciais e execute o comando conforme exemplo:

```json
serverless config credentials \
  --provider aws \
  --key AKIAIOSFODNN7EXAMPLE \
  --secret wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
  ```

Também é possivel configurar via [aws-cli](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) executando o comando:

```json
$ aws configure
AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
Default region name [None]: us-east-1
Default output format [None]: ENTER
  ```

#### Observação

As credenciais devem ficar apenas localmente no seu ambiente. Nunca exponha as crendenciais no Readme ou qualquer outro ponto do código.

Após executar as instruções acima, o serverless estará pronto para ser utilizado e poderemos publicar a solução na AWS.

5. Para efetuar o deploy da solução na sua conta aws execute (acesse a pasta `api-tts`):

```
serverless deploy
```

Depois de efetuar o deploy, teremos um retorno semelhante a este:

```bash
Deploying api-tts to stage dev (us-east-1)

Service deployed to stack api-tts-dev (85s)

endpoints:
  GET - https://xxxxxxxxxx.execute-api.us-east-1.amazonaws.com/
  GET - https://xxxxxxxxxx.execute-api.us-east-1.amazonaws.com/v1
functions:
  health: api-tts-dev-health (2.1 kB)
  v1Description: api-tts-dev-v1Description (2.1 kB)
  v2Description: api-tts-dev-v2Description (2.1 kB)
```

6. Abra o browser e confirme que a solução está funcionando colando os 3 endpoints que deixamos como exemplo:

### Rota 1 → Get /

1. Esta rota já está presente no projeto.
2. O retorno rota é:

```json
  {
    "message": "Go Serverless v3.0! Your function executed successfully!",
    "input": { 
        ...(event)
      }
  }
```

3. Status code para sucesso da requisição será `200`.

### Rota 2 → Get /v1

1. Esta rota já está presente no projeto.
2. O retorno rota é:

```json
  {
    "message": "TTS api version 1."
  }
 
```

3. Status code para sucesso da requisição será `200`.


***

Após conseguir rodar o projeto base o objetivo final será divida em duas partes:

## Atividade -> Parte 1

### Rota 3 -> Post /v1/tts

Deverá ser criada a rota `/v1/tts` que receberá um post no formato abaixo:

```json
  {
    "phrase": "converta esse texto para áudio e salve uma referencia no dynamoDB. Caso a referencia já exista me devolva a URL com audio já gerado"
  }
```

- Deverá ser criada uma lógica para que a frase recebida seja um id único (um _hash code_);
- Esse hash será o atributo chave em nosso DynamoDB - exemplo: "Teste 123" será sempre o id "123456";
- O texto da frase recebida deverá ser transformado em áudio via AWS Polly;
- O áudio deverá ser armazenado em um bucket S3 (que deverá ser público, apenas para a nossa avaliação);
- Deverá utilizar a lógica de _hash code_ para verificar se a frase já foi gerada anteriormente;
- Caso o hash (_unique_id_) já exista no DynamoDB entregue o retorno conforme abaixo;
- Caso não exista, faça a geração do áudio, grave no s3 e grave as referências no dynamoDB.

Resposta a ser entregue:

```json
  {
    "received_phrase": "converta esse texto para áudio",
    "url_to_audio": "https://meu-buckect/audio-xyz.mp3",
    "created_audio": "02-02-2023 17:00:00",
    "unique_id": "123456"
  }
```

Exemplos de referência:

- <https://github.com/hussainanjar/polly-lambda> (Python)
- <https://github.com/serverless/examples/tree/v3/aws-python-http-api-with-dynamodb> (Python)

***

## Atividade -> Parte 2

Com base na [Documentação Amazon Lex](https://compasso-my.sharepoint.com/:f:/g/personal/lucas_sousa_compasso_com_br/Eph8d9BDeRhGhBzyoAYRLZUBhfjA54P1-5YHERGaN5_Osg?e=1ibFDI), crie um chatbot utilizando o Amazon Lex V2 e o conecte a uma plataforma de mensageria.

**Especificações**:

- Função do chatbot é de livre escolha do desenvolvedor;
- Conexões: O chatbot deve ser disponibilizado em uma das seguintes plataformas:  
  - Slack - [Conexão Slack](https://docs.aws.amazon.com/pt_br/lex/latest/dg/slack-bot-association.html);  
  - Web - [Web](https://github.com/aws-samples/aws-lex-web-ui);
- Construção:
  - Intents:
    - O chatbot deve possuir ao menos 4 intents distintas;  
  - Slots:
    - Captação de informações presentes no texto;
    - Solicitação de informações quando o slot não for reconhecido;
    - Confirmação de informações;
    - O chatbot deve captar ao menos 3 slots no decorrer do fluxo;
- O chatbot deve utilizar-se de menu com botões (Response Cards);
- Tratamento de erros (fallback);
- Deve ter a opção de enviar a resposta em áudio, utilizando o texto de resposta do chatbot, com uso da API da Parte 1 deste trabalho;
- (Opcional) Uso de conditional branching para controle de fluxos ([Doc Conditional Branching](https://docs.aws.amazon.com/pt_br/lexv2/latest/dg/paths-branching.html));

Ao final, a arquitetura a ser implantada deverá estar assim:

![post-v3-tts](./assets/sprints6-7.jpg)

***

## O que será avaliado?

- Projeto em produção na AWS;
- Em python conforme projeto base disponibilizado;
- Infra-estrutura como codigo;
- Seguir as atividades na ordem proposta;
- Sobre as rotas:
  - Possuir a rota com o retorno esperado (somente campos solicitados conforme especificação);
- Entendimento do chatbot e o que ele soluciona;
- Criatividade em relação ao tema escolhido para o desenvolvimento do chatbot;
- Intents e slots criados e informações que eles se dispõem a obter;
- Organização:  
  - Estrutura de intenções;  
  - Estrutura da lógica de negócio;  
  - Divisão de responsabilidades da equipe;  
  - Funcionalidade do chatbot;
- Objetividade do README.md.

***

## Entrega

- **O trabalho deve ser feito em grupos de três ou quatro pessoas**;
  - Evitar repetições de grupos da sprint anterior;
- Criar uma branch no repositório com o formato grupo-número (Exemplo: grupo-1);
- Subir o trabalho na branch com um Readme.md:
  - Documentar detalhes sobre como a avaliação foi desenvolvida;
  - Dificuldades conhecidas;
  - Como utilizar o sistema;
  - **Export do bot Lex em formato .zip**;
- 🔨 código fonte desenvolvido (observar estruturas de pastas);
- O prazo de entrega é até às 14h do dia 30/09/2024 no repositório do github (https://github.com/Compass-pb-aws-2024-JUNHO/sprints-6-7-pb-aws-junho).

